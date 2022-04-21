from django.contrib import admin
from django.urls import path
from .views import index, new_index
urlpatterns = [
    path('', index, name='index'),
    path('name', new_index, name='index_2'),
]
