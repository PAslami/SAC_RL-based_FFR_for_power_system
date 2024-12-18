import argparse


def create_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--Q1",
        type=float,
        default=0.2,
        help="reward penalizer Q1",
    )
    parser.add_argument(
        "--Q2",
        type=float,
        default=0.3,
        help="reward penalizer Q2",
    )
    parser.add_argument(
        "--R1",
        type=float,
        default=0.005,
        help="reward penalizer R1",
    )

    parser.add_argument(
        "--reset-time",
        type=float,
        default=0.0,
        help="reset time",
    )

    parser.add_argument(
        "--stop-time",
        type=float,
        default=100.0,
        help="simulation stop time",
    )

    parser.add_argument(
        "--step-time",
        type=float,
        default=0.02,
        help="simulation step time",
    )

    parser.add_argument(
        "--load-range",
        type=float,
        default=0.2,
        help="Load (L) to use as load range [-L, +L] while training",
    )

    parser.add_argument(
        "--train", 
        action="store_false", 
        help="whether to conduct training or not"
    )

    parser.add_argument(
        "--save-checkpoint", 
        action="store_false", 
        help="whether to save the checkpoint"
    )

    parser.add_argument(
        "--load-checkpoint", 
        type=str,
        required=False,
        help="Checkpoint to start training from",
        default=None,
    )

    parser.add_argument(
        "--test-load",
        type=float,
        default=None,
        help="value of step load for testing policy",
    )

    parser.add_argument(
        "--models-dir",
        type=str,
        default="trained_SAC",
        help="directory to save trained policies",
    )

    parser.add_argument(
        "--chkpt-dir",
        type=str,
        default="tmp/sac",
        help="directory to save checkpoints",
    )

    parser.add_argument(
        "--input-size",
        type=int,
        default=3,
        help="size of observation input (single dimension)",
    )

    parser.add_argument(
        "--action-size",
        type=int,
        default=1,
        help="size of control action (single dimension)",
    )
    # parser.add_argument(
    #     "--fig-file",
    #     type=str,
    #     default='plots/average_reward_SAC.png',
    #     help="file to reward plot",
    # )

    parser.add_argument(
        "--n-episodes",
        type=int,
        default=4001,
        help="number of episodes for training",
    )

    parser.add_argument(
        "--fig-file",
        type=str,
        default=None,
        help="figure file",
    )


    return parser
