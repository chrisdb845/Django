
from django.contrib import admin
from django.urls import path
from cartapp import views
urlpatterns = [

    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),

     path('services/', views.services),



]


