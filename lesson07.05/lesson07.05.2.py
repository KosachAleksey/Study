from flask import Flask
# Создан объект для упраления веб-сервером
app = Flask(__name__)

@app.route('/') #устанавливает маршрут для главной страницы
def hello():
    return "Main world"

@app.route('/about')
def about():
    return "Information about the author of the website"

@app.route('/user/<username>')
def user_profile(username):
    return f"This page is for the user {username} "

if __name__ == "__main__":
    app.run(port=8000, debug=True)