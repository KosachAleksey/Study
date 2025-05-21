from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Имя порльзователя', validators=[
            DataRequired(),
            Length(min=4, max=25),
            Regexp(r'^[А-я].+\s[А-я].+$', message="Необходимо ввести ФИО на русском языке")
    ])

    email = StringField('Email', validators=[
            DataRequired(),
            Email(message="Некорректный емайл")
    ])

    password = PasswordField('Пароль', validators=[
            DataRequired(),
            Length(min=8, message="Пароль должен содержать минимум 8 символов")
    ])

    confirm_password = PasswordField('Подтверждение пароля', validators=[
        DataRequired(),
        EqualTo('password', message="Пароли должны совпадать")
    ])

    submit = SubmitField("Зарегистрироваться")


