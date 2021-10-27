from werkzeug.security import check_password_hash

from accounts.models import User


class NotFoundError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


def find_by_username_and_password(username: str, password: str):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise NotFoundError('Incorrect username')
    if not check_password_hash(user.hashed_password, password):
        raise IncorrectPasswordError('Incorrect password')
    return user


def find_user_by_id(user_id: int):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        raise NotFoundError()
    return user
