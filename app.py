from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER = "admin"
PASS = "canteen123"

menu = [
    {"item": "Veg Sandwich", "price": 50},
    {"item": "Chicken Burger", "price": 80},
    {"item": "Cold Coffee", "price": 40},
]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USER and request.form['password'] == PASS:
            return render_template('menu.html', menu=menu)
        error = "Invalid credentials"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
