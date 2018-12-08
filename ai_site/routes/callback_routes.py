from flask import render_template, request, flash, redirect, url_for

from ai_site import app, db
from ai_site.models.сallback import Callback
from ai_site.forms import CallbackForm



@app.route("/contacts", methods=['GET', 'POST'])
def contacts():
    form = CallbackForm()
    if form.validate_on_submit():
        callBack = Callback(username=form.username.data, email=form.email.data, phone=form.phone.data,
                            subject=form.subject.data, message=form.message.data)
        db.session.add(callBack)
        db.session.commit()
        # flash('The callback has been added!', 'success')
        return redirect(url_for('contacts'))
    # return render_template("partner/new_partner.html", title='Add Partner', form=form, legend='Add')
    return render_template("callback/contacts.html", title='Contacts', form = form)

@app.route("/callback/get-all")
def callback_get_all():
    return render_template("callback/callback_all.html", title='Callback', callbacks=Callback.query.all())

@app.route("/callback/delete/<int:callback_id>")
def callback_delete(callback_id):
    callback = Callback.query.get_or_404(callback_id)
    db.session.delete(callback)
    db.session.commit()
    flash('The callback has been deleted!', 'danger')
    return redirect(url_for('callback_get_all'))