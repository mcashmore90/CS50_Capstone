
class TypeDto:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
        
class StatDto:
    def __init__(self, health = None, attack = None, defence = None, sp_attack = None, sp_defence = None, speed = None):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.sp_attack = sp_attack
        self.sp_defence = sp_defence
        self.speed = speed
        
    def __repr__(self):
        return self.__str__()
        
class MoveDto:
    def __init__(self, name, description, accuracy, power, pp, type):
        self.name = name
        self.description = description
        self.accuracy = accuracy
        self.power = power
        self.pp = pp
        self.type = type
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class PokemonDto:
    def __init__(self, image, name, number, stat, moves, types ):
        self.image = image
        self.name = name
        self.number = number
        self.stat = stat
        self.moves = moves
        self.types = types
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
    
class PokemonListDto:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()