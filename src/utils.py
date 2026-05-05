import os
import pickle
from src.logger import logging

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        logging.info(f"Saving object to {file_path}")

        with open(file_path, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise e


def load_object(file_path):
    try:
        logging.info(f"Loading object from {file_path}")

        with open(file_path, "rb") as f:
            return pickle.load(f)

    except Exception as e:
        logging.error(f"Error loading object: {e}")
        raise e