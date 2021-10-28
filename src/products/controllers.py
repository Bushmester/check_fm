from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import login_required

from products.forms import ProductForm
from products.services import create_product_for_user

products_blueprint = Blueprint('products', __name__, template_folder='templates')


@products_blueprint.route('/create_product/user', methods=('GET', 'POST'))
@login_required
def create_product_for_user_page():
    form = ProductForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                create_product_for_user(form.name.data, form.price.data, form.category.data, form.description.data)
            except Exception as e:
                flash(str(e) or 'Unknown error', 'error')
            else:
                return redirect(url_for('accounts.dashboard'))
            return render_template('products/products_form.html', form=form)
    return render_template('products/products_form.html', form=form)
