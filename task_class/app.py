from flask import Flask, render_template, request
import sqlite3
import os

# Название базы данных
DATABASE_NAME = 'database.db'

# Путь к базе данных (явно зададим абсолютный путь относительно расположения файла)
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

# Создаем базу данных и таблицу users
def init_db():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                age INTEGER,
                gender TEXT,
                hobbies TEXT,
                city TEXT
            );
        ''')
        conn.commit()

# Подключение к базе данных
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Основной класс приложения
app = Flask(__name__)

# Загрузка начальной страницы с формой
@app.route('/', methods=['GET'])
def show_form():
    return render_template('form.html')

# Отправка данных формы и сохранение в базу данных
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Получаем данные из формы
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        age = int(request.form['age'])
        gender = request.form['gender']
        hobbies = ','.join(request.form.getlist('hobbies'))  # Преобразование списка увлечений в строку
        city = request.form['city']
        
        # Соединяемся с базой данных и вставляем данные
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (first_name, last_name, email, age, gender, hobbies, city)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (first_name, last_name, email, age, gender, hobbies, city))
            conn.commit()
            user_id = cursor.lastrowid
        
        return f'Данные успешно сохранены! Ваш ID: {user_id}'
    except Exception as e:
        return f'Ошибка при сохранении данных: {str(e)}'

if __name__ == '__main__':
    init_db()  # Создаем таблицу при запуске приложения
    app.run(debug=True)