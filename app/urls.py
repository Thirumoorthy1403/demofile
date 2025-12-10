from django.urls import path
from app.views import *

urlpatterns=[
    path('display/',display,name='display'),
    path('show/',show),
    path('update/<int:id>/',update,name='update'),
    path('del/<int:id>/',delete,name='delete'),
    
]