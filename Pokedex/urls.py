from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon", views.pokemon, name="pokemon"),
    path("pokemon-next", views.pokemon_next, name="pokemon_next"),
    path("pokemon-previous", views.pokemon_previous, name="pokemon_previous"),
    path("pokemon/<str:name>/", views.pokemon_details, name="pokemon_details")
]
