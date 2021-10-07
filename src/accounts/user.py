from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id: int, username: str, hashed_password: str) -> None:
        self.id = user_id
        self.username = username
        self.hashed_password = hashed_password
