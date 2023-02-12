class Book:
    def __init__(self, name, author, genre, published_date):
        self.name = name
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.status = False
        self.reserved = False
     
    def change_status(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True

    def reserved_status(self):
        if self.reserved == True:
            self.reserved = False
        else:
            self.reserved = True
