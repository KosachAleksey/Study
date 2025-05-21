from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
import sqlite3
from werkzeug.security import generate_password_hash  # Импортируем для хеширования пароля
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Установите секретный ключ для защиты csrf-токенов

app.config['DATABASE'] = 'users.db'

def get_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        cursor.execute(""" 
"""
        )

        db.cursor

def add_user(username, email, password):
    db = get_db()

    password_hash = generate_password_hash(password)
    cursor.executee(""" 
""", (username, email, password_hash))

#нужно добавить хэширование
# Формируем простую регистрационную форму
class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Зарегистрироваться')

# Функция для создания таблицы пользователей
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Основная точка входа в приложение
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Подключаемся к базе данных
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Хешируем пароль перед сохранением
        hashed_password = generate_password_hash(form.password.data)
        
        # Выполняем вставку данных в таблицу
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?,?,?)",
                      (form.username.data, form.email.data, hashed_password))
        
        # Зафиксируем изменения и закроем соединение
        conn.commit()
        conn.close()
        
        return "<h1>Успешная регистрация!</h1>"  # Пока что просто выводим сообщение
    return render_template('register.html', form=form)

if __name__ == '__main__':
    init_db()  # Сначала создаём таблицу
    app.run(debug=True)