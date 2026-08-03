from pydantic import BaseModel, Field


class EmployeeInput(BaseModel):
    """
    Input schema for employee prediction.
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


class PredictionResponse(BaseModel):
    """
    Prediction API response schema.
    """

    prediction: int
    age: int
    salary: float
    model: str