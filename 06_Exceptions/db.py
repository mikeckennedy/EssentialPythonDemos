import random

class Repository:

    def __init__(self):
        self.fake_data = [
            User(1, "Jeff"),
            User(2, "Bill"),
            User(3, "Ted"),
            User(4, "Zoe"),
        ]

    def find_user(self, id):

        if random.randint(0, 2) == 1:
            raise SQLError("Database not available!!!")

        for u in self.fake_data:
            if u.id == id:
                return u

        raise UserNotFoundError(id, "Sorry, user not found")

    def clean_up(self):
        print("Cleaning repository, bye now!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clean_up()

    def __enter__(self):
        return self



class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class UserNotFoundError(Exception):

    def __init__(self, user_id, msg):
        super().__init__(msg)
        self.user_id = user_id

class SQLError(Exception):
    pass



















