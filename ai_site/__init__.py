from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '246dcac184d5fd3ae934da622bc69e4a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/ai_site'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from ai_site.models import Callback, History, Quotation, Partner, Teacher, Project, Page, News
from ai_site import routes
