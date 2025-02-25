from django.shortcuts import render
from django.http import JsonResponse
from .models import Move, Pokemon
from .services.api_service import ApiService
from django.core.paginator import Paginator
import asyncio

limit = 6

def index(request):    
    #return render(request, "pokedex/index.html")
    print("index")
    return render(request, "index.html")

def pokemon(request):
    print("pokemon list requestsing")
    #ApiService.SeedData()
    asyncio.run(ApiService.SeedData())

    pokemons = Pokemon.objects.all().order_by('pokemonId')
    pokemons = Paginator(pokemons, limit)
    
    page_number = request.GET.get('page')
    if page_number is None or "":
        page_number = 1
    pokemonPage = pokemons.get_page(page_number)

    pokemonList=[]
    for pokemon in pokemonPage.object_list:
        pokemonList.append({
            "pokemonName": pokemon.name,
            "pokemonId":pokemon.pokemonId
        })
    
    
    pokeData={
        "hasNext":pokemonPage.has_next() or None,
        "hasPrevious":pokemonPage.has_previous()or None,
        "nextPageNumber": pokemonPage.next_page_number() if pokemonPage.has_next() else 0,
        "previousPageNumber":pokemonPage.previous_page_number() if pokemonPage.has_previous() else 0,
        "pokemon":pokemonList
    }
    return JsonResponse({"data":pokeData}, safe=False)

def pokemon_details(request, id):
    
    pokemon = Pokemon.objects.prefetch_related('types','moves','moves__type').get(pokemonId = id)

    return JsonResponse({"pokemon":pokemon.to_dic()},safe=False)
