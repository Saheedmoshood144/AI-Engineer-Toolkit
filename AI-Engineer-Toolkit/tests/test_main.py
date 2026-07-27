import json

from main import main


def test_main_cli(tmp_path, monkeypatch):
    """
    Test CLI execution of pipeline.
    """

    csv_file = tmp_path / "data.csv"

    csv_file.write_text(
        "age,salary,target\n"
        "20,30000,0\n"
        "25,40000,0\n"
        "30,50000,0\n"
        "35,60000,1\n"
        "40,70000,1\n"
        "45,80000,1\n",
        encoding="utf-8"
    )


    config_data = {
        "dataset_path": str(csv_file),
        "target_column": "target",
        "log_level": "INFO"
    }


    config_file = tmp_path / "config.json"


    with config_file.open(
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            config_data,
            file
        )


    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--config",
            str(config_file)
        ]
    )


    result = main()


    assert result is not None

    assert "accuracy" in result
    assert "precision" in result
    assert "recall" in result
    assert "f1_score" in result