from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('detail', views.detail, name='detail'),
]