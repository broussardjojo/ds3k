from typing import Tuple, List

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


def fit_scalers_and_encoders(df_in: pd.DataFrame,
                             categorical_features: List[str] = ['key', 'mode', 'time_signature'],
                             continuous_features: List[str] = ['duration_ms', 'danceability', 'energy', 'loudness',
                                                               'speechiness', 'acousticness',
                                                               'instrumentalness', 'liveness', 'valence',
                                                               'tempo']) -> dict:
    scalers_and_encoders = {}
    # Creating onehotencoders for categorical features
    for column in categorical_features:
        encoder = OneHotEncoder(sparse=False)
        encoder.fit(df_in[[column]])
        scalers_and_encoders[column] = encoder
    # Creating scalers for continuous features
    for column in continuous_features:
        scaler = MinMaxScaler()
        scaler.fit(df_in[[column]])
        scalers_and_encoders[column] = scaler
    return scalers_and_encoders


# transformers is a dictionary mapping of column names (as strings) to scalers or encoders.
def encode_dataframe_given_transformers(df_in: pd.DataFrame, transformers: dict) -> pd.DataFrame:
    # Encoding categorical variables and discarding their non-encoded versions
    for column in ['key', 'mode', 'time_signature']:
        df_in[transformers[column].get_feature_names_out()] = transformers[column].transform(df_in[[column]])
        df_in = df_in.drop(columns=column)

    # Normalizing continuous features
    for column in ['duration_ms', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo']:
        df_in[[column]] = transformers[column].transform(df_in[[column]])
    return df_in


def encode_training_data(df_in: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    training_scalers_and_encoders = fit_scalers_and_encoders(df_in)
    cleaned_training_dataset = encode_dataframe_given_transformers(df_in, training_scalers_and_encoders)
    cleaned_training_dataset = cleaned_training_dataset.set_index("uri")
    return cleaned_training_dataset, training_scalers_and_encoders
