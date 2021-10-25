import os

from flask import Flask
from flask_login import LoginManager

from database import users_lst
from accounts.user import User

from accounts.controllers import accounts_blueprint
from accounts.services import find_by_username_and_password, password_hash, IncorrectPasswordError, UserNotFoundError
from local_configs import Configuration


app = Flask(__name__)


def main():
    app.register_blueprint(accounts_blueprint, url_prefix='/accounts')

    if not os.getenv('IS_PRODUCTION', None):
        app.config.from_object(Configuration)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        for user in users_lst:
            if user_id == user.get_id():
                return user

    app.run()


if __name__ == '__main__':
    main()
