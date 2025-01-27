from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

# Custom validators
def validate_tool_id(form, field):
    if len(field.data) != 8:  # Example: Tool ID must be 8 characters long
        raise ValidationError('Tool ID must be exactly 8 characters long.')

def validate_badge_id(form, field):
    if not field.data.isalnum():  # Example: Badge ID must be alphanumeric
        raise ValidationError('Badge ID must be alphanumeric.')

class CheckInForm(FlaskForm):
    tool_id_number = StringField('Tool ID', validators=[DataRequired(), validate_tool_id])
    checkin_time = DateTimeField('Check In Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(CheckInForm, self).__init__(*args, **kwargs)
        self.checkin_time.data = datetime.now()

class CheckOutForm(FlaskForm):
    username_or_badge_id = StringField('Username or Badge ID', validators=[DataRequired(), validate_badge_id])
    tool_id_number = StringField('Tool ID', validators=[DataRequired(), validate_tool_id])
    checkout_time = DateTimeField('Check Out Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(CheckOutForm, self).__init__(*args, **kwargs)
        self.checkout_time.data = datetime.now()
