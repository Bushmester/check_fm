from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, logout_user

from accounts.services import find_by_username_and_password, password_hash, IncorrectPasswordError, UserNotFoundError


accounts_blueprint = Blueprint(
    'accounts', __name__, template_folder='templates')


@accounts_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        try:
            user = find_by_username_and_password(
                username, password_hash(password))
        except IncorrectPasswordError:
            flash('Incorrect password.')
        except UserNotFoundError:
            flash('Incorrect username.')
        except Exception:
            flash('Unknown error.')
        else:
            login_user(user, remember=remember)
        return render_template('accounts/login.html') #TODO: изменить редирект
    return render_template('accounts/login.html')


@accounts_blueprint.route('/logout', methods=('GET',))
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))
