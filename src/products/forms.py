from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        "name",
        validators=[
            DataRequired(),
            Length(max=32)
        ]
    )
    price = DecimalField(
        "price",
        validators=[
            DataRequired()
        ]
    )
    category = StringField(
        "category",
        validators=[
            DataRequired(),
            Length(min=3, max=32)
        ]
    )
    description = StringField(
        "description",
        validators=[
            DataRequired(),
            Length(max=1024)
        ]
    )
