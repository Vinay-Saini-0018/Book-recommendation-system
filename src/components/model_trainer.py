import numpy as np
import sys
import pickle
import os
from src.exception import CustomException
from sklearn.metrics.pairwise import cosine_similarity
from src.components.feature_engineering import feature_engineering
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import data_transformation


class recommendation_model:
        
        def __init__(self,pivot_table,books_data):
             self.pvt_table = pivot_table
             self.books = books_data
             self.similarity_score = cosine_similarity(pivot_table)


        def recommendall(self,book_name):
            try:
                
                if book_name not in self.pivot_table.index:
                    raise ValueError("Book not found in pivot table")

                #fetching index
                index = np.where(self.pivot_table.index==book_name)[0][0]
                similar_books = sorted(list(enumerate(self.similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]

                data = []
                for i in similar_books:
                    item = []
                    temp_dt = self.books[self.books['Book-Title']==self.pivot_table.index[i[0]]]
                    item.extend(list(temp_dt.drop_duplicates('Book-Title')['Book-Title'].values))
                    item.extend(list(temp_dt.drop_duplicates('Book-Title')['Book-Author'].values))
                    item.extend(list(temp_dt.drop_duplicates('Book-Title')['Image-URL-M'].values))

                    data.append(item)
                return data
        
            except Exception as e:
                raise CustomException(e,sys)


if __name__ == "__main__":
     books,ratings_data,users_data = DataIngestion().load_data()

     trans = data_transformation()
     books_data = trans.trans_books_data(books)

     pivot_table = feature_engineering().computation_for_rec_system(books_data,ratings_data,users_data)
     

     model = recommendation_model(pivot_table, books_data)
     
     # Save the model
     os.makedirs('artifacts', exist_ok=True)
     with open('artifacts/model.pkl', 'wb') as f:
         pickle.dump(model, f)
     
     print("Model saved successfully!")

