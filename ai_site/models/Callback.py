from datetime import datetime

from ai_site import db


def __init__():
    return Callback


class Callback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(13))
    subject = db.Column(db.String(60), nullable=False)
    message = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Callback('{self.username}', '{self.email}', '{self.subject}', '{self.message}', '{self.datetime}')"
