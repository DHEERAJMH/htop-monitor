from django.urls import path
from .views import system_info

urlpatterns = [
    path('', system_info, name='system_info'),
]
