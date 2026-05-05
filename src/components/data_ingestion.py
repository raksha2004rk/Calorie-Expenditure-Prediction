import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import sys

class DataIngestion:
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            df = pd.read_csv("data/train.csv")

            os.makedirs("artifacts", exist_ok=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv("artifacts/train.csv", index=False)
            test_set.to_csv("artifacts/test.csv", index=False)

            logging.info("Data ingestion completed")

            return (
                "artifacts/train.csv",
                "artifacts/test.csv"
            )

        except Exception as e:
            logging.error("Error in data ingestion")
            raise CustomException(e, sys)