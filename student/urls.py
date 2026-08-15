from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("list/", views.list, name="list"),
    path("base/", views.base, name="base"),
    path("model/", views.model, name="model"),
    path("students/", views.student_list, name="student_list"),
    path("create/", views.student_create, name="student_create"),
#create vanelo page hera browser ko lagi,secondly student_create vaneko function call garxa views.py bata ani lastly name vaneko url ko lagi ho frontend ko lagiii.
    path("<int:student_id>/edit/", views.student_update, name="student_update"),
    path("<int:student_id>/delete/",views.student_delete,name="student-delete"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]