from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator

from todos_app.forms_workshop.models import User


PASSWORD_ERROR_MESSAGE = "Enter a valid password."
def validate_email(value):
	if User.objects.filter(email=value).first():
		raise forms.ValidationError("Email is already submitted!")

def validate_name(value:str):
	if not value[0].isupper():
		raise forms.ValidationError("The name must start with an uppercase letter.")

def validate_password(value: str):
	if not all([char.isalnum() for char in value]):
		raise forms.ValidationError(PASSWORD_ERROR_MESSAGE)

class WorkshopForm(forms.Form):
	name = forms.CharField(
		widget=forms.TextInput(),
		validators=[
			validate_name,
			MinLengthValidator(
				limit_value=6,
			),
		],
	)
	age = forms.IntegerField(
		widget=forms.NumberInput(),
		validators=[
			MinValueValidator(
				limit_value=0,
				message="The age cannot be less than zero.",
			),
		],
	)
	email = forms.EmailField(
		widget=forms.EmailInput(),
		validators=[
			EmailValidator(
				message="Enter a valid email.",
			),
			validate_email,
		],
	)
	password = forms.CharField(
		widget=forms.PasswordInput(),
		validators=[
			MinLengthValidator(
				limit_value=8,
				message=PASSWORD_ERROR_MESSAGE,
			),
		],
	)
	text = forms.CharField(
		widget=forms.Textarea(),
	)
	bot_catcher = forms.CharField(
		widget=forms.HiddenInput(),
		required=False,
		max_length=0,
	)

	# def clean_password(self):
	# 	pure_password = self.cleaned_data['password']
	# 	return f'!{pure_password}!' # 'encode' the password

	# def clean_name(self):
	# 	if not self.cleaned_data['name'].isupper():
	# 		raise forms.ValidationError("The name must start with an uppercase letter.")
	def clean_bot_catcher(self):
		value = self.cleaned_data['bot_catcher']
		if value:
			raise forms.ValidationError("This form was created by a bot")
