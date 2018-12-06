from flask import render_template, request

from ai_site import app
from ai_site.models.news import News, NewsCategory
from ai_site.models.page import Page


@app.route("/")
@app.route("/home")
def home():
    print(Page.query.filter_by(name="home").first())
    return render_template("home.html", title='Home', page=Page.query.filter_by(name="home").first())


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/news/<int:category_id>/page/<int:page_number>")
def news(category_id, page_number):
    if category_id == 0:
        page = request.args.get('page', page_number, type=int)
        news = News.query.order_by(News.date_posted.desc()).paginate(page=page, per_page=12)
        return render_template('news.html', title='News', category_id=category_id, news_list=news,
                               categories=NewsCategory.query.all())
    else:
        page = request.args.get('page', page_number, type=int)
        news = News.query.filter_by(category_id=category_id).order_by(News.date_posted.desc()).paginate(page=page,
                                                                                                        per_page=12)
        return render_template("news.html", title='News', category_id=category_id, news_list=news,
                               categories=NewsCategory.query.all())


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title='Contacts')
