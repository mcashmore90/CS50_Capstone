import requests
from ..models import Type, Stat, Move, Pokemon
from decimal import Decimal
from datetime import datetime
import asyncio

class ApiService:  
    
    def SeedData():
        start = datetime.now()
        request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
        response = request.json()
        for pokemon in response["results"]:
            ApiService.CreatePokemon(pokemon)

        end = datetime.now()
        print(f"Seed complete in....{end-start}")
  
  
    def CreatePokemon(url):     
        pokemonSearch = Pokemon.objects.filter(name=url["name"].replace('-', ' ')).first()
        
        print(f'creating new pokemon: {url["name"]}')
        request = requests.get(url["url"])
        response = request.json()
            
        moves = ApiService.GetMoves(response["moves"])           
        description = ApiService.GetDescription(response["species"])
        print(f'printing descript {description}')

        types = []
        for type in response["types"]:
            print(type["type"])
            types.append(ApiService.GetType(type["type"]))
            
        if pokemonSearch is None:    
            newPokemon = Pokemon(
                pokemonId = response["id"],
                name = response["name"].replace('-', ' '),
                image = response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                height= round(Decimal(response["height"]) * Decimal(0.1),2),
                weight= round(Decimal(response["weight"]) * Decimal(0.1),2),
                description = description,
            )
            newPokemon.save()
            newPokemon.moves.add(*moves)
            newPokemon.types.add(*types)
            
            ApiService.GetStats(response["stats"], newPokemon)
            
            print(f'New pokemon created: {newPokemon}')
        else:
            missing_moves = set(moves) - set(pokemonSearch.moves.all())
            missing_types = set(types) - set(pokemonSearch.types.all())

            if missing_moves:
                pokemonSearch.moves.set(missing_moves)
                pokemonSearch.save()
                print(f'added moves {list(pokemonSearch.moves.all())} to {pokemonSearch}')
                
            if missing_types:
                pokemonSearch.types.set(missing_types)
                pokemonSearch.save()
                print(f'added types {list(pokemonSearch.types.all())} to {pokemonSearch}')
            print(f'returning {pokemonSearch}')
            
  
    def GetStats(stats, newPokemon):
        searchStats = Stat.objects.filter(pokemon = newPokemon).first()
        if searchStats is None:
            print(f"Adding Stats")
            newStat = Stat(
            health=stats[0]["base_stat"],
            attack=stats[1]["base_stat"],
            defence=stats[2]["base_stat"],
            sp_attack=stats[3]["base_stat"],
            sp_defence=stats[4]["base_stat"],
            speed=stats[5]["base_stat"],
            pokemon=newPokemon
        )
            newStat.save()
        
        print("Stats applied")
        
    
    def GetMoves(moves):
        print(f"Organizing moves")
        move_urls = [move['move'] for move in moves 
                          if any( version_group['version_group']['name'] 
                        in [ 'red-blue','yellow']and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'] )]        
       
        print(f'Moves organized...')
        moveDetails=[]
        for move in move_urls:
            moveDetails.append(ApiService.GetMoveDetail(move))
        return moveDetails
        
    
    def GetDescription(url):
        print("getting description")
        request = requests.get(url["url"])
        if request.status_code == 200:
            data = request.json()
            for entry in data['flavor_text_entries']:
                if entry['version']['name'] == "yellow" and entry['language']['name'] == "en":
                    return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
        else:
            return ""
        

    def GetType(type):  
        print(f'getting tpye: {type["name"]}') 
        searchType = Type.objects.filter(name=type["name"]).first()
        if searchType is None:
            print(f'Adding new type: {type["name"]}')
            request = requests.get(type["url"])
            result = request.json()
            
            newType = Type(
                typeId=result["id"],
                name = result["name"],
                image = result["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
            )
            newType.save()
            print(f"added new type: {newType}")
            return newType         
        else:
            print(f"returning type: {searchType}")
            return searchType   
    
    def GetMoveDetail(move):
        searchMove = Move.objects.filter(name = move["name"]).first()
        if searchMove is None:
            print(f'Adding new Move: {move["name"]}')
            request = requests.get(move["url"])
            response = request.json()
            
            moveType = ApiService.GetType(response["type"])
            
            newMove = Move(
                moveId = response["id"],
                name = response["name"],
                description = response["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' '),
                accuracy = response["accuracy"],
                power = response["power"],
                pp = response["pp"],
                type = moveType
            )
            newMove.save()
            print(f'New move added: {newMove}')
            return newMove
        else:
            if searchMove.type is None:
                searchMove.type = ApiService.GetType(response["type"])
                searchMove.save()
                print(f'added type to {searchMove}')
            print(f'returning Move: {searchMove}')
            return searchMove
    