import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load the training data
data = pd.read_csv('data/train.csv')

# Split into X and y
X = data.drop('Survived', axis=1)
y = data['Survived']

# Train a logistic regression model
clf = LogisticRegression()
clf.fit(X, y)

# Save the trained model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(clf, f)
