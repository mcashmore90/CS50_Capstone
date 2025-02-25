from django.db import models

# Create your models here.
class Type(models.Model):
    typeId = models.IntegerField()
    name= models.CharField(max_length=15)
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
    def to_dic(self):
        return{
            "name":self.name,
            "image":self.image
        }

class Move(models.Model):
    moveId = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    accuracy = models.IntegerField(null=True, default=0)
    power = models.IntegerField(null=True, default=0)
    pp = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        #if self.type is None:
             return f"{self.name} {self.type.name}"
        #else:
           #return f"{self.name} "
    
    def to_dic(self):
        return{
            "name":self.name,
            "description":self.description,
            "accuracy":self.accuracy,
            "power":self.power,
            "pp":self.pp,
            "type":self.type.to_dic()
        }

    
class Pokemon(models.Model):
    pokemonId = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    description = models.CharField( blank= True,max_length=255)
    weight = models.DecimalField(default=0.00,max_digits=5, decimal_places=2)
    height = models.DecimalField(default=0.00,max_digits=5, decimal_places=2)
    
    health = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    sp_attack = models.IntegerField(default=0)
    sp_defence = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    
    moves = models.ManyToManyField(Move)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return f"{self.name} - {self.pokemonId}"
    
    def stats(self):
        return{
            "health":self.health,
            "attack":self.attack,
            "defence":self.defence,
            "sp_attack":self.sp_attack,
            "sp_defence":self.sp_defence,
            "speed":self.speed
        }

    def to_dic(self):
        return{
            "image":self.image,
            "name":self.name,
            "number":self.pokemonId,
            "desc": self.description,
            "height":self.height,
            "weight":self.weight,
            
            "health":self.health,
            "attack":self.attack,
            "defence":self.defence,
            "sp_attack": self.sp_attack,
            "sp_defence":self.sp_defence,
            "speed":self.speed,           
            
            "moves": [move.to_dic() for move in self.moves.all()],
            "types": [type.to_dic() for type in self.types.all()]
        }