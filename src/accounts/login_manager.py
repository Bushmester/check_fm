import base64

from flask_login import LoginManager

from accounts.models import User
from accounts.services import find_by_username_and_password, IncorrectPasswordError, NotFoundError


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(int(user_id))
    return None


@login_manager.request_loader
def load_basic_auth(request):
    basic_auth_val = request.headers.get('Authorization')
    if basic_auth_val is None:
        return None
    basic_auth_val = basic_auth_val.replace('Basic ', '', 1)
    try:
        username, password = str(base64.b64decode(basic_auth_val), 'utf-8').split(':')
        user = find_by_username_and_password(username, password)
    except (IncorrectPasswordError, NotFoundError):
        return None
    return user
