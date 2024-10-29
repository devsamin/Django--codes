
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    # path('coures/',views.coures )
    path('coures',views.courses),
    path('about',views.about),
    path('',views.home)
    
]