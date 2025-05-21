from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form.get('password')

        if not re.match(r'^[А-я].+\s[А-я].+$', username):
            return render_template("register.html", username_error=True)

        if not username or not email or not password:
            return render_template ("Все поля обяз. к заполн.", emply_fields=True)
        
        return f"Регистр. успешна {username} <br> email {email}"
    
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
        
