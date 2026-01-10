import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from dataclasses import dataclass

@dataclass
class transformationconfig:
    
    ratings_path:str = "data/transformed/trans_ratings.csv"
    users_path:str = "data/transformed/trans_users.csv"

class data_transformation:
    def __init__(self):
        self.config = transformationconfig()

    # ----------- Books ------------ #
    def trans_books_data(self,books_df):
        try:
             # Drop image columns if they exist
            img_cols = ["Image-URL-S", "Image-URL-L"]
            books_df = books_df.drop(columns=img_cols, errors="ignore")   #if column not found it ignore error

            # Remove rows where Book-Author is missing
            books_df = books_df.dropna(subset=["Book-Author"])

            # Remove duplicate rows
            books_df = books_df.drop_duplicates()

            return books_df
        except Exception as e:
            raise CustomException(e,sys)
    
    # ---------- users ----------- #
            # not required


    # ----------- ratings ----------- #
            # not required

if __name__ == "__main__":
    books,_,_ = DataIngestion().load_data()
    trans = data_transformation()
    print(trans.trans_books_data(books))
            