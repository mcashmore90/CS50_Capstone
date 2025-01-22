from django.shortcuts import render

from .service import ApiService
apiService = ApiService()


def index(request):
    
    poke = apiService.GetPokemon()
    stats = apiService.GetStats()
    moves = apiService.GetMoves()
    return render(request, "pokedex/index.html",{"poke":poke, "stats":stats, "moves":moves})