from django.urls import path
from . import views

urlpatterns = [
    path('backup_switch/<int:pk>/', views.backup_switch, name='backup_switch'),
    path('restore_switch/<int:pk>/', views.restore_switch, name='restore_switch'),
]
