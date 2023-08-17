from fastapi import FastAPI, Request, HTTPException
import uvicorn
import pandas as pd
import pickle
import json


app = FastAPI()


def load_pipeline(path: str):
    """
    This is a helper function to load the pipeline artefacts.
    """
    with open(path, "rb") as f:
        return pickle.load(f)


pipeline = load_pipeline("/opt/ml/model/pipeline.pkl")


@app.get("/ping")
def read_ping():
    """
    This function is for ping health check of the service.
    """
    return {"ping": "pong"}


@app.post("/invocations")
async def invocations(request: Request):
    """
    This function predicts the target value of the incoming data point
    and returns the prediction.
    """
    try:
        body = await request.body()
        data = body.decode("utf-8")
        data = json.loads(data)
        data_df = pd.DataFrame(data, index=[0])
        prediction = pipeline.predict(data_df)
        return {"Survived": int(prediction[0])}

    except UnicodeDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Unicode decode error: {e}, Raw body: {body}")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
