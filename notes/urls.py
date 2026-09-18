from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="notes/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("note/<int:note_id>/edit/", views.edit_note, name="edit_note"),
    path("note/<int:note_id>/delete/", views.delete_note, name="delete_note"),
    path("robots.txt", views.robots_txt, name="robots"),
]
