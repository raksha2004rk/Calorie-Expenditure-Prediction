import pandas as pd
import os

class DataIngestion:

    def __init__(self):
        self.train_path = "artifacts/train.csv"
        self.test_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):
        df = pd.read_csv("data/processed/cleaned_data.csv")

        os.makedirs("artifacts", exist_ok=True)

        from sklearn.model_selection import train_test_split

        train, test = train_test_split(df, test_size=0.2, random_state=42)

        train.to_csv(self.train_path, index=False)
        test.to_csv(self.test_path, index=False)

        return self.train_path, self.test_path