from django.urls import path

from . import views

urlpatterns = [
    path("",views.user, name="generic"),
    path("<str:user_name>", views.user, name="user")
]