from django.urls import path
from .views import *


urlpatterns = [
    path("form/",Form.as_view(),name="form"),
    path("",LoginView.as_view(),name="login"),
    path("register/",Register.as_view(),name="register"),
    path("home/",Home.as_view(),name="home"),
    path("logout/",logoutView,name="logout"),
    path("template1/",TemplateView.as_view(),name="template1"),
    path("template2/",TemplateView2.as_view(),name="template2"),
    path("template3/",TemplateView3.as_view(),name="template3"),
    path("all-templates/",AllTemplate.as_view(),name="all-templates"),
]



