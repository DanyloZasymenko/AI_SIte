import wtforms_sqlalchemy.fields as f
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def get_pk_from_identity(obj):
    cls, key = f.identity_key(instance=obj)[:2]
    return ':'.join(f.text_type(x) for x in key)


f.get_pk_from_identity = get_pk_from_identity

MY_API_KEY = '36ef29ad4020bf2da8f93c12ae260636'

app = Flask(__name__)
app.config['SECRET_KEY'] = '246dcac184d5fd3ae934da622bc69e4a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/ai_site'
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
from ai_site.routes import home_routes, history_routes, partner_routes, news_routes, project_routes, page_routes, \
    teacher_routes
from ai_site.utils import get_scopus_h_index

get_scopus_h_index()