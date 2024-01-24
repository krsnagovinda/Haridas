from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),   
    path('servicios/', views.services, name='services'),
    path('portafolio/', views.portfolio, name='portfolio'),
    
    ]
