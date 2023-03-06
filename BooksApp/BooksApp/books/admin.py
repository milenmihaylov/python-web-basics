from django.contrib import admin

from BooksApp.books.models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'pages']
	# filter = ['title', 'author', 'pages']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass
