from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email


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
