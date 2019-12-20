from django.conf.urls import url
from . import views
from django.urls import path
from ScrimPay.views import ItemCreateView

urlpatterns = [
    
    path('',ItemCreateView.as_view(),name = 'index'),
    path('main', views.main, name='main'),
    path('detail', views.detail, name='detail'),
    path('rod', views.rod, name='rod'),
    path('search',views.SearchCriteria,name='search'),
    path('support', views.support, name='support'),
    path('top', views.top, name='top'),
    path('deletedb', views.deletedb, name='deletedb'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]