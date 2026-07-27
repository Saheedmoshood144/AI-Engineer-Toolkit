import pandas as pd

from src.pipeline import DataPipeline


def test_complete_ml_pipeline(tmp_path):
    """
    Test complete machine learning workflow.
    """

    csv_file = tmp_path / "employees.csv"

    data = pd.DataFrame(
        {
            "age": [20, 25, 30, 35, 40, 45],
            "salary": [
                30000,
                40000,
                50000,
                60000,
                70000,
                80000
            ],
            "target": [
                0,
                0,
                0,
                1,
                1,
                1
            ]
        }
    )

    data.to_csv(
        csv_file,
        index=False
    )

    config = {
        "dataset_path": str(csv_file),
        "target_column": "target",
        "log_level": "INFO"
    }

    pipeline = DataPipeline(config)

    result = pipeline.run()

    assert result is not None

    assert "accuracy" in result
    assert "precision" in result
    assert "recall" in result
    assert "f1_score" in result