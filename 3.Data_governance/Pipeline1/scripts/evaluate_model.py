from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

# Load test data
data = pd.read_csv('data/test.csv')

# Split into X and y
X = data.drop('class', axis=1)
y = data['class']

# Load the trained model
with open('models/model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Make predictions on the test set
y_pred = clf.predict(X)

# Calculate the accuracy
accuracy = accuracy_score(y, y_pred)

# Save the accuracy to a txt file in models directory
with open('models/accuracy.txt', 'w') as f:
    f.write(f'Accuracy: {accuracy}\n')