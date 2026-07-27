import pandas as pd

from src.model_evaluator import ModelEvaluator


def test_model_evaluation():
    """
    Test evaluation metrics calculation.
    """

    y_true = pd.Series(
        [0, 1, 1, 0]
    )

    y_pred = pd.Series(
        [0, 1, 1, 1]
    )

    evaluator = ModelEvaluator()

    metrics = evaluator.evaluate(
        y_true,
        y_pred
    )

    assert isinstance(metrics, dict)

    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "f1_score" in metrics

    assert metrics["accuracy"] == 0.75