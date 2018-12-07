from flask import render_template, request

from ai_site import app
from ai_site.models.news import News, NewsCategory
from ai_site.models.page import Page


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
