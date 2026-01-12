import sys
import os
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import data_transformation
from dataclasses import dataclass

# ------- Getting Top 50 books -------------
@dataclass
class config:
    top_n_books : int = 50
    top_books_path:str = "data/transformed/top_books.csv"

class feature_engineering:
    def __init__(self):
        self.config = config()

    def compute_top_books(self,books,ratings):
        try:
            books_with_ratings = books.merge(ratings,on="ISBN")
            books_with_nor = books_with_ratings.groupby('Book-Title').count()['Book-Rating'].reset_index()
            books_with_avgr = books_with_ratings.groupby('Book-Title')['Book-Rating'].mean().reset_index()
            popular_books = books_with_nor.merge(books_with_avgr,on=['Book-Title'])
            popular_books.rename(columns={'Book-Rating_x':'no. of ratings','Book-Rating_y':'avg. rating'},inplace=True)
            popular_bwgr = popular_books[popular_books['no. of ratings']>=250].sort_values('avg. rating',ascending=False).head(50)
            final_cdf = popular_bwgr.merge(books,on='Book-Title').drop_duplicates('Book-Title')
            final_cdf['avg. rating'] = final_cdf['avg. rating'].round(2)
            final_df = final_cdf[['Book-Title','no. of ratings','avg. rating','Book-Author','Image-URL-M']]

            #saving the file
            file_path = config().top_books_path
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            final_df.to_csv(file_path,index=False)

            print("csv file of top 50 books is saved")


        except Exception as e:
            raise CustomException(e,sys)
        
    def computation_for_rec_system(self,books,ratings,users):
        try:
            
            books_with_ratings = books.merge(ratings,on="ISBN")
            x = books_with_ratings.groupby('User-ID').count()['Book-Title']>=200
            padhe_likhe_users = x[x].index
            filtered_users = books_with_ratings[books_with_ratings['User-ID'].isin(padhe_likhe_users)]

            y = filtered_users.groupby('Book-Title').count()['Book-Rating']>=50
            famous_books = y[y].index
            filtered_books = filtered_users[filtered_users['Book-Title'].isin(famous_books)]
            pivot_table = filtered_books.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')
            pivot_table.fillna(0,inplace=True)

            return pivot_table


        except Exception as e:
            raise CustomException(e,sys)
        

# Temporary test block to check feature_engineering pipeline
'''if __name__ == "__main__":
    # Load and transform data
    books, ratings_data, users_data = DataIngestion().load_data()
    trans = data_transformation()
    books_data = trans.trans_books_data(books)
    
    fe = feature_engineering()
    fe.compute_top_books(books_data, ratings_data)
    print(fe.computation_for_rec_system(books_data, ratings_data, users_data))'''