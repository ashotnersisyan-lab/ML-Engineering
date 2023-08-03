from fastapi import FastAPI
from .utils import load_pipeline
import uvicorn
import pandas as pd

app = FastAPI()


pipeline = load_pipeline("/app/classification/model/pipeline.pkl")


@app.post("/predict")
async def predict(data: dict):
    """
    This function predicts the target value of the incoming data point
    and returns the prediction.
    """
    data = pd.DataFrame(data, index=[0])
    prediction = pipeline.predict(data)
    return {"Survived": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
