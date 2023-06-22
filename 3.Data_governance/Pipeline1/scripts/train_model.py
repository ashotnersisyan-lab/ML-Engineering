from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

# Load training data
data = pd.read_csv('data/train.csv')

# Split into X and y
X = data.drop('class', axis=1)
y = data['class']

# Train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X, y)

# Save the trained model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(clf, f)
