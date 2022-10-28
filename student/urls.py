from django.urls import path  , include
from .views import ParentView, StudentLogin, StudentRegister, StudentDetailView   , ParentDetailView  ,ParentRegister , ParentLogin , StudentsView
#,  CRUDStudents , CRUDStudent , CRUDParent , CRUDParents  , CRUDSubject , CRUDSubjects

urlpatterns = [
    path("student/" , include(
        [
           path("<int:pk>" , StudentDetailView.as_view()), 
            path("register/" , StudentRegister.as_view()) , 
            path("login/" , StudentLogin.as_view() ) , 
            path("" , StudentsView.as_view())
        ]
    ) )  ,
    path("parent/" , include(
        [
            path("<int:pk>" , ParentDetailView.as_view()), 
            path("register/" , ParentRegister.as_view()) , 
            path("login/" , ParentLogin.as_view() ) , 
            path("" , ParentView.as_view())
        ]
    ) ) 


]
 