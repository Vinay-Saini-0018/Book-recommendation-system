from flask import Flask,render_template,request
import pandas as pd
from src.pipeline.prediction_pipeline import predict_pipeline

top_books_df = pd.read_csv("data/transformed/top_books.csv")

app = Flask(__name__)

@app.route("/")
def dashboard():
    books_dict = top_books_df.to_dict(orient="records")
    return render_template("index.html",books=books_dict)

@app.route("/recommend",methods=["GET","POST"])
def recommend():
    result = []
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        if book_name:
            model = predict_pipeline()
            result = model.prediction(book_name)
    return render_template("recommend.html",result=result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)