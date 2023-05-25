from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse ('<h1>virat is the great batsmen</h1>')
def ABD(request):
    return HttpResponse('<h1>ABD is Mr.360</h1>')