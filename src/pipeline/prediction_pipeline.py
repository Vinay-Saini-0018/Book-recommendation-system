import sys
import pickle
from src.exception import CustomException
from src.logger import logging


class predict_pipeline:
    def __init__(self,model_path = "artifacts/model.pkl"):
        try:
            with open(model_path,"rb") as file:
                self.model = pickle.load(file)
        except Exception as e:
            raise CustomException(e,sys)
        
    def prediction(self,book_name):
        try:
            logging.info("prediction started")
            if book_name not in self.model.pivot_table.index:
                return{
                    "status":"error",
                    "message": "book not found in trained data"
                }
            logging.info("prediction completed")
            return self.model.recommendall(book_name)
            

        except Exception as e:
            logging.info("error occured in prediction pipeline")
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    model = predict_pipeline()
    book = input("Enter the book name :")
    print(f"similar books are: \n {model.prediction(book)}")
        