import os

from flask import Flask, redirect, url_for
from flask_login import current_user

from accounts.controllers import accounts_blueprint
from accounts.login_manager import login_manager
# noinspection PyUnresolvedReferences
from accounts.models import UserGroup, User, Group, UserProduct, GroupProduct
from products.controllers import products_blueprint
# noinspection PyUnresolvedReferences
from products.models import Product, Category, ProductCategory
from database import db, migrate
from local_configs import Configuration


app = Flask(__name__)

if not os.getenv('IS_PRODUCTION', None):
    app.config.from_object(Configuration)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

app.register_blueprint(accounts_blueprint, url_prefix='/accounts')
app.register_blueprint(products_blueprint, url_prefix='/products')


@app.route('/', methods=('GET',))
def index():
    if current_user.is_authenticated:
        return redirect(url_for('accounts.dashboard'))
    return redirect(url_for('accounts.login'))


if __name__ == '__main__':
    app.run(debug=True)
