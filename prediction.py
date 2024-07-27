import joblib

model = joblib.load("model/gbcmodel.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Enrolled or Droput)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    if final_result == 1:
        return "Enrolled"
    else:
        return "Dropout"
