from flask import render_template

from ai_site import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home')
