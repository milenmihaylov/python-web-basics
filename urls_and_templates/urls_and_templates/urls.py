from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_app/', include('main_app.urls')),
    path('secondary_app/', include('secondary_app.urls'))
]
