import pandas as pd
from src.utils import load_object

class PredictPipeline:

    def __init__(self):
        self.model = load_object("artifacts/model.pkl")
        self.preprocessor = load_object("artifacts/preprocessor.pkl")

    def predict(self, data):
        df = pd.DataFrame([data])
        data_transformed = self.preprocessor.transform(df)
        return self.model.predict(data_transformed)


class CustomData:

    def __init__(self, age, gender, height, weight, duration, heart_rate):
        self.data = {
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight,
            "Duration": duration,
            "Heart_Rate": heart_rate
        }

    def get_data_as_dict(self):
        return self.data