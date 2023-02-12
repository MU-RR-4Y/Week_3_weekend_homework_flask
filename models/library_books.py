from models.book import Book
import datetime

book_1=Book('The Godfather', 'Mario Puzo','Crime',datetime.date(1969,3,10))
book_2=Book('Nineteen Eighty-Four', 'George Orwell', 'Science Fiction', datetime.date(1949,6,8))
book_3=Book('The Eye of the World', 'Robert Jordan', 'Fantasy', datetime.date(1990,1,15))
book_4=Book('A Game of Thrones', 'George R. R. Martin', 'Fantasy', datetime.date(1996,8,1))

book_list = [book_1, book_2, book_3, book_4]

def add_book(book):
    book_list.append(book)

def remove_book(book_removed):
    book_removed = None
    for book in book_list:
        if book.name == book_removed:
            book_removed = book
            break
    book_list.remove(book)