from django.urls import path
from BooksApp.books.views import create, index, edit

urlpatterns = [
	path('', index, name='index'),
	path('create/', create, name='create'),
	path('edit/<int:pk>', edit, name='edit'),
]
