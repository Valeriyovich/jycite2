from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField(
        'password',
        validators=[InputRequired(),
                    Length(min=8, max=80, message='Password must be between 8 and 80 characters long.')])
    passwordConfirm = PasswordField('passwordConfirm', validators=[InputRequired(),
                                                                   EqualTo('password', message='Passwords must match')])
    country = StringField('country', validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


class ContactForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=0, max=50)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    text = StringField('text', validators=[InputRequired(), Length(min=0, max=1000)])


class EmailForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])


class PasswordForm(FlaskForm):
    password = PasswordField(
        'password',
        validators=[InputRequired(),
                    Length(min=8, max=80, message='Password must be between 8 and 80 characters long.')])
    confirm = PasswordField('Repeat Password', validators=[
        DataRequired(), EqualTo('password', message="Passwords must match")])


class AlertsForm(FlaskForm):
    symbols = StringField('symbols', validators=[InputRequired(), Length(max=20)])
    analytics = BooleanField('analytics')
    news = BooleanField('news')
    enabled = BooleanField('enabled')


class JyforumForm(FlaskForm):
    message_forum = StringField('message_forum', validators=[InputRequired()])
    reply = BooleanField('reply')
