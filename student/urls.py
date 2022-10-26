from django.urls import path  , include
from .views import StudentView  , StudentDetailView , ParentView , ParentDetailView, SubjectView , SubjectDetailView
#,  CRUDStudents , CRUDStudent , CRUDParent , CRUDParents  , CRUDSubject , CRUDSubjects

urlpatterns = [
    path("student/" , include(
        [
            path("" , StudentView.as_view()) , 
            path("<int:id>" , StudentDetailView.as_view())
        ]
    ) )  ,
    path("parent/" , include(
        [
            path("" , ParentView.as_view()) , 
            path("<int:pk>" , ParentDetailView.as_view())
        ]
    ) )  ,
    path("subject/" , include(
        [
           path("" , SubjectView.as_view())  ,
            path("<int:pk>" , SubjectDetailView.as_view())
        ]
    ) )

]
 