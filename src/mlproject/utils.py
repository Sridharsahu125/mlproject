import os
import sys
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection details from environment variables
host = os.getenv('host', 'localhost')
user = os.getenv('user', 'root')
password = os.getenv('password', '')
db = os.getenv('db', 'mydatabase')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        # Construct the database URL
        db_url = f"mysql+pymysql://{user}:{password}@{host}/{db}"

        # Create an SQLAlchemy engine
        engine = create_engine(db_url)
        logging.info("Connection Established: %s", engine)

        # Execute the query and return the DataFrame
        df = pd.read_sql_query('SELECT * FROM students', engine)
        return df

    except Exception as e:
        logging.error("An error occurred while reading from the SQL database: %s", e)
        raise CustomException(e)

# Example usage
if __name__ == "__main__":
    try:
        data = read_sql_data()
        print(data.head())
    except CustomException as ce:
        logging.error("Data retrieval failed: %s", ce)
