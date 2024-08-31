import panda as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the data

data = pd.read_csv('data.csv')
# Extract the features and target variable

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
# Split the data into training and testing sets
from sklearn.model_selection import train_test_split

