import pandas as pd

from src.model_trainer import ModelTrainer
from src.model_persistence import ModelPersistence
from src.predictor import Predictor


def test_predictor(tmp_path):
    """
    Test loading a saved model and making predictions.
    """

    X = pd.DataFrame(
        {
            "age": [20, 25, 30, 35],
            "salary": [
                30000,
                40000,
                50000,
                60000
            ]
        }
    )

    y = pd.Series(
        [0, 0, 1, 1]
    )

    trainer = ModelTrainer()

    model = trainer.train(
        X,
        y
    )

    model_path = tmp_path / "model.pkl"

    persistence = ModelPersistence()

    persistence.save(
        model,
        str(model_path)
    )

    predictor = Predictor(
        str(model_path)
    )

    predictions = predictor.predict(
        X
    )

    assert len(predictions) == len(X)