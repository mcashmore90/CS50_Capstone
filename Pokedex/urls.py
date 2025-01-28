from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getlist", views.getPokemons, name="pokemons"),
    path("pokemon/<str:name>/", views.getPokemonbyUrl, name="pokemonurl")
]
