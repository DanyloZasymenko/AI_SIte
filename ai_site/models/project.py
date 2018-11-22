import enum

from ai_site import db


class Years(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6


class Semesters(enum.Enum):
    FIRST = 1
    SECOND = 2


class ProjectPicture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __repr__(self):
        return f"ProjectPicture('{self.id}', '{self.project_id}')"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    image = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    authors = db.Column(db.String(180), nullable=False)
    url = db.Column(db.String(70))
    year = db.Column(db.Enum(Years), default=Years.FIRST)
    semester = db.Column(db.Enum(Semesters), default=Semesters.FIRST)
    pictures = db.relationship('ProjectPicture', backref='project', lazy=True)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.authors}', '{self.year}','{self.semester}')"
