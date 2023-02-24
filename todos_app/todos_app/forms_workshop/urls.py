from django.urls import path

from todos_app.forms_workshop.views import fill_out_the_form

urlpatterns = [
	path('', fill_out_the_form),
]
