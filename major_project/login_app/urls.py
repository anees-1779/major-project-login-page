from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Login page
    path('submit/', views.submit, name='submit'),  # Form submission handler
    path('home/', views.home, name='home'),# Home page after login
    path('logout/',views.logout, name = 'logout')
]
