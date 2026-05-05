import os
from joblib import dump, load
from src.logger import logging
from src.exception import CustomException
import sys

def save_object(file_path, obj):
    try:
        logging.info("Saving object started")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        dump(obj, file_path)

        logging.info("Object saved successfully")

    except Exception as e:
        logging.error("Error occurred while saving object")
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        logging.info("Loading object started")

        obj = load(file_path)

        logging.info("Object loaded successfully")
        return obj

    except Exception as e:
        logging.error("Error occurred while loading object")
        raise CustomException(e, sys)