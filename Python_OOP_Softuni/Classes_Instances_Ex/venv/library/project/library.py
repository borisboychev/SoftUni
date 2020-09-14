from library.project.user import User
from typing import List

class Library:

    def __init__(self):
        #stores user objects
        self.user_records: List[User] = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        if user_id not in [x.user_id for x in self.user_records]:
            return f"There is no such user with id = {user_id}"
        user = [x for x in self.user_records if x.user_id == user_id][0]
        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"
        user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"