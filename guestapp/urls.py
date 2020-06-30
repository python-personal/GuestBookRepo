from django.contrib import admin
from django.urls import path
from guestapp import views
urlpatterns = [
    path('home/',views.HomeView,name='home'),
    path('create/',views.createView,name='create'),
]
