from datetime import datetime

from ai_site import db


def __init__():
    return News, NewsComment, NewsCategory


class NewsComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)

    def __repr__(self):
        return f"NewsComment('{self.username}', '{self.email}', '{self.datetime}', '{self.message}')"


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(70), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('news_category.id'), nullable=False)
    comments = db.relationship('NewsComment', backref='news', lazy=True)

    def __repr__(self):
        return f"News('{self.header}', '{self.description}', '{self.date_posted}')"


class NewsCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    news = db.relationship('News', backref='category', lazy=True)

    def __repr__(self):
        return f"NewsCategory('{self.name}')"
