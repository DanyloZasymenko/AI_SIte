from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField, MultipleFileField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms_sqlalchemy.fields import QuerySelectField

from ai_site.models.news import news_category_query
from ai_site.models.project import Years, Semesters


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


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=70)])
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png'])])
    description = TextAreaField('Description', validators=[DataRequired()])
    authors = TextAreaField('Authors', validators=[DataRequired(), Length(min=1, max=180)])
    url = StringField('Url', validators=[DataRequired(), Length(min=1, max=70)])
    year = SelectField('Year', choices=[(e.name, e.value) for e in Years], validators=[DataRequired()])
    semester = SelectField('Semester', choices=[(e.name, e.value) for e in Semesters], validators=[DataRequired()])
    pictures = MultipleFileField('Choose pictures')
    submit = SubmitField('Add')


class PageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=30)])
    submit = SubmitField()


class PageTextForm(FlaskForm):
    primary_text = TextAreaField('Primary Text')
    image = FileField('Choose image', validators=[FileAllowed(['jpg', 'png'])])
    secondary_text = TextAreaField('Secondary Text')
    position = IntegerField('Position on page', validators=[NumberRange(min=0), DataRequired()])
    submit = SubmitField('Add element')
