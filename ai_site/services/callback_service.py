from ai_site import db
from ai_site.models.сallback import Callback


def save(form):
    callback = Callback(username=form.username.data, email=form.email.data, phone=form.phone.data,
                        subject=form.subject.data, message=form.message.data)
    db.session.add(callback)
    db.session.commit()
    return callback
