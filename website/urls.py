from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home page"),
    path('add', views.add, name="add"),
    path('subtract.html', views.subtract, name="subtract"),
    path('multiple.html', views.multiple, name="multiple"),
    path('divide.html', views.divide, name="divide"),
]
