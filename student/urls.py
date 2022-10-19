from xml.etree.ElementInclude import include
from django.urls import path 
from .views import read_create , update_delete
urlpatterns = [
    path("" , read_create ) , 
    path("<int:id>" , update_delete)
]
