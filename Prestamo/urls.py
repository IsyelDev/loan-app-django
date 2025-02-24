from django.urls import path

from . import views


urlpatterns = [
    path("bienvenido/", views.Bienvenido, name="bienvenido"),
    path("about/", views.About, name="about")
]
