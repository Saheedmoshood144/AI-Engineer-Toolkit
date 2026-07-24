import pandas as pd

from src.file_manager import read_csv, write_csv


def test_write_and_read_csv(tmp_path):
    # Create sample data
    data = pd.DataFrame({
        "name": ["Saheed", "AI Engineer"],
        "score": [95, 100]
    })

    # Temporary file location
    file_path = tmp_path / "test.csv"

    # Write file
    result = write_csv(data, file_path)

    assert result is True

    # Read file
    loaded_data = read_csv(file_path)

    assert loaded_data is not None
    assert loaded_data.equals(data)
