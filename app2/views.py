from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return HttpResponse('<h1>msd is best batsmen</h1>')
def faf(request):
    return HttpResponse('<h1> best player</h1>')