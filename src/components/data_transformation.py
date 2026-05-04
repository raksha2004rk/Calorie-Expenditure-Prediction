import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from src.utils import save_object

class DataTransformation:

    def get_preprocessor(self):

        num_cols = ["Age", "Height", "Weight", "Duration", "Heart_Rate"]
        cat_cols = ["Gender"]

        num_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        cat_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ])

        preprocessor = ColumnTransformer([
            ("num", num_pipeline, num_cols),
            ("cat", cat_pipeline, cat_cols)
        ])

        return preprocessor

    def initiate_data_transformation(self, train_path, test_path):

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        target = "Calories"

        X_train = train_df.drop(columns=[target])
        y_train = train_df[target]

        X_test = test_df.drop(columns=[target])
        y_test = test_df[target]

        preprocessor = self.get_preprocessor()

        X_train = preprocessor.fit_transform(X_train)
        X_test = preprocessor.transform(X_test)

        save_object("artifacts/preprocessor.pkl", preprocessor)

        return X_train, X_test, y_train, y_test