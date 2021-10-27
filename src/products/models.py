from database import db
# # noinspection PyUnresolvedReferences
# from accounts.models import UserProduct, GroupProduct


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric, nullable=False, default=0)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    users_products = db.relationship("UserProduct", back_populates="products")
    groups_products = db.relationship("GroupProduct", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name}>"
