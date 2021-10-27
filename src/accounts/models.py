from flask_login import UserMixin

from database import db
# # noinspection PyUnresolvedReferences
# from products.models import Product

UserGroup = db.Table(
    'user_group',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(128), unique=True)
    hashed_password = db.Column(db.String(1024), nullable=False)
    users_products = db.relationship("UserProduct", back_populates="users")
    groups = db.relationship('Group', secondary=UserGroup, backref='User')

    def __repr__(self):
        return f"<User {self.name}, id {self.id}>"


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    users = db.relationship('User', secondary=UserGroup, backref='Group')
    groups_products = db.relationship("GroupProduct", back_populates="groups")

    def __repr__(self):
        return f"<Group {self.name}>"


class UserProduct(db.Model):
    __tablename__ = "user_product"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship("User", back_populates="users_products")
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="users_products")


class GroupProduct(db.Model):
    __tablename__ = "group_product"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    groups = db.relationship("Group", back_populates="groups_products")
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="groups_products")
