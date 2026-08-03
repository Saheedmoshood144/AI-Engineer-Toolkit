import pandas as pd

from fastapi import FastAPI, HTTPException

from src.logger import get_logger
from src.model_persistence import ModelPersistence
from src.settings import Settings

from api.schemas import (
    EmployeeInput,
    PredictionResponse
)


logger = get_logger(__name__)


# Load application settings first
settings = Settings()


app = FastAPI(
    title=settings.app_name
)


# Load trained model
persistence = ModelPersistence()

model = persistence.load(
    settings.model_path
)

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
settings = Settings()


persistence = ModelPersistence()

model = persistence.load(
    settings.model_path
)




@app.post(
    "/predict",
    response_model=PredictionResponse
)
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
        [
            {
                "age": employee.age,
                "salary": employee.salary
            }
        ]
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