
class TypeDto:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    
    def to_dic(self):
        return{
            "name":self.name,
            "image":self.image
        }
        
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
    
    def to_dic(self):
        return{
            "health":self.health,
            "attack":self.attack,
            "defence":self.defence,
            "sp_attack":self.sp_attack,
            "sp_defence":self.sp_defence,
            "speed":self.speed
        }
        
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
    
    def to_dic(self):
        return{
            "name":self.name,
            "description":self.description,
            "accuracy":self.accuracy,
            "power":self.power,
            "pp":self.pp,
            "type":self.type.to_dic()
        }

class PokemonDto:
    def __init__(self, image, name, number, height, weight, description, stat, moves, types ):
        self.image = image
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.description = description
        self.stat = stat
        self.moves = moves
        self.types = types
        
    def __str__(self):
        return self.description

    def __repr__(self):
        return self.__str__()
    
    def to_dic(self):
        return{
            "image":self.image,
            "name":self.name,
            "number":self.number,
            "desc": self.description,
            "stat":self.stat.to_dic(),
            "height":self.height,
            "weight":self.weight,
            "moves": [move.to_dic() for move in self.moves],
            "types": [type.to_dic() for type in self.types]
        }
    
class PokemonListDto:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            'name': self.name
        }