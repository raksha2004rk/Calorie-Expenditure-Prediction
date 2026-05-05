import sys
from src.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = self.get_error_details(error_message, error_detail)

    def get_error_details(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename

        return f"Error in {file_name}, line {exc_tb.tb_lineno}: {error_message}"

    def __str__(self):
        return self.error_message