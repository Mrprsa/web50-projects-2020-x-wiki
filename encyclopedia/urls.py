from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("newEntry", views.newEntry, name="newEntry"),
    path('edit/', views.edit, name="edit"),
    path("rand/", views.rand, name="rand"),
    path("search", views.search, name="search"),
    path("save_edit/", views.save_edit, name="save_edit"),
]
