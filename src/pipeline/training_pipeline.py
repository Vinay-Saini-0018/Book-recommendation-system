import os
import pickle
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import datavalidation
from src.components.data_transformation import data_transformation
from src.components.feature_engineering import feature_engineering
from src.components.model_trainer import recommendation_model


# 1. loading data
data = DataIngestion()
books,ratings,users = data.load_data()
logging.info("data loaded successfullly in training pipeline")

# 2. validate data
validate = datavalidation()
duplicates = validate.validate_data(books,ratings,users)
print(duplicates)

# 3. transforming data
trans = data_transformation()
books_transformed = trans.trans_books_data(books)

# 4. feature engineering
fe = feature_engineering()
fe.compute_top_books(books_transformed,ratings)

pivot_table = fe.computation_for_rec_system(books_transformed,ratings,users)

# 5. training model 
model = recommendation_model(pivot_table,books_transformed)
logging.info("model training completed")

# 6. export model
os.makedirs("artifacts", exist_ok = True)
with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(model,f)
logging.info("model exported successfully")

logging.info("Training pipeline completed successfully.")



