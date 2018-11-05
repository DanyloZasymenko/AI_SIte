from datetime import datetime

from ai_site import db


def __init__():
    return History


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"History('{self.header}', '{self.description}', '{self.datetime}')"
