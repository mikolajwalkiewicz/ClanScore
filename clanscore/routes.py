from flask import render_template
from clanscore import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home page")
