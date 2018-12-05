from flask import render_template, flash, url_for, redirect, request

from ai_site import app, db
from ai_site.forms import PageForm, PageTextForm
from ai_site.models.page import Page, PageText
from ai_site.utils import save_picture, delete_picture


@app.route("/page/save", methods=['GET', 'POST'])
def page_save():
    form = PageForm()
    if form.validate_on_submit():
        page = Page(name=form.name.data)
        db.session.add(page)
        db.session.commit()
        flash('The page has been added!', 'success')
        return redirect(url_for('page_get_one', page_id=page.id))
    return render_template("page/new_page.html", title='Add Page', form=form, legend='Add')


@app.route("/page/get-one/<int:page_id>", methods=['GET', 'POST'])
def page_get_one(page_id):
    form = PageForm()
    page = Page.query.get_or_404(page_id)
    if form.validate_on_submit():
        page.name = form.name.data
        db.session.commit()
        flash('The page has been updated!', 'success')
        return redirect(url_for('page_get_one', page_id=page.id))
    elif request.method == 'GET':
        form.name.data = page.name
    return render_template("page/page_one.html", title=page.name, page=page, legend='Update', submit='Update',
                           form=form)


@app.route("/page/get-all")
def page_get_all():
    return render_template("page/page_all.html", title='Page', pages=Page.query.all())


@app.route("/page/delete/<int:page_id>")
def page_delete(page_id):
    page = Page.query.get_or_404(page_id)
    for one in page.texts:
        delete_picture('page_pics', one.image)
    db.session.delete(page)
    db.session.commit()
    flash('The page has been deleted!', 'danger')
    return redirect(url_for('page_get_all'))


@app.route("/page-text/save/<int:page_id>", methods=['GET', 'POST'])
def page_text_save(page_id):
    form = PageTextForm()
    if form.validate_on_submit():
        page_text = PageText(primary_text=form.primary_text.data, secondary_text=form.secondary_text.data,
                             position=form.position.data, page_id=page_id)
        if form.image.data:
            page_text.image = save_picture(form.image.data, 'page_pics')
        db.session.add(page_text)
        db.session.commit()
        flash('The new element has been added!', 'success')
        return redirect(url_for('page_get_one', page_id=page_id))
    return render_template("page/new_page_text.html", title='Add element', form=form, legend='Add')


@app.route("/page-text/delete/<int:page_text_id>")
def page_text_delete(page_text_id):
    page_text = PageText.query.get_or_404(page_text_id)
    delete_picture('page_pics', page_text.image)
    db.session.delete(page_text)
    db.session.commit()
    flash('The element has been deleted!', 'danger')
    return redirect(url_for('page_get_one', page_id=page_text.page_id))


@app.route("/page_text/update/<int:page_text_id>", methods=['GET', 'POST'])
def page_text_update(page_text_id):
    page_text = PageText.query.get_or_404(page_text_id)
    form = PageTextForm()
    if form.validate_on_submit():
        page_text.primary_text = form.primary_text.data
        page_text.secondary_text = form.secondary_text.data
        page_text.position = form.position.data
        if form.image.data:
            page_text.image = save_picture(form.image.data, 'page_pics')
        db.session.commit()
        flash('The element has been updated!', 'success')
        return redirect(url_for('page_get_one', page_id=page_text.page_id))
    elif request.method == 'GET':
        form.primary_text.data = page_text.primary_text
        form.secondary_text.data = page_text.secondary_text
        form.position.data = page_text.position
    return render_template("page/new_page_text.html", title='Update element', form=form, legend='Update')


@app.route("/page-text/delete-image/<int:page_text_id>")
def page_text_delete_image(page_text_id):
    page_text = PageText.query.get_or_404(page_text_id)
    delete_picture('page_pics', page_text.image)
    page_text.image = ''
    db.session.commit()
    flash('The image has been deleted!', 'info')
    return redirect(url_for('page_get_one', page_id=page_text.page_id))
