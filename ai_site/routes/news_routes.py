from flask import render_template, flash, url_for, redirect, request

from ai_site import app, db
from ai_site.forms import NewsForm, NewsCategoryForm
from ai_site.models.news import News, NewsCategory
from ai_site.utils import save_picture, delete_picture


@app.route("/news/<int:news_id>")
def news_get_one(news_id):
    news = News.query.get_or_404(news_id)
    print(news)
    return render_template("oneNews.html", title=news.header, oneNews=news)

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


@app.route("/news/save", methods=['GET', 'POST'])
def news_save():
    form = NewsForm()
    if form.validate_on_submit():
        news = News(header=form.header.data, description=form.description.data, text=form.text.data,
                    image=save_picture(form.image.data, 'news_pics'), category=form.category.data)
        db.session.add(news)
        db.session.commit()
        flash('The news has been added!', 'success')
        return redirect(url_for('news_get_all'))
    return render_template("news/new_news.html", title='Add News', form=form, legend='Add')


@app.route("/news-category/save", methods=['GET', 'POST'])
def news_category_save():
    form = NewsCategoryForm()
    if form.validate_on_submit():
        news_category = NewsCategory(name=form.name.data)
        db.session.add(news_category)
        db.session.commit()
        flash('The news category has been added!', 'success')
        return redirect(url_for('news_get_all'))
    return render_template("news/new_news_category.html", title='Add News Category', form=form, legend='Add')


@app.route("/news/get-all")
def news_get_all():
    return render_template("news/news_all.html", title='News', news=News.query.all(),
                           categories=NewsCategory.query.all())


@app.route("/news/update/<int:news_id>", methods=['GET', 'POST'])
def news_update(news_id):
    news = News.query.get_or_404(news_id)
    form = NewsForm()
    if form.validate_on_submit():
        if form.image.data:
            delete_picture('news_pics', news.image)
            news.image = save_picture(form.image.data, 'news_pics')
        news.header = form.header.data
        news.description = form.description.data
        news.text = form.text.data
        news.category = form.category.data
        db.session.commit()
        flash('The news has been updated!', 'success')
        return redirect(url_for('news_get_all'))
    elif request.method == 'GET':
        form.header.data = news.header
        form.description.data = news.description
        form.text.data = news.text
        form.category.data = news.category
    return render_template("news/new_news.html", title='Update News', form=form, legend='Update')


@app.route("/news/delete/<int:news_id>")
def news_delete(news_id):
    news = News.query.get_or_404(news_id)
    delete_picture('news_pics', news.image)
    db.session.delete(news)
    db.session.commit()
    flash('The news has been deleted!', 'danger')
    return redirect(url_for('news_get_all'))


@app.route("/news-category/delete/<int:news_category_id>/<delete_with_news>")
def news_category_delete(news_category_id, delete_with_news):
    category = NewsCategory.query.get_or_404(news_category_id)
    if delete_with_news == 'True':
        for news in category.news:
            delete_picture('news_pics', news.image)
            db.session.delete(news)
    db.session.delete(category)
    db.session.commit()
    flash('The news category has been deleted!', 'danger')
    return redirect(url_for('news_get_all'))


@app.route("/news-category/update/<int:news_category_id>", methods=['GET', 'POST'])
def news_category_update(news_category_id):
    category = NewsCategory.query.get_or_404(news_category_id)
    form = NewsCategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('The news category has been updated!', 'success')
        return redirect(url_for('news_get_all'))
    elif request.method == 'GET':
        form.name.data = category.name
    return render_template('news/new_news_category.html', title='Update News Category', form=form, legend='Update')
