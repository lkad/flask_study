from flask.ext.wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
class NameForm(FlaskForm):  
    name = StringField("what's your name ?",validators=[Required()])
    submit = SubmitField('Submit')    

