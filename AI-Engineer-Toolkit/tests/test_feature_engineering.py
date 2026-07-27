import pandas as pd

from src.feature_engineering import FeatureEngineer


def test_drop_columns_removes_existing_column():
    """
    Test that specified columns are removed.
    """

    data = pd.DataFrame(
        {
            "name": ["John", "Mary"],
            "age": [25, 30],
            "salary": [50000, 60000]
        }
    )

    engineer = FeatureEngineer(data)

    result = engineer.drop_columns(["name"])

    assert isinstance(result, pd.DataFrame)
    assert "name" not in result.columns
    assert "age" in result.columns
    assert "salary" in result.columns


def test_drop_columns_ignores_missing_columns():
    """
    Test that removing a non-existing column does not raise an error.
    """

    data = pd.DataFrame(
        {
            "name": ["John", "Mary"],
            "age": [25, 30],
            "salary": [50000, 60000]
        }
    )

    engineer = FeatureEngineer(data)

    result = engineer.drop_columns(["department"])

    assert isinstance(result, pd.DataFrame)
    assert "name" in result.columns
    assert "age" in result.columns
    assert "salary" in result.columns