from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqlamodel import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '246dcac184d5fd3ae934da622bc69e4a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/ai_site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from ai_site.models.history import History
from ai_site.models.сallback import Callback
from ai_site.models.news import News, NewsCategory, NewsComment, NewsView
from ai_site.models.page import Page, PageText
from ai_site.models.partner import Partner
from ai_site.models.project import ProjectPicture, Project
from ai_site.models.quotation import Quotation
from ai_site.models.teacher import Teacher
from ai_site.routes import home_routes

admin = Admin(app)

admin.add_view(ModelView(History, db.session))
admin.add_view(ModelView(Callback, db.session))
admin.add_view(NewsView(News, db.session, category='News'))
admin.add_view(ModelView(NewsCategory, db.session, category='News'))
admin.add_view(ModelView(Partner, db.session))
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Quotation, db.session))
admin.add_view(ModelView(Teacher, db.session))
