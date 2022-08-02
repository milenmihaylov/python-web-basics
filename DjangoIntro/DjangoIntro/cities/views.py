from django.shortcuts import render

from DjangoIntro.cities.models import Person


def index(req):
    context = {
        'name': 'Milen',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
