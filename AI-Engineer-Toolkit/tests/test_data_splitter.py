import pandas as pd

from src.data_splitter import DataSplitter


def test_data_split():
    """
    Test dataset splitting.
    """

    data = pd.DataFrame(
        {
            "age": [20, 25, 30, 35, 40],
            "salary": [30000, 40000, 50000, 60000, 70000],
            "purchased": [0, 0, 1, 1, 1]
        }
    )

    splitter = DataSplitter(
        data,
        "purchased"
    )

    X_train, X_test, y_train, y_test = splitter.split()

    assert len(X_train) == 4
    assert len(X_test) == 1

    assert "purchased" not in X_train.columns
    assert "purchased" not in X_test.columns
    