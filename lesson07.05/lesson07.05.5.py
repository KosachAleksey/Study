from flask import Flask

# Создаем объект для управления веб-сервером
app = Flask(__name__)

def calculate_url(first, second, operation):
     match operation:
          case "-":
               return f"<h3> resuit: {first-second} </h3>"
          case "+":
               return f"<h3> resuit: {first+second} </h3>"
          case "*":
               return f"<h3> resuit: {first*second} </h3>"
          case "/":
               return f"<h3> resuit: {first/second} </h3>"
          case _:
               return ""
               

@app.route('/<int:first>-<int:second>')  # Устанавливает маршрут для вычитания
def minus(first, second):
    return calculate_url (first, second, "-")

@app.route('/<int:first>+<int:second>')  # Устанавливает маршрут для вычитания
def plus(first, second):
    return calculate_url (first, second, "+")

@app.route('/<int:first>*<int:second>')  # Устанавливает маршрут для вычитания
def multiply(first, second):
    return calculate_url (first, second, "*")

@app.route('/<int:first>/<int:second>')  # Устанавливает маршрут для вычитания
def divide(first, second):
    return calculate_url (first, second, "/")
 

if __name__ == "__main__":
    app.run(port=8000, debug=True)