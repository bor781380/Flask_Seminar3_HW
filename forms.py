from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#
# class RegisterForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     age = IntegerField('Age', validators=[DataRequired()])
#     gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])

class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    lastname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])

