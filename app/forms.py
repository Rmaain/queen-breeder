from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app import User

# add password type again
# add Email verification

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()]) #add email validators
    password = PasswordField('Password', validators=[DataRequired()]) #add max length
    submit = SubmitField('Submit')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Já existe um usuario com esse nome')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')