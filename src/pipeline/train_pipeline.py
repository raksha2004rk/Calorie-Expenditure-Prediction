from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

if __name__ == "__main__":
    logging.info("Training pipeline started")

    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transform = DataTransformation()
    X_train, X_test, y_train, y_test = transform.initiate_data_transformation(
        train_path, test_path
    )

    trainer = ModelTrainer()
    trainer.initiate_model_trainer(X_train, X_test, y_train, y_test)

    logging.info("Training pipeline completed")