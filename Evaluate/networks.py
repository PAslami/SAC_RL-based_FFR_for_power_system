# NETWORKS
import os
import torch as T
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torch.distributions.normal import Normal
import numpy as np 

class CriticNetwork(nn.Module):
    def __init__(self, beta, input_dims, n_actions, fc1_dims=256, fc2_dims=256,
            name='critic', chkpt_dir='tmp/sac'):
        super(CriticNetwork, self).__init__()
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.n_actions = n_actions
        self.name = name
        self.checkpoint_dir = chkpt_dir
        self.checkpoint_file = os.path.join(self.checkpoint_dir, name+'_sac')

        self.fc1 = nn.Linear(self.input_dims[0]+n_actions, self.fc1_dims)
        self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
        self.q = nn.Linear(self.fc2_dims, 1)

        self.optimizer = optim.Adam(self.parameters(), lr=beta)
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')

        self.to(self.device)

    def forward(self, state, action):
        action_value = self.fc1(T.cat([state, action], dim=1))
        action_value = F.relu(action_value)
        action_value = self.fc2(action_value)
        action_value = F.relu(action_value)
        q = self.q(action_value)

        return q

    def save_checkpoint(self):
        T.save(self.state_dict(), self.checkpoint_file)

    def load_checkpoint(self):
        self.load_state_dict(T.load(self.checkpoint_file))

class ActorNetwork(nn.Module):
    def __init__(self, actor_lr, input_dims, max_action, min_action , fc1_dims=256, 
            fc2_dims=256, n_actions= 1, name='actor', chkpt_dir='tmp/sac',  log_sigma_max: float = 2, log_sigma_min: float = -20):## here i am adding the clamping stuff for the log of sigma and also min_action
        super(ActorNetwork, self).__init__()
        self.input_dims = input_dims
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.n_actions = n_actions
        self.name = name
        self.checkpoint_dir = chkpt_dir
        self.checkpoint_file = os.path.join(self.checkpoint_dir, name+'_sac')
        self.max_action = max_action
        self.min_action = min_action
        self.reparam_noise = 1e-6


        ############new addition ##########
        self.log_sigma_max = log_sigma_max
        self.log_sigma_min = log_sigma_min
        ##################################


        self.fc1 = nn.Linear(*self.input_dims, self.fc1_dims)
        self.fc2 = nn.Linear(self.fc1_dims, self.fc2_dims)
        
        self.mu = nn.Linear(self.fc2_dims, self.n_actions)
        # self.tanh = nn.Tanh()
        self.log_sigma = nn.Linear(self.fc2_dims, self.n_actions)

        self.optimizer = optim.Adam(self.parameters(), lr=actor_lr)
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)

        ######## new addition ##########
        self.action_scale = T.as_tensor((self.max_action - self.min_action) / 2.)
        self.action_bias = T.as_tensor((self.max_action + self.min_action) / 2.)
        ############################


    def forward(self, state):
        prob = self.fc1(state)
        prob = F.relu(prob)
        prob = self.fc2(prob)
        prob = F.relu(prob)

        mu = self.mu(prob)

        log_sigma = self.log_sigma(prob)

        log_sigma = T.clamp(log_sigma, min=self.log_sigma_min, max=self.log_sigma_max)  

        sigma = T.exp(log_sigma)

        return mu, sigma

    def sample_normal(self, state, reparameterize=True):
        mu, sigma = self.forward(state)
        probabilities = Normal(mu, sigma)

        if reparameterize:
            actions = probabilities.rsample()
        else:
            actions = probabilities.sample()

        z = T.tanh(actions)
        action = ((z*self.action_scale) + self.action_bias) 
        log_probs = probabilities.log_prob(actions)
        log_probs -= T.log(self.action_scale*(1-z.pow(2))+self.reparam_noise) 
        log_probs = log_probs.sum(1, keepdim=True)


        mu2 = T.tanh(mu) * self.action_scale + self.action_bias 
        

        return action, log_probs, mu2  

    def save_checkpoint(self):
        T.save(self.state_dict(), self.checkpoint_file)

    def load_checkpoint(self):
        self.load_state_dict(T.load(self.checkpoint_file))
