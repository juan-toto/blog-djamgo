from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post, name='post'),
    path('datos', views.datos, name='datos'),
    path('autor', views.autor, name='autor'),
    path('categoria', views.categoria, name='categoria'),
]