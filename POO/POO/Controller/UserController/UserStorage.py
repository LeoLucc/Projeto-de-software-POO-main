# Controller/UserController/UserStorage.py
class UserStorage:
    def __init__(self):
        self._users = []

    def add(self, user):
        self._users.append(user)

    def remove(self, username, password):
        original_len = len(self._users)
        self._users = [u for u in self._users if not (u.username == username and u.password == password)]
        return len(self._users) < original_len

    def find_by_credentials(self, username, password):
        return next((u for u in self._users if u.username == username and u.password == password), None)

    def find_by_id(self, user_id):
        return next((u for u in self._users if u._id == user_id), None)

    def list_all(self):
        return self._users
