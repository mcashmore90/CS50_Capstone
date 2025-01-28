from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .services.api_service import ApiService
import json

selectIndex = 0
offset = 0
limit = 6
pokemonCount=0

def index(request):
    
    poke = ApiService.GetPokemonById(1)
    pokemonList = ApiService.GetPokemons()
    print(pokemonList)
   
    return render(request, "pokedex/index.html",{"poke":poke, "pokemonlist":pokemonList, })


def getPokemons(request):
    pokemonlist = ApiService.GetPokemons()
    
    pokemonData = [pokemon.to_dict() for pokemon in pokemonlist]
    
    return JsonResponse({"newList":pokemonData},safe=False)

def getPokemonbyUrl(request, name):
    print("At url")
    poke = ApiService.getPokemonByUrl(name)
    
    return JsonResponse({"pokemon":poke.to_dic()},safe=False)