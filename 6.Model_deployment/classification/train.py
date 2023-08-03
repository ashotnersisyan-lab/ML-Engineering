import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle


def train_model():
    """
    This is a function for preprocessing and training the model
    on train dataset and saving the results as one pipeline
    later to use it to predict the target variable on the raw data
    that will be received.
    """
    # Load the dataset
    data = pd.read_csv('classification/data/train.csv')

    # Define features and target variable
    numeric_features = ['Age', 'SibSp', 'Parch']
    categorical_features = ['Pclass', 'Sex']
    target = 'Survived'

    # Preprocessing steps
    numeric_transformer = SimpleImputer(strategy='mean')
    categorical_transformer = OneHotEncoder()

    preprocessing_steps = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Define the model
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)

    # Create the pipeline: preprocessing + model
    pipeline = Pipeline(steps=[
        ('preprocessing', preprocessing_steps),
        ('model', model)
    ])

    # Fit the pipeline to the training data
    pipeline.fit(data[numeric_features + categorical_features], data[target])

    # Save the pipeline
    with open('classification/model/pipeline.pkl', 'wb') as f:
        pickle.dump(pipeline, f)


if __name__ == "__main__":
    train_model()
