import requests
from ..models import Type, Stat, Move, Pokemon
from decimal import Decimal
from datetime import datetime
import asyncio

class ApiService:  
    
    def SeedData():
        start = datetime.now()
        pokemonCount = Pokemon.objects.count()
        if pokemonCount < 151:
            request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
            if request.status_code == 200:
                response = request.json()
                for result in response["results"]:
                    isPokemon = Pokemon.objects.filter(name=result["name"].replace('-', ' ').upper()).exists()
                    if isPokemon == False:
                       
                        ApiService.GetPokemons(result["url"])
                        print(f"adding...{result} complete")
                    
        end = datetime.now()
        print(f"Seed complete in....{end-start}")
            
    
    def GetPokemons(url):
        request = requests.get(url)
        if request.status_code == 200:
            response = request.json()
            
            description = ApiService.GetDescription(response["species"]["url"])
            moves = ApiService.GetMoves(response["moves"])
            stats = ApiService.GetStats(response["stats"])
            types=[]
            for type in response["types"]:
                newType = ApiService.GetType(type["type"])
                print(f"adding ntype: {newType}")
                types.append(newType)
                
            
            pokemon = Pokemon(
                pokemonId = response["id"],
                name = response["name"].replace('-', ' ').upper(),
                image = response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                height= Decimal(response["height"]) * Decimal(0.1),
                weight= Decimal(response["weight"]) * Decimal(0.1),
                description = description,
                stat = stats
            )
            pokemon.save()
            pokemon.moves.add(*moves)
            pokemon.types.add(*types)
  
    def GetStats(stats):
        print(f"Adding Stats")
        currentStats = Stat()
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
        currentStats.save()
        return currentStats
    
    def GetMoves(moves):
        print(f"Adding moves")
        move_urls = [move['move'] for move in moves 
                          if any( version_group['version_group']['name'] 
                        in [ 'red-blue','yellow']and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'] )]        
        moves = []
        for url in move_urls:
            print(url["name"].replace('-', ' ').upper())
            searchMove = Move.objects.filter(name=url["name"].replace('-', ' ').upper()).first()
            if searchMove == None:
                request = requests.get(url["url"])
                data = request.json()
                type = ApiService.GetType(data["type"])
                print(type)
                newMove = Move(
                    moveId = data["id"],
                    name = data["name"].replace('-', ' ').upper(),
                    power = data["power"],
                    description = data["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' ').upper(),
                    accuracy = data["accuracy"],
                    pp = data["pp"],
                    type=type
                )
                newMove.save()
                print(f"adding new move: {newMove}")
                moves.append(newMove)
            else:
                moves.append(searchMove)
        print(f"Adding moves complete.......")
        return moves
    
    
    def GetType(type):
        searchType = Type.objects.filter(name=type["name"].upper()).first()
        if searchType == None:
            print(f"Adding new....{type}")
            request = requests.get(type["url"])
            result = request.json()
            newType = Type(
                typeId=result["id"],
                name=result["name"].upper(),
                image = result["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
            ).save()
            return newType
        else:
            return searchType
        
        
    def GetDescription(url):
        print(url)
        request = requests.get(url)
        if request.status_code == 200:
            data = request.json()
            desc = next((entry['flavor_text'] for entry in data["flavor_text_entries"] if entry['version']['name'] == 'yellow'), "").replace('\n', ' ').replace('\f', ' ').upper()
            return desc
            
        else:
            return ""
        
        
    def GetPokemon(limit, offset):
        return None