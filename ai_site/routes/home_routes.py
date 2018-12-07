from flask import render_template, request

from ai_site import app
from ai_site.models.news import News, NewsCategory
from ai_site.models.page import Page
from ai_site.models.partner import Partner


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home', page=Page.query.filter_by(name="home").first())

@app.route("/admission")
def admission():
    texts = []
    page = Page.query.filter_by(name="admission").first()
    # print(Page.query.filter_by(name="admission").first())
    for one in page.texts:
        texts.insert(one.position, one)
    return render_template("admission.html", title='Admission', texts=texts)

@app.route("/department")
def department():
    return render_template("department.html", title='Department', partners=Partner.query.all())

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title='Contacts')
