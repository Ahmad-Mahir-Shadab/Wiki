from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:filename>", views.filename, name="filename"),
    path("Form", views.form, name="form"),
    path("Create", views.create, name="create"),
    path("wiki/<str:filename>/Edit", views.edit, name="edit"),
    path("Random", views.random, name="random")
]