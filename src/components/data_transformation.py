import pandas as pd
import sys
import os
import pickle
from src.logger import logging
from src.exception import CustomException

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class DataTransformation:
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data transformation started")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            target = "Calories"

            X_train = train_df.drop(columns=[target])
            y_train = train_df[target]

            X_test = test_df.drop(columns=[target])
            y_test = test_df[target]

            # ✅ FIXED columns (must match Flask input)
            numerical_columns = ["Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
            categorical_columns = ["Sex"]

            num_pipeline = Pipeline([
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline([
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ])

            preprocessor = ColumnTransformer([
                ("num", num_pipeline, numerical_columns),
                ("cat", cat_pipeline, categorical_columns)
            ])

            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)

            os.makedirs("artifacts", exist_ok=True)

            with open("artifacts/preprocessor.pkl", "wb") as f:
                pickle.dump(preprocessor, f)

            logging.info("Preprocessor saved successfully")

            return X_train, X_test, y_train, y_test

        except Exception as e:
            logging.error("Error in data transformation")
            raise CustomException(e, sys)