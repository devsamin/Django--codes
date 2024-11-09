from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.Register, name="register"),
    # path('login/', views.user_login, name="login"),
    path('login/', views.UserloginViews.as_view(), name="login"),
    path('profile/', views.profile, name="Profile"),
    path('logout/', views.user_logout, name="logout"),

    # path('logout/', views.UserlogoutViews.as_view(), name="logout"),
    # path('logout/', views.LogoutView.as_view(), name="logout"),

    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('profile/edit/pass_change', views.pass_change, name="pass_change"),
]