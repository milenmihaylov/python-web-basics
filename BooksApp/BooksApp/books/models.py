from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
	author_name = models.CharField(
		max_length=20,
	)

	def __str__(self):
		return self.author_name


class Book(models.Model):
	title = models.CharField(
		max_length=20,

	)

	pages = models.IntegerField(
		validators=(
			MinValueValidator(1),
		),
	)

	description = models.CharField(
		max_length=100,
		default='',
	)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
