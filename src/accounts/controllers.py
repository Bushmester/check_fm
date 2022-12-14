from werkzeug.security import generate_password_hash

from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from accounts.services import find_by_username_and_password, create_user, edit_user, create_group
from accounts.forms import LoginForm, SignUpForm, EditUserInfoForm, CreateGroupForm
from products.services import get_paginated_product_user_list

from database import db

accounts_blueprint = Blueprint('accounts', __name__, template_folder='templates')


@accounts_blueprint.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignUpForm(request.form)

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
    raw_page = request.args.get('page', '1')
    page = int(raw_page) if raw_page.isdigit() else 1
    pagination = get_paginated_product_user_list(page)
    return render_template('accounts/dashboard.html', pagination=pagination)


@accounts_blueprint.route("/statistics", methods=["GET"])
@login_required
def statistics():
    with db.engine.connect() as conn:
        results = conn.execute(db.text('''
            SELECT
                category,
                SUM(price) sum
            FROM product
            LEFT JOIN user_product up on product.id = up.product_id
            LEFT JOIN "user" u on up.user_id = u.id
            WHERE u.id = (:i)
            GROUP BY category;
        '''), [{"i": current_user.id}])
    return render_template('accounts/statistics.html', results=results)


@accounts_blueprint.route('/profile', methods=('GET', 'POST'))
@login_required
def profile():
    form = EditUserInfoForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                current_email = current_user.email
                new_email = form.email.data if form.email.data else current_email
                new_name = form.username.data if form.username.data else current_user.name
                new_password = generate_password_hash(form.password.data) if form.password.data else None
                edit_user(current_email, new_email, new_name, new_password)
            except Exception as e:
                flash(str(e) or 'Unknown error', 'error')
                return redirect(url_for('accounts.profile'))
            else:
                return redirect(url_for('accounts.dashboard'))

    return render_template('accounts/profile.html', form=form, user=current_user)


@accounts_blueprint.route("/groups", methods=["GET"])
@login_required
def groups():
    return render_template('accounts/groups.html')


@accounts_blueprint.route("/create_group", methods=('GET', 'POST'))
@login_required
def create_group_page():
    form = CreateGroupForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                create_group(form.name.data, form.party.data.split())
            except Exception as e:
                flash(str(e) or 'Unknown error', 'error')
                return redirect(url_for('accounts.create_group'))
            else:
                return redirect(url_for('accounts.groups'))
    return render_template('accounts/create_group.html', form=form)
