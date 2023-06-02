from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('male', views.male, name='male'),
    path('female', views.female, name='female'),
    path('gay', views.gay, name='gay'),
    path('online', views.online, name='online'),
]
