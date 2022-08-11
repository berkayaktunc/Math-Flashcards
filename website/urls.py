from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('subtract', views.subtract, name="subtract"),
    path('multiple', views.multiple, name="multiple"),
    path('divide', views.divide, name="divide"),
]
