from django.shortcuts import render, redirect

from djangoDemo2.towns.models import Person


def index(request):
	context = {
		'name': 'Milen',
		'people': Person.objects.all()
	}
	return render(request, 'index.html', context)


def create_person(request):
	Person(
		name=request.POST['name'],
		age=int(request.POST['age']),
		home_town='Bozhurishte'
	).save()

	return redirect('/')
