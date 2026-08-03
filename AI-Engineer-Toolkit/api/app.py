from fastapi import FastAPI
from pydantic import BaseModel

from src.model_persistence import ModelPersistence


app = FastAPI(
    title="AI Engineer Toolkit API",
    description="Machine Learning Prediction API",
    version="1.0"
)


persistence = ModelPersistence()

model = persistence.load(
    "models/model.pkl"
)


class EmployeeInput(BaseModel):
    age: int
    salary: int


@app.get("/")
def home():
    return {
        "message": "AI Engineer Toolkit API running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(
    employee: EmployeeInput
):

    prediction = model.predict(
        [[
            employee.age,
            employee.salary
        ]]
    )


    return {
        "prediction": int(prediction[0])
    }