from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from ai_site import app, bCrypt
from ai_site.forms import LoginForm
from ai_site.models.course import Course
from ai_site.models.history import History
from ai_site.models.news import News, NewsCategory
from ai_site.models.page import Page
from ai_site.models.partner import Partner
from ai_site.models.teacher import Teacher
from ai_site.models.user import User


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
                           history=History.query.order_by(History.date.asc()).all())


@app.route("/courses/<int:year>")
def courses(year):
    courses_s1 = Course.query.filter_by(year=year, semester=1)
    courses_s2 = Course.query.filter_by(year=year, semester=2)
    return render_template("course/courses.html", title='Courses', semestr1=courses_s1, semestr2=courses_s2)


@app.route("/science")
def science():
    teachers = Teacher.query.order_by(Teacher.name.asc()).all()
    return render_template("science.html", title='Science', teachers_list=teachers)
    # return render_template("course/courses.html", title='Courses', semestr1 = courses_s1, semestr2 = courses_s2)


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")




@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        if form.username.data == User.username and bCrypt.check_password_hash(User.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
