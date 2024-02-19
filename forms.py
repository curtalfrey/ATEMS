# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from datetime import datetime


class CheckInForm(FlaskForm):
    tool_id_number = StringField('Tool ID', validators=[DataRequired()])
    checkin_time = HiddenField('Check In Time', default=datetime.now().strftime('%Y-%m-%dT%H:%M'), validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class CheckOutForm(FlaskForm):
    username_or_badge_id = StringField('Username or Badge ID', validators=[DataRequired()])
    tool_id_number = StringField('Tool ID', validators=[DataRequired()])
    checkout_time = HiddenField('Check Out Time', default=datetime.now().strftime('%Y-%m-%dT%H:%M'), validators=[DataRequired()])
