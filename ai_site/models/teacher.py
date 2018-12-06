from ai_site import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(70))
    incumbency = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    interests = db.Column(db.Text)
    research_directions = db.Column(db.Text)
    hobby = db.Column(db.String(50))
    scopus_id = db.Column(db.String(11))
    scholar_id = db.Column(db.String(12))
    image = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Teacher('{self.name}', '{self.position}', '{self.incumbency}', '{self.description}')"
