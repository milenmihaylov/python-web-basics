from django import forms

from todos_app.todos.models import Todo
from todos_app.todos.validators import validate_owner_todos_count


# def validate_min_length(min_length):
# 	def validate(value):
# 		if len(value) < min_length:
# 			raise forms.ValidationError(f'{value} does not meet min length requirement')
# 	return validate

class CreateTodoModelForm(forms.ModelForm):

	class Meta:
		model = Todo
		fields = '__all__'
		widgets = {
			'owner': forms.RadioSelect()
		}


class CreateTodoForm(forms.Form):
	title = forms.CharField(
		max_length=30,
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

	def clean(self):
		validate_owner_todos_count(self.cleaned_data['owner'])

	def clean_bot_catcher(self):
		value = self.cleaned_data['bot_catcher']
		if value:
			raise forms.ValidationError('You are a bot')


class UpdateTodoForm(CreateTodoForm):
	state = forms.BooleanField()
