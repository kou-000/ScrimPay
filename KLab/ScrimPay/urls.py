from django.conf.urls import url
from . import views
from django.urls import path
from ScrimPay.views import ItemCreateView

urlpatterns = [
    
    path('',ItemCreateView.as_view()),
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    # path('/create/main', views.main, name='main'),
    path('detail', views.detail, name='detail'),
    
]