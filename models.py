class Book:
    def __init__(self, author, title, rating, read_date):
        self.author = author
        self.title = title
        self.rating = rating
        self.read_date = read_date

    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date
        }