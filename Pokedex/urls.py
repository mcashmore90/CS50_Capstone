from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon", views.pokemon, name="pokemon"),
    path("pokemon/<int:id>/", views.pokemon_details, name="pokemon_details")
]
