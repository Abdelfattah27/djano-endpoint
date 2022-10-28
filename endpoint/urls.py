"""endpoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task6 API",
      default_version='v1',
      description="two end points parent and student used the authentication and permissions, it an application of what we learned in authentications and permissions,  first for go to our system we should register as student or parent in /register/ end point with post request then we can login with the email and password we have registered, after login th authentication key will get back to you then you must save it in headers of any request you will call in headers with name 'Authorization' then you can make CRUD operation in your data based on the http method you call and you can read also your related data of children if you are the parent and your parent if you login as student",
      #terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Abdelfattah.hamdy234@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("student.urls")) , 
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc') ,

]
