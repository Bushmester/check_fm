from typing import Union

from flask_sqlalchemy import Pagination
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from products.forms import ProductForm
from products.models import Product, Category, ProductCategory
from accounts.models import User, Group, UserProduct, GroupProduct
from database import db


class DatabaseError(Exception):
    pass


def get_paginated_product_list(page: int) -> Pagination:
    return Product.query.paginate(page, 5)


def create_product(form: ProductForm, source: Union[User, Group]):
    try:
        pass
    except:
        pass
