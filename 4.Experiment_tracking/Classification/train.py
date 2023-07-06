import mlflow
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from hyperopt import fmin, tpe, hp, Trials, STATUS_OK
from hyperopt.pyll.base import scope
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('data/titanic.csv')


# Preprocessing
def preprocess_encoded(df):
    # Drop non-target columns that are hard to encode
    df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    # Encode categorical columns
    le = LabelEncoder()
    df['Sex'] = le.fit_transform(df['Sex'])
    df['Embarked'] = le.fit_transform(df['Embarked'].astype(str))

    # Fill in missing values
    imputer = SimpleImputer(strategy="mean")
    df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    return df


df = preprocess_encoded(df)

y = df['Survived']
X = df.drop('Survived', axis=1)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define search spaces for hyperparameters
logistic_space = {
    'C': hp.uniform('C', 0.01, 10.0),
    'penalty': hp.choice('penalty', ['none', 'l2']),
}

svm_space = {
    'C': hp.uniform('C', 0.01, 10.0),
    'kernel': hp.choice('kernel', ['linear', 'poly', 'rbf', 'sigmoid']),
}

catboost_space = {
    'iterations': scope.int(hp.quniform('iterations', 100, 1000, 100)),
    'depth': scope.int(hp.quniform('depth', 4, 10, 1)),
    'learning_rate': hp.uniform('learning_rate', 0.01, 0.3),
}


# Define optimization function for each model
def optimize_logistic(params):
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    return {'loss': -accuracy, 'status': STATUS_OK}


def optimize_svm(params):
    model = SVC(**params)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    return {'loss': -accuracy, 'status': STATUS_OK}


def optimize_catboost(params):
    model = CatBoostClassifier(**params)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    return {'loss': -accuracy, 'status': STATUS_OK}


models = [
    ('Logistic Regression', logistic_space, optimize_logistic),
    ('SVM', svm_space, optimize_svm),
    ('CatBoost', catboost_space, optimize_catboost),
]

for model_name, space, optimize_func in models:
    # Run experiment
    with mlflow.start_run(run_name=model_name):
        trials = Trials()
        best_params = fmin(
            fn=optimize_func,
            space=space,
            algo=tpe.suggest,
            max_evals=10,
            trials=trials,
        )

        # Log best parameters and accuracy
        mlflow.log_params(best_params)
        best_accuracy = -trials.best_trial['result']['loss']
        mlflow.log_metric('accuracy', best_accuracy)
