import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the training data
data = pd.read_csv('data/train.csv')

# Split into X and y
X = data.drop('medv', axis=1)
y = data['medv']

# Train a linear regression model
clf = LinearRegression()
clf.fit(X, y)

# Save the trained model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(clf, f)
