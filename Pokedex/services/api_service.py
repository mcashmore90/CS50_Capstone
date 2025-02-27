import requests
from ..models import Type, Move, Pokemon
from decimal import Decimal
from datetime import datetime
import asyncio
import aiohttp
from asgiref.sync import sync_to_async

class ApiService:
    @classmethod
    async def initialize_locks(cls):
        cls.type_lock = asyncio.Lock()
        cls.move_lock = asyncio.Lock()
        cls.pokemon_lock = asyncio.Lock()
    
    @classmethod
    async def SeedData(cls):
        
        start = datetime.now()
        await cls.initialize_locks()
        types = await sync_to_async(lambda: list(Type.objects.all()))()
        cls.types_dict = {t.name: t for t in types}
        
        moves = await sync_to_async(lambda: list(Move.objects.prefetch_related('type')))()
        cls.moves_dict = {m.name: m for m in moves}
        
        pokemons = await sync_to_async(lambda: list(Pokemon.objects.prefetch_related('types','moves','moves__type')))()
        cls.pokemons_dict = {p.name: p for p in pokemons}

        async with aiohttp.ClientSession() as session:
                async with session.get("https://pokeapi.co/api/v2/pokemon?limit=151") as request:
                    response = await request.json()
                    tasks = [ApiService.CheckData(result["url"], session) for result in response["results"]]
                    await asyncio.gather(*tasks)
                    
        end = datetime.now()
        print(f"! Seed complete in....{end-start} !")
        
        
    @classmethod
    async def CheckData(cls, url, session):
        async with session.get(url) as request:
            pokemonData = await request.json()
            print(f'===CHECKING DATA FOR: {pokemonData["name"].upper()}===')
             
            types, moves = await asyncio.gather(
                asyncio.gather(*[cls.CheckType(type["type"], session) for type in pokemonData["types"]]),
                cls.CheckMoves(pokemonData["moves"], session)
            )
            
            await cls.CheckPokemon(pokemonData,types, moves, session)
            
        print(f'===COMPLETED DATA FOR: {pokemonData["name"].upper()}===')
        
            
    @classmethod        
    async def CheckType(cls, type, session):
        print(f'===CHECKING FOR TYPE: {type["name"].upper()}===')
        
        async with cls.type_lock:
            searchType = cls.types_dict.get(type["name"])
            if not searchType:
            
                async with session.get(type["url"]) as request:
                    typeData = await request.json()
                    searchType = Type(
                        typeId=typeData["id"],
                        name=typeData["name"],
                        image=typeData["sprites"]["generation-ix"]["scarlet-violet"]["name_icon"]
                    )
                    cls.types_dict[type["name"]] = searchType
                    await sync_to_async(searchType.save)()
                print(f'===ADDING NEW TYPE: {type["name"].upper()}===')
                    
        print(f'===RETURNING TYPE: {type["name"].upper()}===')
        return searchType

       
    @classmethod    
    async def CheckMoves(cls, moves, session):
        async def GetMoveData(move, session):
            print(f'===CHECKING FOR MOVE: {move["name"].upper()}===')
            async with cls.move_lock:
                searchMove = cls.moves_dict.get(move["name"]) 
                if not searchMove:
                
                    async with session.get(move["url"]) as request:
                        moveData = await request.json()
                        
                        moveType = await cls.CheckType(moveData["type"], session)
                    
                        searchMove = Move(
                            moveId=moveData["id"],
                            name=moveData["name"],
                            description=moveData["effect_entries"][0]["short_effect"].replace('\n', ' ').replace('\f', ' '),
                            accuracy=moveData["accuracy"],
                            power=moveData["power"],
                            pp=moveData["pp"],
                            type=moveType
                        )
                        cls.moves_dict[move["name"]] = searchMove
                        await sync_to_async(searchMove.save)()
                    print(f'===ADDING NEW MOVE: {move["name"].upper()}===')
                        
            print(f'===RETURNING MOVE: {searchMove}===')
            return searchMove
        
        move_urls = [move['move'] for move in moves 
                    if any(version_group['version_group']['name'] == 'yellow' and version_group['level_learned_at'] == 1 for version_group in move['version_group_details'])] 
        
        moveTasks = [GetMoveData(move, session) for move in move_urls]
        moveSet = await asyncio.gather(*moveTasks)
        return moveSet
    
    @classmethod        
    async def CheckPokemon(cls,pokemon,types, moves, session):
        async with cls.pokemon_lock:
            searchPokemon = cls.pokemons_dict.get(pokemon["name"].replace('-', ' '))
            
            if not searchPokemon:
                stats = await cls.GetPokemonStats(pokemon["stats"])
                desc = await cls.GetPokemonDescription(pokemon["species"]["url"],session)
                                
                newPokemon = Pokemon(
                    pokemonId = pokemon["id"],
                    name = pokemon["name"].replace('-', ' '),
                    image = pokemon["sprites"]["versions"]["generation-i"]["yellow"]["front_default"],
                    height= round(Decimal(pokemon["height"]) * Decimal(0.1),2),
                    weight= round(Decimal(pokemon["weight"]) * Decimal(0.1),2),
                    description = desc,
                    
                    health= stats["health"],
                    attack = stats["health"],
                    defence = stats["health"],
                    sp_attack = stats["health"],
                    sp_defence = stats["health"],
                    speed = stats["health"]
                )
                await sync_to_async(newPokemon.save)()
                await sync_to_async(newPokemon.moves.add)(*moves)
                await sync_to_async(newPokemon.types.add)(*types)
                print(f'===ADDING NEW POKEMON: {pokemon["name"].upper()}===')
            else:
                missing_types = set(types) - set(searchPokemon.types.all())
                if missing_types:
                    await sync_to_async(searchPokemon.types.add)(*missing_types)
                    await sync_to_async(searchPokemon.save)()
                    
                missing_moves = set(moves) - set(searchPokemon.moves.all())
                if missing_moves:
                    await sync_to_async(searchPokemon.moves.add)(*missing_moves)
                    await sync_to_async(searchPokemon.save)()

            print(f'===RETURNING POKEMON: {pokemon["name"].upper()}===')    
            
    async def GetPokemonStats(stats):
        return {
            "health":stats[0]["base_stat"],
            "attack":stats[1]["base_stat"],
            "defence":stats[2]["base_stat"],
            "sp_attack":stats[3]["base_stat"],
            "sp_defence":stats[4]["base_stat"],
            "speed":stats[5]["base_stat"],
        }
        
    async def GetPokemonDescription(url, session):
        async with session.get(url) as request:
            data = await request.json()
            for entry in data['flavor_text_entries']:
                if entry['version']['name'] == "yellow" and entry['language']['name'] == "en":
                    return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')

   