from ai_site import db
from ai_site.models.сallback import Callback


def save(form):
    callback = Callback(username=form.username.data, email=form.email.data, phone=form.phone.data,
                        subject=form.subject.data, message=form.message.data)
    db.session.add(callback)
    db.session.commit()
    return callback


def get_one(id):
    return Callback.query.filter_by(id == id).first()


def get_all():
    return Callback.query.all()


def delete(id):
    callback = Callback.query.filter_by(id == id).first()
    callback.delete()
    db.session.commit()
