from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .services.api_service import ApiService
import json

offset = 0
limit = 5
maxPokemonCount = 151

def index(request):
    return render(request, "pokedex/index.html")

def pokemon(request):
    pokemonData = ApiService.GetPokemon(limit, offset)
    pokemonList = [pokemon.to_dict() for pokemon in pokemonData]
    return JsonResponse({"pokemon":pokemonList}, safe=False)

def pokemon_details(request, name):
    pokemon = ApiService.GetPokemonByName(name)
    return JsonResponse({"pokemon":pokemon.to_dic()},safe=False)

def pokemon_next(request):
    global offset
    global limit
    global maxPokemonCount
    
    if (offset + limit > maxPokemonCount-limit):
        offset = maxPokemonCount - limit
        index = limit - 1
    else:
        print("next")
        offset = offset+limit
        index = 0
     
    pokemonData = ApiService.GetPokemon(limit, offset)
    pokemonList = [pokemon.to_dict() for pokemon in pokemonData]
    
    return JsonResponse({"pokemon":pokemonList, "index":index}, safe=False)

def pokemon_previous(request):
    global offset
    global limit
    global maxPokemonCount
    if offset - limit < 0:
        offset = 0
        index = 0
    else:
        offset = offset - limit
        index = limit - 1
        
    pokemonData = ApiService.GetPokemon(limit, offset)
    pokemonList = [pokemon.to_dict() for pokemon in pokemonData]
    
    return JsonResponse({"pokemon":pokemonList, "index":index}, safe=False)
