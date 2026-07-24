import pandas as pd

from src.dataset import Dataset


def test_clean_removes_missing_values():
    """
    Test that clean() removes rows containing missing values.
    """

    # Create a Dataset object
    dataset = Dataset("employees.csv")

    # Create sample data with missing values
    dataset.data = pd.DataFrame(
        {
            "name": ["John", "Mary", None],
            "age": [25, None, 30]
        }
    )

    # Run cleaning method
    dataset.clean()

    # Check that no missing values remain
    assert dataset.data.isnull().sum().sum() == 0

    # Check that rows with missing values were removed
    assert len(dataset.data) == 1