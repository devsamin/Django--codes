from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('passchange/', views.change_pass, name='passchange'),
    path('passchange2/', views.change_pass2, name='passchange2'),
]
