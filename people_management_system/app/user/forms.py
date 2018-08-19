from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app import User

class UserForm(FlaskForm):
	"""
	Form for users to create new account
	"""
	email = StringField('Email',validators=[DataRequired(), Email()])
	username = StringField('Username', validators=[DataRequired()])
	submit = SubmitField('Register')
	def validate_email(self, filed):
		if User.query.filter_by(email=filed.data).first():
			raise ValidationError("Email is already in use!")

	def validate_username(self, filed):
		if User.query.filter_by(username=filed.data).first():
			raise ValidationError("Username is already in use!")

class FindUserForm(FlaskForm):
	'''
	Form for find user
	'''
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Find User')
