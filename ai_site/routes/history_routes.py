from flask import render_template, flash, url_for, redirect, request

from ai_site import app, db
from ai_site.forms import HistoryForm
from ai_site.models.history import History
from ai_site.utils import save_picture


@app.route("/history/save", methods=['GET', 'POST'])
def history_save():
    form = HistoryForm()
    if form.validate_on_submit():
        history = History(header=form.header.data, description=form.description.data, date=form.date.data,
                          image=save_picture(form.image.data, "history_pics"))
        db.session.add(history)
        db.session.commit()
        flash('The history has been added!', 'success')
        return redirect(url_for('history_get_all'))
    return render_template("history/new_history.html", title='Add History', form=form, legend='Add')


@app.route("/history/get-all")
def history_get_all():
    return render_template("history/history_all.html", title='History', histories=History.query.all())


@app.route("/history/update/<int:history_id>", methods=['GET', 'POST'])
def history_update(history_id):
    history = History.query.get_or_404(history_id)
    form = HistoryForm()
    if form.validate_on_submit():
        if form.image.data:
            history.image = save_picture(form.image.data, "history_pics")
        history.header = form.header.data
        history.description = form.description.data
        history.date = form.date.data
        db.session.commit()
        flash('The history has been updated!', 'success')
        return redirect(url_for('history_get_all'))
    elif request.method == 'GET':
        form.header.data = history.header
        form.description.data = history.description
        form.date.data = history.date
    return render_template("history/new_history.html", title='Update History', form=form, legend='Update')


@app.route("/history/delete/<int:history_id>")
def history_delete(history_id):
    history = History.query.get_or_404(history_id)
    db.session.delete(history)
    db.session.commit()
    flash('The history has been deleted!', 'danger')
    return redirect(url_for('history_get_all'))
