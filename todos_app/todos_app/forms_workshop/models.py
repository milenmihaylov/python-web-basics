from django.db import models


class User(models.Model):
	name = models.CharField(
		max_length=30,
	)
	age = models.IntegerField()
	email = models.EmailField()
	password = models.CharField(
		max_length=30,
	)
	text = models.CharField(
		max_length=50,
	)

