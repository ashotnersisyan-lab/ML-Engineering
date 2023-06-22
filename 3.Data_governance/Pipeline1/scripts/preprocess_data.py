from sklearn.model_selection import train_test_split
import pandas as pd

# Load data
data = pd.read_csv('data/iris.csv')

# Handle missing values, if any
# For iris dataset, no missing value handling is necessary

# Split data into train and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Save train and test sets
train.to_csv('data/train.csv', index=False)
test.to_csv('data/test.csv', index=False)
