import unittest
import datetime

from models.book import Book



class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1=Book('The Godfather', 'Mario Puzo','Crime',datetime.date(1969,3,10))
        self.book_2=Book('Nineteen Eighty-Four', 'George Orwell', 'Science Fiction', datetime.date(1949,6,8))
        self.book_3=Book('The Eye of the World', 'Robert Jordan', 'Fantasy', datetime.date(1990,1,15))
        self.book_4=Book('A Game of Thrones', 'George R. R. Martin', 'Fantasy', datetime.date(1996,8,1))

        self.books = [self.book_1, self.book_2, self.book_3, self.book_4]

    def test_book_name(self):
        self.assertEqual('The Godfather', self.book_1.name)

    def test_book_author(self):
        self.assertEqual('George Orwell', self.book_2.author)

    def test_book_genre(self):
        self.assertEqual('Fantasy',self.book_3.genre)

    def test_book_published_date(self):
        date = self.book_4.published_date
        self.assertEqual('01-08-1996', date.strftime('%d-%m-%Y'))

    def test_book_checked_out(self):
        book_5 =Book("Harry Potter and the Philospher's Stone",'J.K. Rowling','Fantasy',datetime.date(1997,6,26))
        self.assertEqual(False,book_5.status)
    
    
    def test_book_change_status(self):
        book_5 =Book("Harry Potter and the Philospher's Stone",'J.K. Rowling','Fantasy',datetime.date(1997,6,26))
        book_5.status = True
        self.book_1.change_status()
        book_5.change_status()
        self.assertEqual(True,self.book_1.status)
        self.assertEqual(False,book_5.status)


