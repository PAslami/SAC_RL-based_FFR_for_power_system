# AGENT
import os
import torch as T
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
from buffer import ReplayBuffer
from networks import ActorNetwork, CriticNetwork

class Agent():
    def __init__(self, actor_lr=0.0003, beta=0.0003, input_dims=[3],
            env=None, gamma=0.99, n_actions=1, max_size=1000000, tau=0.005, alpha: float = 0.0042, 
            layer1_size=256, layer2_size=256, batch_size=256): 
        self.gamma = gamma
        self.tau = tau
        self.alpha = alpha

        self.memory = ReplayBuffer(max_size, input_dims, n_actions)
        self.batch_size = batch_size
        self.n_actions = n_actions

        self.actor = ActorNetwork(actor_lr, input_dims, n_actions=n_actions,
                    name='actor', max_action= 0.5,  min_action = -0.5) 
        self.critic_1 = CriticNetwork(beta, input_dims, n_actions=n_actions,
                    name='critic_1')
        self.critic_2 = CriticNetwork(beta, input_dims, n_actions=n_actions,
                    name='critic_2')
        self.target_critic_1 = CriticNetwork(beta, input_dims, n_actions=n_actions,
                    name='target_critic_1')
        self.target_critic_2 = CriticNetwork(beta, input_dims, n_actions=n_actions,
                    name='target_critic_2')

        self.update_network_parameters(tau=1)  

        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')

        
        ################# Entropy initialization################
        self.alpha = T.Tensor([alpha]).to(self.device)
        self.target_entropy = -T.Tensor([n_actions]).to(self.device).item()
        self.log_alpha = T.zeros(1, requires_grad=True, device=self.device)
        self.alpha_optimizer = optim.Adam([self.log_alpha], lr=beta)

    def choose_action(self, observation):
        state = T.Tensor([observation]).to(self.actor.device)
        actions, _, mu2 = self.actor.sample_normal(state, reparameterize=False) 

        return actions.cpu().detach().numpy()[0], mu2.cpu().detach().numpy()[0]

    def remember(self, state, action, reward, new_state, done):
        self.memory.store_transition(state, action, reward, new_state, done)

    def update_network_parameters(self, tau=None):  
        if tau is None:
            tau = self.tau

        target_critic_1_params = self.target_critic_1.named_parameters() 
        target_critic_2_params = self.target_critic_2.named_parameters() 
        target_critic_1_state_dict = dict(target_critic_1_params)
        target_critic_2_state_dict = dict(target_critic_2_params)

        critic_1_params = self.critic_1.named_parameters()
        critic_2_params = self.critic_2.named_parameters()
        critic_1_state_dict = dict(critic_1_params)
        critic_2_state_dict = dict(critic_1_params)

        for name in critic_1_state_dict:
            critic_1_state_dict[name] = tau*critic_1_state_dict[name].clone() + \
                    (1-tau)*target_critic_1_state_dict[name].clone()
        for name in critic_2_state_dict:
            critic_2_state_dict[name] = tau*critic_2_state_dict[name].clone() + \
                    (1-tau)*target_critic_2_state_dict[name].clone()

        self.target_critic_1.load_state_dict(critic_1_state_dict)
        self.target_critic_2.load_state_dict(critic_1_state_dict)

    def save_models(self):
        print('.... saving models ....')
        self.actor.save_checkpoint()
        self.critic_1.save_checkpoint()
        self.critic_2.save_checkpoint()
        self.target_critic_1.save_checkpoint()
        self.target_critic_2.save_checkpoint()


    def load_models(self):
        print('.... loading models ....')
        self.actor.load_checkpoint()
        self.critic_1.load_checkpoint()
        self.critic_2.load_checkpoint()
        self.target_critic_1.save_checkpoint()
        self.target_critic_2.save_checkpoint()

    def learn(self):
        if self.memory.mem_cntr < self.batch_size:
            return

        state, action, reward, new_state, done = \
                self.memory.sample_buffer(self.batch_size)

        reward = T.tensor(reward, dtype=T.float).to(self.actor.device)
        done = T.tensor(done, dtype=T.float).to(self.actor.device)
        state_ = T.tensor(new_state, dtype=T.float).to(self.actor.device)
        state = T.tensor(state, dtype=T.float).to(self.actor.device)
        action = T.tensor(action, dtype=T.float).to(self.actor.device)

        ########### critic optimization #################
        next_actions, next_log_probs, _ = self.actor.sample_normal(state_, reparameterize=False) 
        next_log_probs = next_log_probs.view(-1)
        q1_target_policy = self.target_critic_1.forward(state_, next_actions).view(-1)
        q2_target_policy = self.target_critic_2.forward(state_, next_actions).view(-1)
        q_target = T.min(q1_target_policy, q2_target_policy)
        next_q = reward + (1-done)*self.gamma*(q_target-self.alpha*next_log_probs)
 
        q1_old_policy = self.critic_1.forward(state, action).view(-1)
        q2_old_policy = self.critic_2.forward(state, action).view(-1)  
        critic_1_loss = 0.5 * F.mse_loss(q1_old_policy, next_q)
        critic_2_loss = 0.5 * F.mse_loss(q2_old_policy, next_q)

        critic_loss = critic_1_loss + critic_2_loss

        self.critic_1.optimizer.zero_grad()
        self.critic_2.optimizer.zero_grad()
        critic_loss.backward(retain_graph=True)
        self.critic_1.optimizer.step()
        self.critic_2.optimizer.step()


        ############# actor optimization ################
        actions, log_probs, _ = self.actor.sample_normal(state, reparameterize=True)
        log_probs = log_probs.view(-1)
        q1_new_policy = self.critic_1.forward(state, actions)
        q2_new_policy = self.critic_2.forward(state, actions)
        critic_value = T.min(q1_new_policy, q2_new_policy)
        critic_value = critic_value.view(-1)    

        actor_loss = (self.alpha*log_probs) - critic_value
        actor_loss = T.mean(actor_loss)

        self.actor.optimizer.zero_grad()
        actor_loss.backward(retain_graph=True)
        self.actor.optimizer.step() 

        ############# alpha optimization  ################
        alpha_loss = -(self.log_alpha * (log_probs + self.target_entropy).detach()).mean()    
        self.alpha_optimizer.zero_grad()
        alpha_loss.backward()
        self.alpha_optimizer.step()
        self.alpha = self.log_alpha.exp()   


        ############ target networks weight update ##############
        self.update_network_parameters()  

