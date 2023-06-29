import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('data/titanic.csv')

# Preprocessing steps (remove nulls, convert categorical variables, etc.)
data = data.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1)
data = data.dropna()
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
data['Embarked'] = le.fit_transform(data['Embarked'])

# Split the data into train and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Save the datasets to csv files
train.to_csv('data/train.csv', index=False)
test.to_csv('data/test.csv', index=False)
