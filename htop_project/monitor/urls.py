from django.urls import path
from .views import system_info, index  # Import index view

urlpatterns = [
    path("", index, name="index"),  # Set index as default page for /htop/
    path("system_info/", system_info, name="system_info"),
]
