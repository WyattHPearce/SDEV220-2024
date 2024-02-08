import json
import requests
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

# Creating a flask app
app = Flask(__name__)

# SQL database using flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Book class (schema)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f"id: {self.id}, book_name: {self.book_name}, " + \
            f"author: {self.author}, publisher: {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)

    return {'books': output}

@app.route('/books', methods=['POST'])
def create_book() -> str:
    book = Book()
    book.id = request.json['id'],
    book.book_name = request.json['book_name'],
    book.author = request.json['author'],
    book.publisher = request.json['publisher']
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }