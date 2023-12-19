"""
A script for training an RL agent in a simulated brain-computer interface (BCI) environment.
"""


import numpy as np

# define a constant for eeg data length
EEG_DATA_LENGTH = 1000


# function for generating a random EEG data sample
def generate_eeg_data():
    return np.random.rand(EEG_DATA_LENGTH)


# function for measuring the mean squared error between two EEG data samples
def mse(x, y):
    return np.mean((x - y) ** 2)


# generate 2 random EEG data samples and measure their MSE
x = generate_eeg_data()
y = generate_eeg_data()
print("MSE between two random EEG data samples: {}".format(mse(x, y)))
