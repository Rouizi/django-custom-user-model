# app/urls.py
from django.contrib import admin
from django.urls import path, include # Add this
from django.views.generic.base import TemplateView # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # Add this
    path('users/', include(('users.urls', 'users'), namespace='users')) # Add this
]