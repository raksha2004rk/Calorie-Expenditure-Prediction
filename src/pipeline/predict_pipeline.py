import pandas as pd
from src.logger import logging
from src.utils import load_object

class PredictPipeline:

    def __init__(self):
        logging.info("Loading model and preprocessor")
        self.model = load_object("artifacts/model.pkl")
        self.preprocessor = load_object("artifacts/preprocessor.pkl")

    def predict(self, data):
        logging.info("Starting prediction")

        df = pd.DataFrame([data])
        logging.info(f"Input data: {df}")

        data_transformed = self.preprocessor.transform(df)

        prediction = self.model.predict(data_transformed)

        logging.info(f"Prediction result: {prediction}")

        return prediction


class CustomData:

    def __init__(self, age, sex, height, weight, duration, heart_rate):
        self.data = {
            "Age": age,
            "Sex": sex,
            "Height": height,
            "Weight": weight,
            "Duration": duration,
            "Heart_Rate": heart_rate
        }

    def get_data_as_dict(self):
        return self.data