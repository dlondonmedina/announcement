from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SubmitField, HiddenField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired
from datetime import datetime

class AnnouncementForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body')
    location = StringField('Location')
    dt = DateTimeLocalField('Date/Time', default=datetime.now(), format='%Y-%m-%d %H:%M')
    submit = SubmitField('Submit')


