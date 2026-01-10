import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from dataclasses import dataclass

@dataclass
class datavalidationconfig:
    required_books_columns = ['ISBN','Book-Title','Book-Author',]
    required_ratings_columns = ["User-ID", "ISBN", "Book-Rating"]
    required_users_columns = ["User-ID","Age"]

class datavalidation:
    def __init__(self):
        self.validation_config = datavalidationconfig()

    def validate_data(self,books_df,ratings_df,users_df):
        try:
            # checking for empty dataframe
            if books_df.empty or ratings_df.empty or users_df.empty:
                raise ValueError("your data is empty")
            
            # checking for missing columns
            # this gives columns which is in required but not in actual
            missing_in_books = set(self.validation_config.required_books_columns) - set(books_df.columns)
            missing_in_ratings = set(self.validation_config.required_ratings_columns) - set(ratings_df.columns)
            missing_in_users = set(self.validation_config.required_users_columns) - set(users_df.columns)

            if missing_in_books:
                raise TypeError(f"Missing required columns in books dataset {missing_in_books}")
            if missing_in_ratings:
                raise TypeError(f"Missing required columns in ratings dataset {missing_in_ratings}")
            if missing_in_users:
                raise TypeError(f"Missing required columns in users dataset {missing_in_users}")
            
            # checking for duplicates
            duplicates_in_books = books_df.duplicated().sum()
            duplicates_in_ratings = ratings_df.duplicated().sum()
            duplicates_in_users = users_df.duplicated().sum()

            return {
                'status': 'success',
                'b_duplicates':int(duplicates_in_books),
                'r_duplicates':int(duplicates_in_ratings),
                'u_duplicates':int(duplicates_in_users)
            }
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    books, ratings, users = data_ingestion.load_data()
    validation = datavalidation()
    tht = validation.validate_data(books, ratings, users)
    print(tht)