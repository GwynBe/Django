from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello World HttpResponse')

def new_index(request):
    return HttpResponse('123456')