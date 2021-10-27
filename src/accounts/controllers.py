from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from accounts.services import find_by_username_and_password
from accounts.forms import LoginForm

accounts_blueprint = Blueprint('accounts', __name__, template_folder='templates')


@accounts_blueprint.route('/', methods=('GET',))
def index():
    if current_user.is_authenticated:
        pass
    return redirect(url_for('accounts.login'))


@accounts_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        try:
            user = find_by_username_and_password(form.username.data, form.password.data)
        except Exception as e:
            flash(str(e) or 'Unknown error')
            return redirect(url_for('accounts.login'))
        else:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('accounts/login.html')) #TODO: изменить редирект
    return render_template('accounts/login.html')


@accounts_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))
