from django.contrib import admin
from django.urls import path, include
from DjangoIntro.cities.views import index, list_phones, test_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('test/', test_index),
    path('cities/', include('DjangoIntro.cities.urls')),
    path('', include('DjangoIntro.people.urls'))
]
