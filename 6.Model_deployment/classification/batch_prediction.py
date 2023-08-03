import pickle
import pandas as pd
from utils import load_pipeline


def predict():
    """
    This function predicts the target value of the incoming batch
    in this case csv is used for batch predictions.
    """
    # Load the pipeline
    pipeline = load_pipeline("classification/model/pipeline.pkl")

    # Load new data and generate predictions
    data = pd.read_csv('classification/data/test.csv')
    predictions = pipeline.predict(data)

    # Save predictions
    pd.DataFrame(predictions).to_csv('classification/data/predictions.csv')


if __name__ == "__main__":
    predict()
