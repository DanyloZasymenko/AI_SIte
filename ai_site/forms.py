from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email
from wtforms_sqlalchemy.fields import QuerySelectField

from ai_site.models.news import news_category_query


class CallbackForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired(), Length(min=10, max=22)])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Leave callback')


class HistoryForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date')
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add')


class PartnerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add')


class NewsForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired(), Length(min=1, max=70)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png'])])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = QuerySelectField('Choose category', validators=[DataRequired()],
                                query_factory=news_category_query, allow_blank=False, get_label='name')
    submit = SubmitField('Add')


class NewsCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Add')
