from django.urls import  path
from . import views

app_name = "restaurant"
urlpatterns = [

    path('', views.index, name='index'),
    path('breakfast', views.breakfast, name='breakfast'),
    path('Breakfast', views.breakfast, name='breakfast'),


]
