from django.urls import path
from main.views import show_main, show_experience, show_projects, toggle_star
from main.views import create_project, update_project, get_projects_json, delete_project
from main.views import create_experience, update_experience, delete_experience, get_experiences_json
from main.views import register, login_user, logout_user

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<str:project_id>/delete/",delete_project, name="delete_project"),
    path("projects/<str:project_id>/edit/", update_project, name="update_project"),

    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", update_experience, name="update_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<str:project_id>/star/", toggle_star, name="toggle_star"),
    ]

