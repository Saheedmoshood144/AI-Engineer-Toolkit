import pandas as pd

from src.predictor import Predictor


predictor = Predictor(
    "models/model.pkl"
)

new_data = pd.DataFrame(
    {
        "age": [28, 50],
        "salary": [
            45000,
            90000
        ]
    }
)

predictions = predictor.predict(
    new_data
)

print(predictions)