import pandas as pd

from src.model_trainer import ModelTrainer


def test_model_training_and_prediction():
    """
    Test model training and prediction.
    """

    X_train = pd.DataFrame(
        {
            "age": [20, 25, 30, 35],
            "salary": [30000, 40000, 50000, 60000]
        }
    )

    y_train = pd.Series(
        [0, 0, 1, 1]
    )

    X_test = pd.DataFrame(
        {
            "age": [40],
            "salary": [70000]
        }
    )

    trainer = ModelTrainer()

    trainer.train(
        X_train,
        y_train
    )

    predictions = trainer.predict(
        X_test
    )

    assert len(predictions) == 1