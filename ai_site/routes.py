from ai_site import app

from flask import render_template, flash, url_for, redirect, request, abort


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title=home)
