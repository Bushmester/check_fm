from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            validators.DataRequired(),
            validators.Length(min=4, max=32)
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=8, max=64)
        ]
    )
    remember = BooleanField("remember")
