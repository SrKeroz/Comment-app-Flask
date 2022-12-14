from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class UserLogin(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Log in")

class SignupForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(),
    Length(min=8, max=64, message='Name length must be between %(min)d and %(max)dcharacters')])
    submit = SubmitField("Signup")

class PublicPost(FlaskForm):
    comment = TextAreaField("comment", validators=[DataRequired(),
    Length(min=8, max=140, message='Name length must be between %(min)d and %(max)dcharacters')])
    submit = SubmitField("Post")

class UpdatePost(FlaskForm):
    comment_update = TextAreaField("comment", validators=[DataRequired(),
    Length(min=8, max=140, message='Name length must be between %(min)d and %(max)dcharacters')])
    submit = SubmitField("Post")
    