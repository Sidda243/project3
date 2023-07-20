from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<li>hello i am good</li>')

def hello1(request):
    return HttpResponse('<marquee><h1>hello are you doing good?</h1></marquee>')
