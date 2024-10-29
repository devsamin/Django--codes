from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('delete/<int:roll>', views.delete_data, name="del_st_data"),
]