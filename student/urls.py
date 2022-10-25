from xml.etree.ElementInclude import include
from django.urls import path 
from .views import CRUDStudents , CRUDStudent , CRUDParent , CRUDParents  , CRUDSubject , CRUDSubjects
from django.views.generic import TemplateView

urlpatterns = [
    path("student/" , CRUDStudents.as_view() ) , 
    path("student/<int:id>" , CRUDStudent.as_view()),
    path("parent/" , CRUDParents.as_view() ) , 
    path("parent/<int:id>" , CRUDParent.as_view()),
    path("subject/" , CRUDSubjects.as_view() ) , 
    path("subject/<int:id>" , CRUDSubject.as_view())
   # path("<int:id>" , update_delete)
]
