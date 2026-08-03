from fastapi import FastAPI
from pydantic import BaseModel

from src.predictor import Predictor


app = FastAPI(
    title="AI Engineer Toolkit API",
    description="Machine Learning Prediction API",
    version="1.0"
)


predictor = Predictor(
    "models/model.pkl"
)


class PredictionRequest(BaseModel):
    """
    Input features for prediction.
    """

    age: int
    salary: int


@app.get("/")
def home():
    """
    API welcome endpoint.
    """

    return {
        "message": "AI Engineer Toolkit API is running"
    }


@app.get("/health")
def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(
    request: PredictionRequest
):
    """
    Generate model prediction.
    """

    import pandas as pd

    data = pd.DataFrame(
        [
            {
                "age": request.age,
                "salary": request.salary
            }
        ]
    )

    prediction = predictor.predict(
        data
    )

    return {
        "prediction": int(prediction[0])
    }