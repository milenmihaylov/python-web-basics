from django import forms


def validate_dot(value):
	if '.' in value:
		raise forms.ValidationError(f'\'.\' is in {value}')

# def validate_min_length(min_length):
# 	def validate(value):
# 		if len(value) < min_length:
# 			raise forms.ValidationError(f'{value} does not meet min length requirement')
# 	return validate

class CreateTodoForm(forms.Form):
	title = forms.CharField(
		max_length=30,
		validators=[
			validate_dot,
			# validate_min_length(30),
		],
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
	)
	description = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'gosho',
			}
		)
	)
	bot_catcher = forms.CharField(
		widget=forms.HiddenInput(),
		required=False,
	)

	def clean_bot_catcher(self):
		value = self.cleaned_data['bot_catcher']
		if value:
			raise forms.ValidationError('You are a bot')


class UpdateTodoForm(CreateTodoForm):
	state = forms.BooleanField()
