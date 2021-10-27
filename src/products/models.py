from database import db
# noinspection PyUnresolvedReferences
# from accounts.models import UserProduct, GroupProduct


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


class ProductCategory(db.Model):
    __tablename__ = "product_category"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    products = db.relationship("Product", back_populates="products_categorys")
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    categorys = db.relationship("Category", back_populates="products_categorys")
