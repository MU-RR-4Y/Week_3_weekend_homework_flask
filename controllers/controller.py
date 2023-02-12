from flask import render_template, redirect, request
import datetime

from app import app
from models.book import Book
from models.library_books import *

@app.route('/')
def index():
    return render_template('index.html', title ='Home', books = book_list)

@app.route('/book/<index>')
def individual_book(index):
    book_selected = book_list[int(index)]
    return render_template('book.html', title = book_selected.name, book = book_selected)

@app.route('/', methods =['POST'])
def add_new_book():
    name = request.form['name']
    author = request.form['author']
    genre = request.form['genre']
    date_list = request.form['published_date'].split('-')
    date = datetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2]))

    book_added = Book(name, author, genre, date)
    add_book(book_added)

    return redirect('/')
   


