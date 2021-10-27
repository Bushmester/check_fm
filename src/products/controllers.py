from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_user, login_required, logout_user

from products.forms import ProductForm

products_blueprint = Blueprint('products', __name__, template_folder='templates')


@products_blueprint.route('/create', methods=('GET', 'POST'))
def create_product_page():
    form = ProductForm()

    if form.validate_on_submit():
        try:
            pass
        except Exception as e:
            flash(str(e) or 'Unknown error', 'error')
        else:
            return redirect(url_for('accounts.dashboard'))

    return render_template('products/products_form.html', form=form)
