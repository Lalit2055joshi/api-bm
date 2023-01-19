from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',CustomerApiView.as_view(),name='alldata')
]