from ..models import Type, Stat, Move, Pokemon
import aiohttp
import asyncio
from datetime import datetime
from decimal import Decimal
from asgiref.sync import sync_to_async
#Seed complete in....0:00:00.806136
class ApiService:
    
    @staticmethod
    async def SeedData():
        start = datetime.now()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://pokeapi.co/api/v2/pokemon?limit=151") as request:
                response = await request.json()
                tasks = [ApiService.CreatePokemon(session, pokemon) for pokemon in response["results"]]
                await asyncio.gather(*tasks)

        end = datetime.now()
        print(f"Seed complete in....{end-start}")

    @staticmethod
    async def CreatePokemon(session, pokemon):
        pokemonSearch = await sync_to_async(Pokemon.objects.filter(name=pokemon["name"].replace('-', ' ')).first)()
        
        print(f'creating new pokemon: {pokemon["name"]}')
        async with session.get(pokemon["url"]) as request:
            response = await request.json()
            
            # moves = await ApiService.GetMoves(session, response["moves"])
            #description = await ApiService.GetDescription(session, response["species"])
            #print(f'printing description {description}')

            types = await asyncio.gather(*[ApiService.GetType(session, type["type"]) for type in response["types"]])
            
            if pokemonSearch is None:
                newPokemon = Pokemon(
                    pokemonId=response["id"],
                    name=response["name"].replace('-', ' '),
                    image=response["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                    height=round(Decimal(response["height"]) * Decimal(0.1), 2),
                    weight=round(Decimal(response["weight"]) * Decimal(0.1), 2),
                    #description=description,
                )
                await sync_to_async(newPokemon.save())
                #await sync_to_async(newPokemon.moves.add)(*moves)
                await sync_to_async(newPokemon.types.add(*types))
                
                await ApiService.GetStats(response["stats"], newPokemon)
                
                print(f'New pokemon created: {newPokemon}')
            else:
                #missing_moves = set(moves) - set(await sync_to_async(list)(pokemonSearch.moves.all()))
                pokemonSearchTypes = await sync_to_async(list)(pokemonSearch.types.all())
                missing_types = set(types) - set(pokemonSearchTypes)

                # if missing_moves:
                #     pokemonSearch.moves.set(missing_moves)
                #     await sync_to_async(pokemonSearch.save)()
                #     print(f'added moves {list(await sync_to_async(list)(pokemonSearch.moves.all()))} to {pokemonSearch}')
                    
                if missing_types:
                    await sync_to_async(pokemonSearch.types.add)(*missing_types)
                    await sync_to_async(pokemonSearch.save)()
                    #print(f'added types {list(pokemonSearch.types.all())} to {pokemonSearch}')
                print(f'returning {pokemonSearch}')

    @staticmethod
    async def GetStats(stats, newPokemon):
        searchStats = await sync_to_async(Stat.objects.filter(pokemon=newPokemon).first)()
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
            await sync_to_async(newStat.save)()
        
        print("Stats applied")

    @staticmethod
    async def GetMoves(session, moves):
        print(f"Organizing moves")
        move_urls = [move['move'] for move in moves
                     if any(version_group['version_group']['name'] 
                            in ['red-blue', 'yellow'] and version_group['level_learned_at'] == 1 
                            for version_group in move['version_group_details'])]
        
        print(f'Moves organized...')
        moveDetails = await asyncio.gather(*[ApiService.GetMoveDetail(session, move) for move in move_urls])
        return moveDetails

    @staticmethod
    async def GetDescription(session, url):
        print("getting description")
        async with session.get(url["url"]) as request:
            if request.status_code == 200:
                data = await request.json()
                for entry in data['flavor_text_entries']:
                    if entry['version']['name'] == "yellow" and entry['language']['name'] == "en":
                        return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
            else:
                return ""

    @staticmethod
    async def GetType(session, type):
        print(f'getting type: {type["name"]}')
        searchType = await sync_to_async(Type.objects.filter(name=type["name"]).first)()
        if searchType is None:
            print(f'Adding new type: {type["name"]}')
            async with session.get(type["url"]) as request:
                result = await request.json()
                
                newType = Type(
                    typeId=result["id"],
                    name=result["name"],
                    image=result["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
                )
                await sync_to_async(newType.save)()
                print(f"added new type: {newType}")
                return newType         
        else:
            print(f"returning type: {searchType}")
            return searchType

    @staticmethod
    async def GetMoveDetail(session, move):
        searchMove = await sync_to_async(Move.objects.filter(name=move["name"]).first)()
        if searchMove is None:
            print(f'Adding new Move: {move["name"]}')
            async with session.get(move["url"]) as request:
                response = await request.json()
                
                moveType = await ApiService.GetType(session, response["type"])
                
                newMove = Move(
                    moveId=response["id"],
                    name=response["name"],
                    description=response["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' '),
                    accuracy=response["accuracy"],
                    power=response["power"],
                    pp=response["pp"],
                    type=moveType
                )
                await sync_to_async(newMove.save)()
                print(f'New move added: {newMove}')
                return newMove
        else:
            if searchMove.type is None:
                async with session.get(move["url"]) as request:
                    response = await request.json()
                    moveType = await ApiService.GetType(session, response["type"])
                    searchMove.type = moveType
                    await sync_to_async(searchMove.save)()
                    print(f'added type to {searchMove}')
            print(f'returning Move: {searchMove}')
            return searchMove