import psycopg2
import os
import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed output
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("database_operations.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)
# Function to establish connection to PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        logging.info("Database connection established successfully.")
        return conn
    except Exception as e:
        logging.error("Error connecting to the database: %s", e)
        raise
# Function to insert DataFrame into PostgreSQL
def insert_dataframe_to_db(df, table_name='telegram_data'):
    try:
        # Get a connection
        conn = get_db_connection()
        cur = conn.cursor()

        # Define SQL query to insert data
        insert_query = f"""
            INSERT INTO {table_name} (message_id, date, sender, channel,  text)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Loop through DataFrame and insert each row
        for _, row in df.iterrows():
            cur.execute(insert_query, (
                row['id'],
                row['date'],
                row['sender'],
                row['channel'],
                row['text']
            ))

        # Commit the transaction and close the connection
        conn.commit()
        logging.info("Data successfully inserted into the PostgreSQL database.")
    except Exception as e:
        logging.error("Error inserting data into the database: %s", e)
    finally:
        cur.close()
        conn.close()
        logging.info("Database connection closed.")