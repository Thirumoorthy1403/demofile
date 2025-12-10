from django.urls import path
from app2.views import *
urlpatterns=[
    path('demo/', demo),
    path('demo1/', demo1),
    path('demo2/', demo2),
    path('demo3/', demo3),
]