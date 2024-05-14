# jhj0510/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jhjlist/', include('jhjlist.urls')),
]
