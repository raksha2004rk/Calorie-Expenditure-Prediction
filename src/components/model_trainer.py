from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from src.utils import save_object

class ModelTrainer:

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):

        model = RandomForestRegressor(n_estimators=100, random_state=42)

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        score = r2_score(y_test, y_pred)
        print("R2 Score:", score)

        save_object("artifacts/model.pkl", model)

        return model