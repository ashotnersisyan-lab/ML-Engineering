from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle
import numpy as np

# Load the test data
data = pd.read_csv('data/test.csv')

# Split into X and y
X = data.drop('medv', axis=1)
y = data['medv']

# Load the trained model
with open('models/model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Make predictions on the test set
y_pred = clf.predict(X)

# Calculate the Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Save the RMSE to a txt file
with open('models/rmse.txt', 'w') as f:
    f.write(f'RMSE: {rmse}\n')
