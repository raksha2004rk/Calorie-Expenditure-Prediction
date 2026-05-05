import pandas as pd
from src.utils import load_object
from src.logger import logging

class PredictPipeline:

    def __init__(self):
        try:
            logging.info("Loading model and preprocessor")

            self.model = load_object("artifacts/model.pkl")
            self.preprocessor = load_object("artifacts/preprocessor.pkl")

        except Exception as e:
            logging.error(f"Error loading artifacts: {e}")
            raise e

    def predict(self, data):
        try:
            logging.info(f"Input data: {data}")

            df = pd.DataFrame([data])
            transformed = self.preprocessor.transform(df)

            result = self.model.predict(transformed)

            logging.info(f"Prediction: {result}")

            return result

        except Exception as e:
            logging.error(f"Prediction error: {e}")
            raise e


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