import requests
from .models import Pokemon, Stats,Move,Type


class ApiService:
    def __init__(self):
        self.api_url = "https://pokeapi.co/api/v2/"
        
#https://pokeapi.co/api/v2/pokemon/1
#https://pokeapi.co/api/v2/pokemon/1

    def GetPokemon(self):
        response = requests.get(self.api_url+"pokemon/1/")
        if response.status_code == 200:
            data = response.json()
            return Pokemon(
                name = data["name"],
                number = data["id"],
                picture = data["sprites"]["versions"]["generation-i"]["red-blue"]["front_default"]
            )
            
        else: 
            return None
        
        
    def GetStats(self):
        
        response = requests.get(self.api_url+"pokemon/1/")
        if response.status_code == 200:
            data = response.json()
            currentStats = Stats()
            for stat in data["stats"]:
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
    
    
    def GetMoves(self):
        response = requests.get(self.api_url+"pokemon/1/")
        if response.status_code==200:
            data = response.json()
            move_urls = [move['move']['url'] for move in data["moves"] 
                          if any( version_group['version_group']['name'] 
                        in ['red-blue', 'yellow']and version_group['level_learned_at'] == 0 for version_group in move['version_group_details'] )]
            
            moves = []
            for url in move_urls:
                move = requests.get(url)
                if move.status_code ==200:
                   
                    moves.append(Move(
                        name = move.json()["name"],
                        power = move.json()["power"],
                        description = move.json()["effect_entries"][0]["short_effect"],
                        accuracy = move.json()["accuracy"],
                        pp = move.json()["pp"]
                    ))
            
            print(moves)
        return moves