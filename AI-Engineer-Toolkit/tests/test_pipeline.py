import pandas as pd

from src.pipeline import DataPipeline


def test_pipeline_run(tmp_path):
    """
    Test that the pipeline loads data and removes missing values.
    """

    # Create temporary CSV file
    csv_file = tmp_path / "employees.csv"

    data = pd.DataFrame(
        {
            "name": ["John", "Mary", None],
            "age": [25, None, 30]
        }
    )

    data.to_csv(csv_file, index=False)

    # Create pipeline configuration
    config = {
        "dataset_path": str(csv_file),
        "log_level": "INFO"
    }

    # Create and run pipeline
    pipeline = DataPipeline(config)

    result = pipeline.run()

    # Verify pipeline returned a DataFrame
    assert result is not None
    assert isinstance(result, pd.DataFrame)

    # Verify missing values were removed
    assert result.isnull().sum().sum() == 0

    # Verify rows containing missing values were removed
    assert len(result) == 1