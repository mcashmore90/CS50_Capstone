import requests
from ..data.dtos import PokemonDto, TypeDto, StatDto, MoveDto, PokemonListDto
from decimal import Decimal

class ApiService:
    api_url = "https://pokeapi.co/api/v2/"
    
    def GetPokemon(limit, offset):
        request = requests.get(f"{ApiService.api_url}pokemon?limit={limit}&offset={offset}")
        if request.status_code == 200:
            response = request.json()
            pokemonList = []
            for result in response["results"]:
                pokemonList.append(PokemonListDto(
                    name = result["name"].replace('-', ' ').upper()
                ))
            return pokemonList
        
        
    def GetPokemonByName(name):
        request = requests.get(f"{ApiService.api_url}pokemon/{name}")
        if request.status_code == 200:
            response = request.json()
            
            stats = ApiService.GetStats(response["stats"])
            moves_list = ApiService.GetMoves(response["moves"])
            types_list = []
            for type in response["types"]:
                types_list.append(ApiService.GetType(type["type"]["url"]))
            description = ApiService.GetDescription(response["species"]["url"])

            pokemon= PokemonDto(
                image = response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                name = response["name"].replace('-', ' ').upper(),
                number = response["id"],
                height= str((Decimal(response["height"]) * Decimal(0.1)).quantize(Decimal('0.01'))),
                weight= str((Decimal(response["weight"]) * Decimal(0.1)).quantize(Decimal('0.01'))),
                description = description,
                stat = stats,
                moves=moves_list,
                types = types_list
            )
            
            return pokemon
            
        else: 
            return None

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
                    name = data["name"].replace('-', ' ').upper(),
                    power = data["power"],
                    description = data["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' ').upper(),
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
            return TypeDto(name=response["name"], image = response["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"])
        
    def GetDescription(url):
        print(url)
        request = requests.get(url)
        if request.status_code == 200:
            data = request.json()
            desc = next((entry['flavor_text'] for entry in data["flavor_text_entries"] if entry['version']['name'] == 'yellow'), "").replace('\n', ' ').replace('\f', ' ').upper()
            return desc
            
        else:
            return None