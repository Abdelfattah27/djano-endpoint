from xml.etree.ElementInclude import include
from django.urls import path 
from .views import CRUDStudents , CRUDStudent
from django.views.generic import TemplateView

urlpatterns = [
    path("" , CRUDStudents.as_view() ) , 
    path("<int:id>" , CRUDStudent.as_view())
   # path("<int:id>" , update_delete)
]
