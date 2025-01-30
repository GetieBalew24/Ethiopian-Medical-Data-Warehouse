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
    def remove_duplicates(self):
        """Removes duplicate messages based on 'message_id'."""
        before_removal = len(self.df)
        self.df = self.df.drop_duplicates(subset='message_id', keep='first')
        after_removal = len(self.df)
        logging.info(f"Removed {before_removal - after_removal} duplicate rows.")
        
    def handle_missing_values(self):
        """Handles missing values by filling or dropping them."""
        before_removal = len(self.df)
        self.df = self.df.dropna(subset=['message_id', 'text', 'sender', 'channel', 'date'])
        after_removal = len(self.df)
        logging.info(f"Removed {before_removal - after_removal} rows due to missing values.")

    def standazrdize_formats(self):
        """Standardizes the formats, for example, converting date to standard format."""
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')  # Ensures date is in datetime format
        self.df['text'] = self.df['text'].str.strip()  # Removes leading/trailing spaces
        logging.info("Standardized date formats and cleaned text fields.")