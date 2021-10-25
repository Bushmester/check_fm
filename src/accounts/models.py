from database import db


User_Group = db.Table(
    'User_Group',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('Group.id'))
)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(1024), nullable=False)
    users_products = db.relationship("User_Product", back_populates="users")
    groups = db.relationship('Group', secondary=User_Group, backref='User')

    def __repr__(self):
        return f"<User {self.name}>"


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Decimal, nullable=False, default=0)
    category = db.Column(db.String(255), nullable=False),
    description = db.Column(db.String(255), nullable=True)
    users_products = db.relationship("User_Product", back_populates="products")
    groups_products = db.relationship("Group_Product", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    users = db.relationship('User', secondary=User_Group, backref='Group')
    groups_products = db.relationship("Group_Product", back_populates="groups")

    def __repr__(self):
        return f"<Group {self.name}>"


class User_Product(db.Model):
    __tablename__ = "user_product"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship("User", back_populates="users_products")
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="users_products")


class Group_Product(db.Model):
    __tablename__ = "group_product"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    groups = db.relationship("Group", back_populates="groups_products")
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="groups_products")
