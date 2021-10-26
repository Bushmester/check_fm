from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, login_required, logout_user

from accounts.services import find_by_username_and_password

accounts_blueprint = Blueprint('accounts', __name__, template_folder='templates')


@accounts_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember_me = len(request.form.getlist('remember_me')) > 0
        try:
            user = find_by_username_and_password(username, password)
        except Exception as e:
            flash(str(e) or 'Unknown error')
            return redirect(url_for('accounts.login'))
        else:
            login_user(user, remember=remember_me)
            return redirect(url_for('accounts/login.html')) #TODO: изменить редирект
    return render_template('accounts/login.html')


@accounts_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))
