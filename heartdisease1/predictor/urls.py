from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.base,name='home'),
   path('index/',views.index,name="index"),
   path('result/',views.result,name="result")
]