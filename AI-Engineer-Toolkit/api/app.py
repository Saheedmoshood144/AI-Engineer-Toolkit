from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd

from src.logger import get_logger
from src.model_persistence import ModelPersistence


logger = get_logger(__name__)

app = FastAPI()


@app.get("/")
def home():
    """
    Home endpoint.
    """
    return {
        "message": "AI Engineer Toolkit API running"
    }


@app.get("/health")
def health():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy"
    }


# Load saved model once when API starts
persistence = ModelPersistence()

model = persistence.load(
    "models/model.pkl"
)


class EmployeeInput(BaseModel):
    """
    Employee features used for prediction.
    """

    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Employee age"
    )

    salary: float = Field(
        ...,
        ge=0,
        description="Employee salary"
    )


@app.post("/predict")
def predict(employee: EmployeeInput):
    """
    Predict the target class for an employee.
    """

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded."
        )

    logger.info(
        f"Prediction requested: age={employee.age}, salary={employee.salary}"
    )

    input_data = pd.DataFrame(
        [{
            "age": employee.age,
            "salary": employee.salary
        }]
    )

    prediction = model.predict(
        input_data
    )

    logger.info(
        f"Prediction result: {prediction[0]}"
    )

    return {
        "prediction": int(prediction[0]),
        "age": employee.age,
        "salary": employee.salary,
        "model": "LogisticRegression"
    }