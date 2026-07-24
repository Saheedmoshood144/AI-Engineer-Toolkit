import json

from main import main


def test_main_cli(tmp_path, monkeypatch):
    """
    Test the CLI execution of the pipeline.
    """

    # Create temporary CSV file
    csv_file = tmp_path / "employees.csv"

    csv_file.write_text(
        "name,age\nJohn,25\nMary,\n",
        encoding="utf-8"
    )

    # Create temporary config file
    config_data = {
        "dataset_path": str(csv_file),
        "log_level": "INFO"
    }

    config_file = tmp_path / "config.json"

    with config_file.open("w", encoding="utf-8") as file:
        json.dump(config_data, file)

    # Simulate command line arguments
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--config",
            str(config_file)
        ]
    )

    # Run CLI
    result = main()

    # Verify pipeline output
    assert result is not None
    assert len(result) == 1