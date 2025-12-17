import sys

from bank_classification_model.config.core import config

sys.path.append(
    "/Users/khvandima/Documents/Programming/KS_AI_JLR_18/ml_practice/Bank_retirement"
)


def test_features_exist(sample_input_data):
    # Given
    expected_features = config.model_config.features

    # When
    actual_columns = sample_input_data.columns

    # Then
    for feature in expected_features:
        assert feature in actual_columns
