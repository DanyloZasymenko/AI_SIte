from ai_site import db


class PageText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primary_text = db.Column(db.Text)
    image = db.Column(db.String(20))
    secondary_text = db.Column(db.Text)
    position = db.Column(db.Integer, nullable=False, default=1)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)

    def __repr__(self):
        return f"PageText('{self.primary_text}', '{self.secondary_text}', '{self.position}', '{self.page_id}')"


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    texts = db.relationship('PageText', backref='page', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"Page('{self.name}')"
