from django.conf.urls import url
from . import views
from django.urls import path
from ScrimPay.views import ItemCreateView

urlpatterns = [
    
    path('',ItemCreateView.as_view()),
    path('main', views.main, name='main'),
    path('detail', views.detail, name='detail'),
    path('rod', views.rod, name='rod'),
    path('search',views.SearchCriteria,name='search'),
    path('support', views.support, name='support'),
]