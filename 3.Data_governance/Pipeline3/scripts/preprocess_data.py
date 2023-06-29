import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('data/housing.csv')

# Assuming data is already clean, split it into train and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Save the datasets to csv files
train.to_csv('data/train.csv', index=False)
test.to_csv('data/test.csv', index=False)
