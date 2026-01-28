## 📚 Book Recommendation System

A smart book recommendation system that suggests books based on what other readers liked. Built using collaborative filtering and machine learning techniques.

##  Live Demo

🔗 **[Try it Live Here](https://book-recommendation-system-d6pr.onrender.com/)** 

## 📖 About The Project

This project helps book lovers discover new books they might enjoy. It analyzes reading patterns of thousands of users and recommends books similar to the ones you already like. Think of it as having a personal librarian who knows your taste!

### How It Works

The system uses **collaborative filtering** and **cosine similarity** to find books that are similar based on user ratings. When you select a book you like, it finds other books that were enjoyed by readers with similar tastes.


## 🛠️ Technologies Used

- **Python** - Core programming language
- **Flask** - Web framework for the application
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Scikit-learn** - Machine learning algorithms (Cosine Similarity)
- **HTML/CSS** - Frontend interface
- **Jupyter Notebook** - Data analysis and model development

## 📊 Dataset

The system uses three main datasets:
- **Books Data**: Contains book titles, authors, publishers, and other details
- **Users Data**: Information about users who rated the books
- **Ratings Data**: User ratings for different books

## 🚀 Getting Started

Follow these simple steps to run the project on your local machine:

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Vinay-Saini-0018/Book-recommendation-system.git
   cd Book-recommendation-system
```

2. **Install required packages**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python app.py
```

4. **Open in browser**
```
   Navigate to http://127.0.0.1:5000/ in your web browser
```

## 💡 How to Use

1. **Browse Popular Books**: Check out the homepage to see the most popular books
2. **Search for a Book**: Enter a book title you've enjoyed
3. **Get Recommendations**: The system will suggest 5 similar books you might like
4. **Discover New Reads**: Explore the recommendations and find your next favorite book!



## 🧠 How The Recommendation Works

### Step-by-Step Process:

1. **Data Loading**: Load books, users, and ratings data from CSV files

2. **Data Filtering**:
   - Keep only books with at least 250 ratings (ensures quality)
   - Select users who have rated more than 200 books (active users)
   - Focus on books with at least 50 ratings

3. **Create Pivot Table**:
   - Rows = Book names
   - Columns = User IDs
   - Values = Ratings
   - This converts our data into a format perfect for similarity calculations

4. **Calculate Similarity**:
   - Use cosine similarity to find how similar books are
   - Books liked by similar users get higher similarity scores

5. **Generate Recommendations**:
   - When you select a book, the system finds the 5 most similar books
   - These become your personalized recommendations!


## 👨‍💻 Author

**Vinay Saini**

- GitHub: [@Vinay-Saini-0018](https://github.com/Vinay-Saini-0018)

