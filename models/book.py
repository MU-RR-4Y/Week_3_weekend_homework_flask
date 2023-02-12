class Book:
    def __init__(self, name, author, genre, published_date):
        self.name = name
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.status = False
     
    def change_status(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True
