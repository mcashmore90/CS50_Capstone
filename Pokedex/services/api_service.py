import requests
from ..models import Type, Stat, Move, Pokemon
from decimal import Decimal
from datetime import datetime
import asyncio
import aiohttp
from asgiref.sync import sync_to_async

class ApiService:  
    
    types_dict ={}
    moves_dict ={}
    pokemons_dict ={}
    
    @classmethod
    async def SeedData(cls):
        start = datetime.now()
        
        types = await sync_to_async(lambda: list(Type.objects.all()))()
        cls.types_dict = {t.name: t for t in types}
        
        moves = await sync_to_async(lambda: list(Move.objects.all()))()
        cls.moves_dict = {m.name: m for m in moves}
        
        pokemons = await sync_to_async(lambda: list(Pokemon.objects.all()))()
        cls.pokemons_dict = {p.name: p for p in pokemons}
    
        #print(types_dict)
        
        #try:
        async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon?limit=6") as request:
                    response = await request.json()
                    tasks = [ApiService.CheckData(result["url"], session) for result in response["results"]]
                    await asyncio.gather(*tasks)
                    #ApiService.CreatePokemon(pokemon)
        # except Exception:
        #     print(f'ERROR ON SEED DATA')
        # finally:
        end = datetime.now()
        print(f"Seed complete in....{end-start}")
    @classmethod
    async def CheckData(cls, url, session):  
        async with session.get(url) as request:
            pokemonData = await request.json()
            print(f'===CHECKING DATA FOR: {pokemonData["name"].upper()}===')
            #searchPokemon = await sync_to_async(Pokemon.objects.filter(name = pokemonData["name"].replace('-',' ')).first)()
            searchType,searchMove = await asyncio.gather(
             asyncio.gather(*[ApiService.CheckType(type["type"], session) for type in pokemonData["types"]]),
             ApiService.CheckMoves(pokemonData["moves"], session),
            )

        print(f'===COMPLETED DATA FOR: {pokemonData["name"].upper()}===')
            
    @classmethod        
    async def CheckType(cls, type, session) :
        
        print(f'===CHECKING FOR TYPE: {type["name"].upper()}===')
        searchType = cls.types_dict.get(type["name"])
        
        if searchType is None:
            print(f'===ADDING NEW TYPE: {type["name"].upper()}===')    
            async with session.get(type["url"]) as request:
                typeData = await request.json()
                searchType = Type(
                    typeId=typeData["id"],
                    name=typeData["name"],
                    image=typeData["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
                )
                
                
                async with cls.type_lock:
                    cls.types_dict[type["name"]] = searchType
                    await sync_to_async(searchType.save)()
            print(f'===RETURNING TYPE: {type["name"].upper()}===')         
            return searchType
        
    @classmethod    
    async def CheckMoves(cls, moves, session):
        
        #===INNER FUNCTION===
        async def GetMoveData(move, session):
            
            print(f'===CHECKING FOR MOVE: {move["name"].upper()}===')
            searchMove = cls.moves_dict.get(move["name"])
            
            if searchMove is None:
                print(f'===ADDING NEW MOVE: {move["name"].upper()}===')
                async with session.get(move["url"]) as request:
                    moveData = await request.json()
                    
                    moveType = await ApiService.CheckType(moveData["type"], session)
                
                    searchMove = Move(
                        moveId=moveData["id"],
                        name=moveData["name"],
                        description=moveData["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' '),
                        accuracy=moveData["accuracy"],
                        power=moveData["power"],
                        pp=moveData["pp"],
                        type=moveType
                    )
                    
                async with cls.move_lock:
                    cls.moves_dict[move["name"]] = searchMove
                    await sync_to_async(searchMove.save)()
                    
                await sync_to_async(lambda:searchMove.type)()
            #else:
                # Ensure the related 'type' field is loaded
                #await sync_to_async(lambda:searchMove.type)()
            
            print(f'===RETURNING MOVE: {searchMove}===') 
            return searchMove        
        #===INNER FUNCTION===
        
        #filters the proper moves
        move_urls = [move['move'] for move in moves 
                    if any(version_group['version_group']['name'] == 'yellow' and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'])] 
        
        #Gets the details for filtered moves
        moveTasks = [GetMoveData(move, session) for move in move_urls]
        moveSet = await asyncio.gather(*moveTasks)

        return moveSet
        
    #====================   
    #     print(f'SEARCHING {result["name"]}')
    #     pokemonSearch = await sync_to_async(Pokemon.objects.filter(name=result["name"].replace('-', ' ')).first)()

    #     if pokemonSearch is None:
    #         pokemonSearch = await ApiService.CreatePokemon(result["url"], session)
        
    #         #print(f'IN DATABASE {pokemonSearch}')
  
    # async def CreatePokemon(url,session):
    #     #try:
    #         async with session.get(url) as request:
    #             pokemonItem = await request.json()
                
    #             taskTypes = [ApiService.GetType(type["type"], session) for type in pokemonItem["types"]]
    #             types = await asyncio.gather(*taskTypes)
    #             print(types)
                
                
    #             print(f'CREATING {pokemonItem["name"]}')
    #             newPokemon = Pokemon(
    #                 pokemonId = pokemonItem["id"],
    #                 name = pokemonItem["name"].replace('-', ' '),
    #                 image = pokemonItem["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
    #                 height= round(Decimal(pokemonItem["height"]) * Decimal(0.1),2),
    #                 weight= round(Decimal(pokemonItem["weight"]) * Decimal(0.1),2),
    #                 description = "description",
    #             )
    #             #await sync_to_async(newPokemon.save)()
    #             return newPokemon
    #     # except Exception as e:
    #     #     print(f'ERROR CREATING {result["name"]} ERROR: {e}')
    #     #     return
        
    # async def GetType(type, session):
    #     print("getting type")
    #     return type["name"]
    
    # async def CreateType(type, session):
    #     return    
        
    #==========================================================
    #==========================================================
    #     print(f'creating new pokemon: {url["name"]}')
    #     request = requests.get(url["url"])
    #     response = request.json()
            
    #     moves = ApiService.GetMoves(response["moves"])           
    #     description = ApiService.GetDescription(response["species"])
    #     print(f'printing descript {description}')

    #     types = []
    #     for type in response["types"]:
    #         print(type["type"])
    #         types.append(ApiService.GetType(type["type"]))
            
    #     if pokemonSearch is None:    
    #         newPokemon = Pokemon(
    #             pokemonId = response["id"],
    #             name = response["name"].replace('-', ' '),
    #             image = response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
    #             height= round(Decimal(response["height"]) * Decimal(0.1),2),
    #             weight= round(Decimal(response["weight"]) * Decimal(0.1),2),
    #             description = description,
    #         )
    #         newPokemon.save()
    #         newPokemon.moves.add(*moves)
    #         newPokemon.types.add(*types)
            
    #         ApiService.GetStats(response["stats"], newPokemon)
            
    #         print(f'New pokemon created: {newPokemon}')
    #     else:
    #         missing_moves = set(moves) - set(pokemonSearch.moves.all())
    #         missing_types = set(types) - set(pokemonSearch.types.all())

    #         if missing_moves:
    #             pokemonSearch.moves.set(missing_moves)
    #             pokemonSearch.save()
    #             print(f'added moves {list(pokemonSearch.moves.all())} to {pokemonSearch}')
                
    #         if missing_types:
    #             pokemonSearch.types.set(missing_types)
    #             pokemonSearch.save()
    #             print(f'added types {list(pokemonSearch.types.all())} to {pokemonSearch}')
    #         print(f'returning {pokemonSearch}')
            
  
    # def GetStats(stats, newPokemon):
    #     searchStats = Stat.objects.filter(pokemon = newPokemon).first()
    #     if searchStats is None:
    #         print(f"Adding Stats")
    #         newStat = Stat(
    #         health=stats[0]["base_stat"],
    #         attack=stats[1]["base_stat"],
    #         defence=stats[2]["base_stat"],
    #         sp_attack=stats[3]["base_stat"],
    #         sp_defence=stats[4]["base_stat"],
    #         speed=stats[5]["base_stat"],
    #         pokemon=newPokemon
    #     )
    #         newStat.save()
        
    #     print("Stats applied")
        
    
    # def GetMoves(moves):
    #     print(f"Organizing moves")
        # move_urls = [move['move'] for move in moves 
        #                   if any( version_group['version_group']['name'] 
        #                 in [ 'red-blue','yellow']and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'] )]        
       
    #     print(f'Moves organized...')
    #     moveDetails=[]
    #     for move in move_urls:
    #         moveDetails.append(ApiService.GetMoveDetail(move))
    #     return moveDetails
        
    
    # def GetDescription(url):
    #     print("getting description")
    #     request = requests.get(url["url"])
    #     if request.status_code == 200:
    #         data = request.json()
    #         for entry in data['flavor_text_entries']:
    #             if entry['version']['name'] == "yellow" and entry['language']['name'] == "en":
    #                 return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
    #     else:
    #         return ""
        

    # def GetType(type):  
    #     print(f'getting tpye: {type["name"]}') 
    #     searchType = Type.objects.filter(name=type["name"]).first()
    #     if searchType is None:
    #         print(f'Adding new type: {type["name"]}')
    #         request = requests.get(type["url"])
    #         result = request.json()
            
    #         newType = Type(
    #             typeId=result["id"],
    #             name = result["name"],
    #             image = result["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
    #         )
    #         newType.save()
    #         print(f"added new type: {newType}")
    #         return newType         
    #     else:
    #         print(f"returning type: {searchType}")
    #         return searchType   
    
    # def GetMoveDetail(move):
    #     searchMove = Move.objects.filter(name = move["name"]).first()
    #     if searchMove is None:
    #         print(f'Adding new Move: {move["name"]}')
    #         request = requests.get(move["url"])
    #         response = request.json()
            
    #         moveType = ApiService.GetType(response["type"])
            
    #         newMove = Move(
    #             moveId = response["id"],
    #             name = response["name"],
    #             description = response["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' '),
    #             accuracy = response["accuracy"],
    #             power = response["power"],
    #             pp = response["pp"],
    #             type = moveType
    #         )
    #         newMove.save()
    #         print(f'New move added: {newMove}')
    #         return newMove
    #     else:
    #         if searchMove.type is None:
    #             searchMove.type = ApiService.GetType(response["type"])
    #             searchMove.save()
    #             print(f'added type to {searchMove}')
    #         print(f'returning Move: {searchMove}')
    #         return searchMove
    