from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from src.logger import logging
import pickle
import os

class ModelTrainer:

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        try:
            logging.info("Starting model training")

            # ✅ Lighter model (small + fast)
            model = GradientBoostingRegressor(
                n_estimators=50,
                max_depth=3,
                random_state=42
            )

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)

            logging.info(f"Model R2 Score: {score}")

            os.makedirs("artifacts", exist_ok=True)

            # ✅ Save with pickle (safe)
            with open("artifacts/model.pkl", "wb") as f:
                pickle.dump(model, f)

            logging.info("Model saved successfully")

            return model

        except Exception as e:
            logging.error(f"Error in model training: {e}")
            raise e