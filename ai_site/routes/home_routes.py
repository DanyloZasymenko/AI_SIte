from flask import render_template

from ai_site import app
from ai_site.models.news import News


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home')


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/news")
def news():
    return render_template('news.html', title='News', news_list=News.query.all())
