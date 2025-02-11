from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .models import Type, Stat, Move, Pokemon, PokemonSerializer
from .services.api_service import ApiService
import json
from django.core.paginator import Paginator

offset = 0
limit = 6
maxPokemonCount = 151

def index(request):
    ApiService.SeedData()
    
    # pokemon = Pokemon.objects.get(name="MEWTWO")
    

    # print(pokemon.moves.all())
    
    
    return render(request, "pokedex/index.html")

def pokemon(request):
    #pokemonData = ApiService.GetPokemon(limit, offset)
    #note - list splicing [start:end]
    # Retrieve Pokemon along with their related moves and types

    # pokemon = Pokemon.objects.all()
    # pokemonList =[]
    # for p in pokemon:
    #     print(p)
    #     poke = PokemonSerializer(p)
    #     pokemonList.append(poke.data)

    pokemons = Pokemon.objects.all().order_by('pokemonId')
    pokemons = Paginator(pokemons, limit)
    
    page_number = request.GET.get('page')
    if page_number is None or "":
        page_number = 1
    pokemonPage = pokemons.get_page(page_number)
    
    # print(pokemonPage)
    # print(f"has next page {pokemonPage.has_next() or None}")
    # print(f"next page number { pokemonPage.next_page_number() if pokemonPage.has_next() else 0}")
    # print(f"has previous {pokemonPage.has_previous() or None}")
    # print(f"previous page number {pokemonPage.previous_page_number() if pokemonPage.has_previous() else 0}")
    # print(f"page number {pokemonPage.number}")
    # print(f"object list {pokemonPage.object_list}")

    pokemonList=[]
    for pokemon in pokemonPage.object_list:
        pokemonList.append({
            "pokemonName": pokemon.name,
            "pokemonId":pokemon.pokemonId
        })
    #print(pokemonList)
    
    
    pokeData={
        "hasNext":pokemonPage.has_next() or None,
        "hasPrevious":pokemonPage.has_previous()or None,
        "nextPageNumber": pokemonPage.next_page_number() if pokemonPage.has_next() else 0,
        "previousPageNumber":pokemonPage.previous_page_number() if pokemonPage.has_previous() else 0,
        "pokemon":pokemonList
    }

    # pokemon = Pokemon.objects.get(pokemonId=150)
    # serializer = PokemonSerializer(pokemon)
    # print(serializer.data)
    
    
    
    
    # Loop through moves to access related types and abilities
    # for move in pokemon.moves.all():
    #    for type in move.type.all():
    #        print(f"{move.name} {type.name}")
    # for poke in pokemonData:
    #     types = poke.types.all()
    #     print(types)
    #     moves = poke.moves.all()
    #     print(moves)
    #     stat = poke.stat
    #     print(stat)
    
    
    #page_number = request.GET.get('page')
    # if page_number is None or "":
    #     page_number = 1

    
  
    return JsonResponse({"data":pokeData}, safe=False)

def pokemon_details(request, id):
    
    pokemon = Pokemon.objects.get(pokemonId = id)
    stats = Stat.objects.get(pokemon = pokemon)
    moves = Move.objects.select_related('type').filter(pokemon = pokemon)
    for move in moves:
        print(move)
    
    print(moves[0].type.name)
    print(pokemon)
    print(stats)

    return JsonResponse({"pokemon":[]},safe=False)

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
