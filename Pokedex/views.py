from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .services.api_service import ApiService
import json

offset = 0
limit = 6
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
        print("at limit")
        offset = maxPokemonCount - limit
    else:
        print("next")
        offset = offset+limit
    print(F"condition {offset + limit > maxPokemonCount}")
    print(f"offset {offset}")
    print(f"limit {limit}")
    print(f"limit and offset {offset + limit }")
     
    pokemonData = ApiService.GetPokemon(limit, offset)
    pokemonList = [pokemon.to_dict() for pokemon in pokemonData]
    
    return JsonResponse({"pokemon":pokemonList}, safe=False)

def pokemon_previous(request):
    global offset
    global limit
    global maxPokemonCount
    if offset - limit < 0:
        offset = 0
    else:
        offset = offset - limit
        
    pokemonData = ApiService.GetPokemon(limit, offset)
    pokemonList = [pokemon.to_dict() for pokemon in pokemonData]
    
    return JsonResponse({"pokemon":pokemonList}, safe=False)
    
# def index(request):
    
#     pokemonList = ApiService.GetPokemon()
#     print(pokemonList)
   
#     return render(request, "pokedex/index.html",{"poke":poke, "pokemonlist":pokemonList, })


# def getPokemons(request):
#     pokemonlist = ApiService.GetPokemons()
    
#     pokemonData = [pokemon.to_dict() for pokemon in pokemonlist]
    
#     return JsonResponse({"newList":pokemonData},safe=False)

# def getPokemonbyUrl(request, name):
#     print("At url")
#     poke = ApiService.getPokemonByUrl(name)
    
#     return JsonResponse({"pokemon":poke.to_dic()},safe=False)