from django.shortcuts import render, redirect

from BooksApp.books.forms import BookForm, AuthorForm
from BooksApp.books.models import Book, Author


def index(request):
	context = {
		'books': Book.objects.all()
	}
	return render(request, 'index.html', context)


def create(request):
	if request.method == 'GET':
		book_form = BookForm()
		author_form = AuthorForm()
		return show_form(request, book_form, author_form, 'create.html')
	else:
		book_form = BookForm(request.POST)
		author_form = AuthorForm(request.POST)
		if book_form.is_valid() and author_form.is_valid():
			author = author_form.save()
			book = book_form.save(commit=False)
			book.author = author
			book.save()
			return redirect('index')
		return show_form(request, book_form, author_form, 'create.html')


def edit(request, pk):
	book = Book.objects.get(pk=pk)
	book_form = BookForm(initial=book.__dict__)
	author_form = AuthorForm(initial=Author.objects.get(pk=book.author_id).__dict__)
	if request.method == 'GET':
		return show_form(request, book_form, author_form, 'edit.html')

	else:
		book_form = BookForm(
			request.POST,
			instance=book,
		)
		author_form = AuthorForm(
			request.POST,
			instance=book.author
		)
		if book_form.is_valid() and author_form.is_valid():
			book_form.save()
			author_form.save()
			return redirect('index')
		return show_form(request, book_form, author_form, 'edit.html')


def show_form(request, book_form, author_form, template):
	context = {
		'book_form': book_form,
		'author_form': author_form,
	}
	return render(request, template, context)


def show_edit_form(request, book_form, template):
	context = {
		'form': book_form,
	}
	return render(request, template, context)
