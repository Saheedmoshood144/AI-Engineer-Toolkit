from sklearn.linear_model import LogisticRegression

from src.model_persistence import ModelPersistence


def test_model_save_and_load(tmp_path):

    model = LogisticRegression()

    file_path = tmp_path / "model.pkl"

    persistence = ModelPersistence()

    saved = persistence.save(
        model,
        str(file_path)
    )

    assert saved is True

    loaded_model = persistence.load(
        str(file_path)
    )

    assert loaded_model is not None