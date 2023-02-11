from flask import render_template, redirect, request
import datetime

from app import app
from models.book import Book
from models.library_books import *

@app.route('/')
def index():
    return render_template('index.html', title ='Home', books = book_list)

