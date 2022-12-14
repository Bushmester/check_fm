from typing import Optional, List

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import SQLAlchemyError

from accounts.models import User, Group, UserGroup
from database import db


class NotFoundError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


def find_by_username_and_password(username: str, password: str):
    user = User.query.filter_by(name=username).first()
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


def create_user(email: str, name: str, password: str):
    new_user = User(email=email, name=name, hashed_password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()


def edit_user(current_email: str, email: str, name: str, hashed_password: Optional[str]):
    user = User.query.filter_by(email=current_email).first()
    user.email = email
    user.name = name
    db.session.commit()
    if hashed_password:
        db.session.commit()


def create_group(name: str, party: List[str]):
    try:
        group = Group(
            name=name
        )
        db.session.add(group)
        db.session.commit()

        for user in party:
            UserGroup.group_id = group,
            UserGroup.user_id = User.query.filter_by(email=user).first()
    except SQLAlchemyError as e:
        db.session.rollback()
