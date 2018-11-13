from ai_site import db


class PageText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20))
    position = db.Column(db.Integer, nullable=False, default=1)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)

    def __repr__(self):
        return f"PageText('{self.text}', '{self.position}', '{self.page_id}')"


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    texts = db.relationship('PageText', backref='page', lazy=True)

    def __repr__(self):
        return f"Page('{self.name}')"
