from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yahoo', views.yahoo, name='yahoo'),
    path('tenki.jp', views.tenki_jp, name='tenki_jp'),
    path('goo', views.goo, name='goo')
]