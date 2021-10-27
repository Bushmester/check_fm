from database import db

UserGroup = db.Table(
    'user_group',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True)
    hashed_password = db.Column(db.String(1024), nullable=False)
    users_products = db.relationship("UserProduct", back_populates="users")
    groups = db.relationship('Group', secondary=UserGroup, backref='users')

    def __repr__(self):
        return f"<User {self.name}>"


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric, nullable=False, default=0)
    description = db.Column(db.String(255), nullable=True)
    users_products = db.relationship("UserProduct", back_populates="products")
    groups_products = db.relationship("GroupProduct", back_populates="products")
    products_categorys = db.relationship("ProductCategory", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products_categorys = db.relationship("ProductCategory", back_populates="categorys")


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


class ProductCategory(db.Model):
    __tablename__ = "product_category"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="products_groups")
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", back_populates="products_categorys")
