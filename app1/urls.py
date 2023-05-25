
from django.urls import path
from app1.views import *

app_name='something'

urlpatterns = [
    path('virat/',virat,name='virat'),
    path('ABD/',ABD,name='ABD')
]
