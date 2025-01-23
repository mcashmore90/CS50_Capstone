from django.shortcuts import render

from .services.api_service import ApiService


def index(request):
    
    poke = ApiService.GetPokemonById(1)
    pokemonList = ApiService.GetPokemons()
    return render(request, "pokedex/index.html",{"poke":poke, "list":pokemonList})