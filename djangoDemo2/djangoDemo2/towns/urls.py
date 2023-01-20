from django.urls import path

from djangoDemo2.towns.views import create_person

urlpatterns = [
	path('create/', create_person)
]
