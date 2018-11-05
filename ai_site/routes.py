from flask import render_template, flash, url_for, redirect

from ai_site import app
from ai_site.forms.callback_forms import LeaveCallbackForm
from ai_site.services.callback_service import save


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title='Home')


@app.route("/leave-callback", methods=['GET', 'POST'])
def leave_callback():
    form = LeaveCallbackForm()
    if form.validate_on_submit():
        callback = save(form)
        if callback:
            flash('Thank you for your callback!', 'success')
        else:
            flash('Something went wrong!', 'info')
        return redirect(url_for('home'))
    else:
        flash(form.errors, 'danger')
    return render_template("callback.html", title='Callback', form=form)
