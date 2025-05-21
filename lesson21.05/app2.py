from flask import Flask, request, render_template
from flask_wtf import CSRFProtect
from forms import RegistrationForm
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

csrf = CSRFProtect()


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

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        return f"Успешная регистрация"
    
    return render_template("register.html", form=form)

if __name__ == "__main__":
    init_db()  
    app.run(debug=True)


