from flask_wtf import FlaskForm#从flask_wtf包中导入FlaskForm类
from wtforms import StringField,PasswordField,BooleanField,SubmitField, TextAreaField#导入这些类
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeated Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()

		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()

		if user is not None:
			raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About_me', validators=[Length(min=0, max=140)])
	submit = SubmitField('Submit')

	##############  Check whether you are using a used username.  ##############
	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username
	
	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()

			if user is not None:
				raise ValidationError('Please use a different username!')
	############################################################################

class PostForm(FlaskForm):
	post = TextAreaField('Dude, Ask Anything!!', validators=[DataRequired(), Length(min=1, max=140)])

	submit = SubmitField('Submit')