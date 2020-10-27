from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from .. import db

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitch(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    category = SelectField("What category are you submitting to?", choices=[("Event", "Event Pitches"), ( "Elevator", "Elevator Pitches"), ("Motivational", "Motivational Pitches"), ("Job", "Job Pitches")],validators=[Required()])
    content = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')    