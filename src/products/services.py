from decimal import Decimal

from flask_login import current_user

from flask_sqlalchemy import Pagination
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from accounts.services import find_user_by_id
from products.models import Product
from accounts.models import User, UserProduct
from database import db


class DatabaseError(Exception):
    pass


def get_user_product() -> Product:
    return Product.query \
        .join(UserProduct, Product.id == UserProduct.product_id) \
        .join(User, UserProduct.user_id == User.id) \
        .filter(User.id == current_user.id).order_by(Product.id.desc())


def get_paginated_product_user_list(page: int) -> Pagination:
    return get_user_product().paginate(page, 12)


def create_product_for_user(name: str, price: Decimal, category: str, description: str) -> None:
    try:
        product = Product(
            name=name,
            price=price,
            category=category,
            description=description
        )
        user_product = UserProduct(
            users=find_user_by_id(current_user.id),
            products=product
        )
        db.session.add(product)
        db.session.add(user_product)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise DatabaseError(f'Unknown error')
