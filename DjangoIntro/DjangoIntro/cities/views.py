from django.http import HttpResponse
from django.shortcuts import render

from DjangoIntro.cities.models import Person


def index(req):
    context = {
        'name': 'Milen',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_phones(request):
    # return HttpResponse('Phones list')
    return render(request, 'phones.html')
