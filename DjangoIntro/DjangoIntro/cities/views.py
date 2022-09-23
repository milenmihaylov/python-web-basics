from django.http import HttpResponse
from django.shortcuts import render, redirect

from DjangoIntro.cities.models import Person


def index(req):
    context = {
        'name': 'Milen',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def test_index(req):
    return HttpResponse(
        '{"name": "Doncho"}',
        content_type='application/json',
    )


def create_person(req):
    Person(
        name='Pesho',
        age=31,
        home_town='Sofia'
    ).save()

    return redirect('/cities')


def list_phones(request):
    # return HttpResponse('Phones list')
    context = {
        'phones': ['Galaxy S500', 'Xiaomi redmi T9', 'iPhone 12']
    }
    return render(request, 'phones.html', context)
