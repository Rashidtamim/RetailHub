from django.urls import path

from home.views import *

urlpatterns = [
  path('', home ,name = 'home'),
  path('dashboard/', home2 ,name = 'home2'),
]