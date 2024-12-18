import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt")) as f:
    install_requires = f.readlines()

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name="sacFFR",
    version="0.1",
    description="fast frequency response (FFR) in power system using Reinforcement learning (RL)[Soft Actor Critic (SAC)]",
    url="https://github.com/PAslami/SAC_RL-based_FFR_for_power_system.git",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_dir={"sacFFR": "sacFFR"},
    python_requires=">=3.10",
    install_requires=install_requires,
    author="Pooja Aslami",
    author_email="Pooja.Aslami@jacks.sdstate.edu",
)
