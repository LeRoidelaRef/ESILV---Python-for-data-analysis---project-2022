from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route("/<name>", methods=('GET', 'POST'))
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/avila_bible", methods=('GET', 'POST'))
def show_bible():
    return render_template('show_bible.html')

@app.route("/test", methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            return "<p>Success!</p>"

        flash(error)
    return render_template('register.html')

with app.test_request_context():
    print(url_for("show_bible"))
