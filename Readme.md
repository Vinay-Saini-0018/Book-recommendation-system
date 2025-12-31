-------Book Recommendation System --------
In this project, I built a book recommendation system using collaborative filtering and cosine similarity.

-----About notebook----

Step 1: Loading the data
First, I loaded the CSV files that contain information about books, users, and their ratings.

Step 2: Exploratory Data Analysis (EDA)
After loading the data, I performed some basic EDA 

Step 3: Selecting popular books
I select top 50 books based on the number of ratings
From these, I kept only those books that have more than 250 ratings
This step helps in improving the quality of recommendations.

Step 4: Filtering active users and books
I selected only those users who have rated more than 200 books
Then, I kept only those books that have at least 50 ratings

Step 5: Creating the pivot table
After filtering, I created a pivot table where:
-rows represent book names
-columns represent user IDs
-values represent ratings

Why pivot table?
Because cosine similarity works on vector data, not on raw tables.
pivot table data looks similar to vector form

Step 6: Applying cosine similarity
Using the pivot table, I calculated cosine similarity between books to find how similar they are based on user ratings.

Step 7: Recommendation function

Finally, I created a function that:
takes a book name as input, finds similar books using cosine similarity
returns the top 5 recommended books
