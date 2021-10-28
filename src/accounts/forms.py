from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(),
            Length(min=4, max=32)
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=6, max=64)
        ]
    )
    remember = BooleanField("remember")


class SignUpForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            DataRequired(),
            Email(),
            Length(min=6)
        ]
    )
    username = StringField(
        "username",
        validators=[
            DataRequired(),
            Length(min=4, max=32)
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=6, max=64),
            EqualTo(fieldname='confirm_password')
        ]
    )
    confirm_password = PasswordField(
        "confirm_password",
        validators=[
            DataRequired(),
            Length(min=6, max=64),
        ]
    )


class EditUserInfoForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            Optional(),
            Email(),
            Length(min=6)
        ]
    )
    username = StringField(
        "username",
        validators=[
            Optional(),
            Length(min=4, max=32)
        ]
    )
    password = PasswordField(
        "password",
        validators=[
            Optional(),
            Length(min=6, max=64),
            EqualTo(fieldname='confirm_password')
        ]
    )
    confirm_password = PasswordField(
        "confirm_password",
        validators=[
            Optional(),
            Length(min=6, max=64),
        ]
    )


class CreateGroupForm(FlaskForm):
    name = StringField(
        "name",
        validators=[
            DataRequired(),
            Length(min=4, max=32)
        ]
    )
    party = TextAreaField(
        "party",
        validators=[
            Optional()
        ]
    )
