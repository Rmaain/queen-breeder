from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SubmitField, PasswordField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from app.models import User

# add password type again
# add Email verification

class RegistrationForm(FlaskForm):
    username = StringField('Nome', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()]) #add email validators
    password = PasswordField('Senha', validators=[DataRequired()]) #add max length
    submit = SubmitField('Entrar')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Já existe um usuario com esse nome')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')
class FrameForm(FlaskForm):
    image=FileField('Quadro')
class AddHivesForm(FlaskForm):
    hive_number = IntegerField('Numero da colmeia', validators=[DataRequired()])
    temperament = SelectField('Avalie o temperamento', choices=[str(i) for i in range(1, 6)], validators=[DataRequired()])
    frames = FieldList(FormField(FrameForm), min_entries=2)
    submit = SubmitField('Submit')
    # image
        # frame number in the image

    # maybe 
    # lineage
    # date
    # estimated age of the queen