import json

from src.config import load_config


def test_load_config(tmp_path):
    # Create a temporary config file
    config_data = {
        "dataset_path": "employees.csv",
        "log_level": "INFO"
    }

    config_file = tmp_path / "config.json"

    with config_file.open("w", encoding="utf-8") as file:
        json.dump(config_data, file)

    config = load_config(str(config_file))

    assert config is not None
    assert config["dataset_path"] == "employees.csv"
    assert config["log_level"] == "INFO"