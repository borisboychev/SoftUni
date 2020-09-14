from library.project.library import Library

class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library: Library):
        pass

    def return_book(self, author, book_name, library: Library):
        pass

    def info(self):
        pass
