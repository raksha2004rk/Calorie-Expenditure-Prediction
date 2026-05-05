import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

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

            # Identify columns
            numerical_columns = X_train.select_dtypes(exclude="object").columns
            categorical_columns = X_train.select_dtypes(include="object").columns

            logging.info(f"Numerical cols: {numerical_columns}")
            logging.info(f"Categorical cols: {categorical_columns}")

            # Pipelines
            num_pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("onehot", OneHotEncoder(handle_unknown="ignore"))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num", num_pipeline, numerical_columns),
                    ("cat", cat_pipeline, categorical_columns)
                ]
            )

            # Fit & transform
            X_train_processed = preprocessor.fit_transform(X_train)
            X_test_processed = preprocessor.transform(X_test)

            # Save preprocessor
            save_object("artifacts/preprocessor.pkl", preprocessor)

            logging.info("Data transformation completed")

            return X_train_processed, X_test_processed, y_train, y_test

        except Exception as e:
            logging.error("Error in data transformation")
            raise CustomException(e, sys)