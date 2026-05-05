from sklearn.ensemble import RandomForestRegressor
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
import sys

class ModelTrainer:
    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        try:
            logging.info("Model training started")

            model = RandomForestRegressor(n_estimators=100, max_depth=10)
            model.fit(X_train, y_train)

            save_object("artifacts/model.pkl", model)

            logging.info("Model training completed")

        except Exception as e:
            logging.error("Error in model training")
            raise CustomException(e, sys)