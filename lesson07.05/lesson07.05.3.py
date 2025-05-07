from flask import Flask

# Создаем объект для управления веб-сервером
app = Flask(__name__)

@app.route('/<int:first>-<int:second>')  # Устанавливает маршрут для вычитания
def minus(first, second):
    return f"{first - second}"

@app.route('/<int:first>+<int:second>')  # Устанавливает маршрут для сложения
def plus(first, second):
    return f"{first + second}"

@app.route('/<int:first>*<int:second>')  # Устанавливает маршрут для умножения
def multiply(first, second):
    return f"{first * second}"

@app.route('/divide/<int:first>/<int:second>')  # Маршрут для целочисленного деления
def divide(first, second):
        return f"{first // second}"
 

if __name__ == "__main__":
    app.run(port=8000, debug=True)