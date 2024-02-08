"""
    Author:  Wyatt H. Pearce
    Date:
    Section: 16.8
    
    Instructions: 
        Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. 
        As in 16.6, select and print the ```title``` column from the book table in alphabetical order.

    Description:
        This program displays the title column in alphabetical order.
        The title column is part of the book table within 'books.db'. 
"""
# Imports for API
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a flask app
app = Flask(__name__)

# SQL database using flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Book class (schema)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    year = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"id: {self.id}, title: {self.title}, " + \
            f"author: {self.author}, year: {self.year}"

# Index
@app.route('/')
def index():
    return 'M04_assignment, 16.8!'

@app.route('/booktitles')
def get_titles() -> str:
    """ 
    Route that returns all book titles in order

    Returns:
        str: title_column_str
    """

    # Getting all within the book database, ordered by title
    titles = Book.query.order_by(Book.title).all()

    '''
        # My original method before remembering join() exists
        for title in titles:
            title_column_str = title_column_str + title.title + ", "
    '''

    # single string using list comprehension
    title_column_str = ', '.join(title.title for title in titles)

    return f'Titles: {title_column_str}'