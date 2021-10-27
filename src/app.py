import os

from flask import Flask

from accounts.controllers import accounts_blueprint
from accounts.login_manager import login_manager
# noinspection PyUnresolvedReferences
from accounts.models import UserGroup, User, Product, Group, UserProduct, GroupProduct, Category, ProductCategory
from database import db, migrate
from local_configs import Configuration


app = Flask(__name__)

if not os.getenv('IS_PRODUCTION', None):
    app.config.from_object(Configuration)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

app.register_blueprint(accounts_blueprint, url_prefix='/accounts')

if __name__ == '__main__':
    app.run(debug=True)
