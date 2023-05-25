from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('faf/',faf,name='faf'),
]