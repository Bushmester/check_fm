from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, login_required, logout_user

from accounts.services import find_by_username_and_password, create_user
from accounts.forms import LoginForm, SignupForm

accounts_blueprint = Blueprint('accounts', __name__, template_folder='templates')


@accounts_blueprint.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                create_user(form.email.data, form.username.data, form.password.data)
            except Exception as e:
                flash(str(e) or 'Unknown error', 'error')
                return redirect(url_for('accounts.signup'))
            else:
                return redirect(url_for('accounts.login'))

    return render_template('accounts/signup.html', form=form)


@accounts_blueprint.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user = find_by_username_and_password(form.username.data, form.password.data)
            except Exception as e:
                flash(str(e) or 'Unknown error')
                return redirect(url_for('accounts.login'))
            else:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('accounts.dashboard'))
    return render_template('accounts/login.html', form=form)


@accounts_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))


@accounts_blueprint.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template('accounts/dashboard.html')