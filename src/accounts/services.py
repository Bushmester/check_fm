from accounts.database import users_lst

from hashlib import sha256


class UserNotFoundError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


def find_by_username_and_password(username, hashed_password):
    for user in users_lst:
        if user.username == username:
            if user.hashed_password == hashed_password:
                return user
            else:
                raise IncorrectPasswordError()
    raise UserNotFoundError()


def find_by_id(user_id):
    for user in users_lst:
        if user.id == user_id:
            return user


def password_hash(password):
    return sha256(password.encode("utf-8")).hexdigest()
