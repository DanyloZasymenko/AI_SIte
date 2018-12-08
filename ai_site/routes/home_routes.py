from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from ai_site import app, bCrypt
from ai_site.forms import LoginForm
from ai_site.models.news import News, NewsCategory
from ai_site.models.page import Page
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
        print(one.position)
        texts.insert(one.position, one)

    print(texts)
    return render_template("admission.html", title='Admission', texts=texts)


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")


@app.route("/news/<int:category_id>/page/<int:page_number>")
def news(category_id, page_number):
    if category_id == 0:
        page = request.args.get('page', page_number, type=int)
        news = News.query.order_by(News.date_posted.desc()).paginate(page=page, per_page=9)
        return render_template('news.html', title='News', category_id=category_id, news_list=news,
                               categories=NewsCategory.query.all())
    else:
        page = request.args.get('page', page_number, type=int)
        news = News.query.filter_by(category_id=category_id).order_by(News.date_posted.desc()).paginate(page=page,
                                                                                                        per_page=9)
        return render_template("news.html", title='News', category_id=category_id, news_list=news,
                               categories=NewsCategory.query.all())


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title='Contacts')


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
