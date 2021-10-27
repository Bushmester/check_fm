from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators


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
            validators.Length(min=6, max=64)
        ]
    )
    remember = BooleanField("remember")


class SignupForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6)
        ]
    )
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
            validators.Length(min=6, max=64),
            validators.EqualTo(fieldname='confirm_password')
        ]
    )
    confirm_password = PasswordField(
        "confirm_password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=6, max=64),
        ]
    )
