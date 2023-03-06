from django import forms

from BooksApp.books.models import Book, Author

"""
class BookForm(forms.ModelForm):
	author_name = forms.CharField(
		max_length=20,
	)

	def save(self, commit=True):
		author = Author.objects.create(name=self.cleaned_data['author_name'])
		author.save()
		self.instance.author = author
		return super().save(commit)

	class Meta:
		model = Book
		fields = ('title', 'pages', 'description', 'author_name')
		widgets = {
			'title': forms.TextInput(
				attrs={
					'class': 'form-control',
				},
			),
			'pages': forms.NumberInput(
				attrs={
					'class': 'form-control',
				},
			),
			'author_name': forms.TextInput(
				attrs={
					'class': 'form-control',
				},
			),
			'description': forms.Textarea(
				attrs={
					'class': 'form-control',
				},
			),
		}
"""


class BootstrapFormMixin:
	def _init_bootstrap(self):
		for (_, field) in self.fields.items():
			field.widget.attrs = {
				'class': 'form-control'
			}


class BookForm(forms.ModelForm, BootstrapFormMixin):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._init_bootstrap()

	class Meta:
		model = Book
		fields = ('title', 'pages', 'description')


class AuthorForm(forms.ModelForm, BootstrapFormMixin):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._init_bootstrap()

	def save(self, commit=True):
		db_author = Author.objects.filter(author_name=self.instance.author_name)\
			.first()
		if db_author:
			return db_author
		else:
			return super().save(commit)

	class Meta:
		model = Author
		fields = '__all__'
