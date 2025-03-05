from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
from .services.api_service import ApiService
import asyncio


def index(request):    
    return render(request, "index.html")

def pokemon(request):
    asyncio.run(ApiService.SeedData())

    pokemons = Pokemon.objects.all().order_by('pokemonId')

    return JsonResponse({"data":[ pokemon.to_dic_list() for pokemon in pokemons]}, safe=False)

def pokemon_details(request, id):
    
    pokemon = Pokemon.objects.prefetch_related('types','moves','moves__type').get(pokemonId = id)

    return JsonResponse({"pokemon":pokemon.to_dic()},safe=False)
