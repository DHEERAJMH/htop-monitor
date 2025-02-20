from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', include('monitor.urls')),
    path('', lambda request: redirect('/htop/')),  # Redirect root to /htop/
]
