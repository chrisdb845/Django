
from django.contrib import admin
from django.urls import path
from cartapp import views
urlpatterns = [

    path('home/', views.index),
    path('gallery/', views.gallery),
]


