from flask import render_template, request

from ai_site import app
from ai_site.models.page import Page
from ai_site.models.partner import Partner
from ai_site.models.course import Course
from ai_site.models.history import History


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
    return render_template("department.html", title='Department', partners=Partner.query.all(),
                           history = History.query.order_by(History.date.asc()).all())

@app.route("/courses/<int:year>")
def courses(year):
    courses_s1 = Course.query.filter_by(year=year, semester=1)
    courses_s2 = Course.query.filter_by(year=year, semester=2)
    return render_template("courses.html", title='Courses',  semestr1 = courses_s1, semestr2 = courses_s2)

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title='Contacts')
