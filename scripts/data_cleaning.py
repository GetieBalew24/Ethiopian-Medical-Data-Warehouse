import pandas as pd
import logging

# Set up logging for DataCleaner, logging to data_cleaner.log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data_cleaner.log"),  # Log to a separate file for DataCleaner
        logging.StreamHandler()  # Log to console
    ]
)

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        """
        Initializes the DataCleaner with a DataFrame to clean.
        
        :param df: The DataFrame containing the Telegram data.
        """
        self.df = df