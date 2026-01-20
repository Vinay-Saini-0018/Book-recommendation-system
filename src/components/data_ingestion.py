import pandas as pd
from src.exception import CustomException
import sys
from dataclasses import dataclass
from src.logger import logging

@dataclass
class DataIngestionconfig:
    books_path:str = "data/raw/Books.csv"
    ratings_path:str = "data/raw/Ratings.csv"
    Users_path:str = "data/raw/Users.csv"

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    # method 1 
    """
    def load_books_data(self):
        books_path = self.ingestion_config.books_path
        return pd.read_csv(books_path)
    
    def load_ratings_data(self):
        ratings_path = self.ingestion_config.ratings_path
        return pd.read_csv(ratings_path)

    def load_user_data(self):
        users_path = self.ingestion_config.Users_path
        return pd.read_csv(users_path)
    """   
   
    def load_data(self):
        try:
            logging.info("Data ingestion started")
            books = pd.read_csv(self.ingestion_config.books_path)
            ratings = pd.read_csv(self.ingestion_config.ratings_path)
            users = pd.read_csv(self.ingestion_config.Users_path)
            return books,ratings,users
            
            loggine.info("Data ingected Successfully.")
        except Exception as e:
            logging.error("Error occoured while ingecting data")
            raise CustomException(e,sys)
        


# Temporary test block to check data_ingestion pipeline
"""if __name__ == "__main__":
    data = DataIngestion()
    print(data.load_data())"""