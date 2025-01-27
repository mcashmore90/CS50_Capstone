from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .services.api_service import ApiService
import json

selectIndex = 0

def index(request):
    
    poke = ApiService.GetPokemonById(1)
    pokemonList = ApiService.GetPokemons()
    print(pokemonList)
   
    

    return render(request, "pokedex/index.html",{"poke":poke, "pokemonlist":pokemonList, })


def updateSelection(request):
    print('at api')
    #data = json.loads(request.body)
    #post = Post.objects.get(id = data["postId"])
    data = json.loads(request.body)
    print(data)
    print(data)
    ApiService.offset+=data
    
    poke = ApiService.GetList()
    print(poke)
    pokemonData = [pokemon.to_dict() for pokemon in poke]
    # global selectIndex
    # selectIndex +=int(dir)
    # pokemonList = ApiService.GetPokemons()
    # request.session["selected"]=pokemonList[selectIndex].name
    return JsonResponse({"newList":pokemonData},safe=False)