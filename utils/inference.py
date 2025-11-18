import pandas as pd
from .FactorsData import FactorsData

def predict_new(data: FactorsData, preprocessor, label_encoder, model):

    """
    data          : instance of FactorsData
    preprocessor  : fitted preprocessor (MinMaxScaler for X)
    model         : trained model
    label_encoder : fitted LabelEncoder for decoding target
    """

    # to df
    df = pd.DataFrame([data.model_dump()])

    # transformers
    X_processed = preprocessor.transform(df)

    # Predict
    y_pred_encoded = model.predict(X_processed)

    # Encoder
    y_pred = label_encoder.inverse_transform(y_pred_encoded)

    return {'Recommended crop' : y_pred[0]}

