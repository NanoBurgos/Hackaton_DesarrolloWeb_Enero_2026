from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

def get_user_by_id(user_id):
    if user_id == "1":
        return User("1", "admin", "admin")
    return None