import requests
from ..data.dtos import PokemonDto, TypeDto, StatDto, MoveDto, PokemonListDto


class ApiService:
    api_url = "https://pokeapi.co/api/v2/"
    limit = 5
    
    def GetPokemons():
        request = requests.get(f"{ApiService.api_url}pokemon?limit={ApiService.limit}&offset=6")
        if request.status_code == 200:
            response = request.json()
            pokemonList = []
            for result in response["results"]:
                pokemonList.append(PokemonListDto(
                    name = result["name"],
                    url = result["url"]
                ))
            return pokemonList
    
    @staticmethod
    def GetPokemonById(id): #will have to change this to GetPokemonUrl. The URL is already provided in the list display.
        request = requests.get(F"{ApiService.api_url}pokemon/{id}/")
        if request.status_code == 200:
            response = request.json()
            
            stats = ApiService.GetStats(response["stats"])
            moves_list = ApiService.GetMoves(response["moves"])
            types_list = []
            for type in response["types"]:
                types_list.append(ApiService.GetType(type["type"]["url"]))
            
            pokemon= PokemonDto(
                image = response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                name = response["name"],
                number = response["id"],
                stat = stats,
                moves=moves_list,
                types = types_list
            )
            return pokemon
            
        else: 
            return None
    
      
    @staticmethod    
    def GetStats(stats):
        currentStats = StatDto()
   
        for stat in stats:
            if stat['stat']['name'] == "hp":
                currentStats.health = stat["base_stat"]
            if stat['stat']['name'] == "attack":
                currentStats.attack = stat["base_stat"]                 
            if stat['stat']['name'] == "defense":
                currentStats.defence = stat["base_stat"]               
            if stat['stat']['name'] == "special-attack":
                currentStats.sp_attack = stat["base_stat"]                 
            if stat['stat']['name'] == "special-defense":
                currentStats.sp_defence = stat["base_stat"]                    
            if stat['stat']['name'] == "speed":
                currentStats.speed = stat["base_stat"]                
        return currentStats
    
    @staticmethod
    def GetMoves(moves):
        move_urls = [move['move']['url'] for move in moves 
                          if any( version_group['version_group']['name'] 
                        in [ 'red-blue','yellow']and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'] )]        
        moves = []
        for url in move_urls:
            request = requests.get(url)
            if request.status_code == 200:
                data = request.json()
                moves.append(MoveDto(
                    name = data["name"],
                    power = data["power"],
                    description = data["effect_entries"][0]["short_effect"],
                    accuracy = data["accuracy"],
                    pp = data["pp"],
                    type= ApiService.GetType(data["type"]["url"])
                ))
            else:
                return None
        return moves
    
    def GetType(url):
        request = requests.get(url)
        if request.status_code == 200:
            response = request.json()
            return TypeDto(name=response["name"], image = response["sprites"]["generation-iii"]["emerald"]["name_icon"])
        
        