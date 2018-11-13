from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '246dcac184d5fd3ae934da622bc69e4a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/ai_site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from ai_site.models.history import History
from ai_site.models.сallback import Callback
from ai_site.models.news import News, NewsCategory, NewsComment
from ai_site.models.page import Page, PageText
from ai_site.models.partner import Partner
from ai_site.models.project import ProjectPicture, Project
from ai_site.models.quotation import Quotation
from ai_site.models.teacher import Teacher
from ai_site.routes import home_routes, history_routes, partner_routes
