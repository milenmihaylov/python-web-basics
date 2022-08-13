# cities urls
from django.urls import path
from django.views.generic import TemplateView

from DjangoIntro.cities.views import list_phones, index

urlpatterns = [
    path('', index),  # /cities/
    path('phones/', list_phones),  # /cities/phones/
    path('phones2/', TemplateView.as_view(template_name='phones.html'))
]
