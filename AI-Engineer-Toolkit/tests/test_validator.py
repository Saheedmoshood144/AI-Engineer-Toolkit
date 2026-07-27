import pandas as pd

from src.validator import DatasetValidator


def test_validator_accepts_valid_dataframe():
    """
    Test validation succeeds for valid data.
    """
    data = pd.DataFrame(
        {
            "name": ["John", "Mary"],
            "age": [25, 30]
        }
    )

    validator = DatasetValidator(data)

    assert validator.validate() is True


def test_validator_rejects_empty_dataframe():
    """
    Test validation fails for empty data.
    """
    data = pd.DataFrame()

    validator = DatasetValidator(data)

    assert validator.validate() is False