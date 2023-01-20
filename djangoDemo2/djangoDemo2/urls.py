from django.contrib import admin
from django.urls import path, include

from djangoDemo2.towns.views import index

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index),
	path('towns/', include('djangoDemo2.towns.urls'))
]
