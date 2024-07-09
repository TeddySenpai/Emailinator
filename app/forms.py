from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class EmailForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')
