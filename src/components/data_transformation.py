import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.logger import logging


class data_transformation:
    # ----------- Books ------------ #
    def trans_books_data(self,books_df):
        try:
            logging.info("Transformation in books data is started")
             # Drop image columns if they exist
            img_cols = ["Image-URL-S", "Image-URL-L"]
            books_df = books_df.drop(columns=img_cols, errors="ignore")   #if column not found it ignore error

            # Remove rows where Book-Author is missing
            books_df = books_df.dropna(subset=["Book-Author"])

            # Remove duplicate rows
            books_df = books_df.drop_duplicates()

            return books_df
            logging.info("Transformation only in books data completed")
        except Exception as e:
            logging.error("Error occured")
            raise CustomException(e,sys)
    
    # ---------- users ----------- #
            # not required


    # ----------- ratings ----------- #
            # not required


# Temporary test block to check data_transformation pipeline
'''
if __name__ == "__main__":
    books,_,_ = DataIngestion().load_data()
    trans = data_transformation()
    print(trans.trans_books_data(books))'''
            