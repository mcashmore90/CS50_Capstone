from django.db import models
from rest_framework import serializers

# Create your models here.
class Type(models.Model):
    typeId = models.IntegerField()
    name= models.CharField(max_length=15)
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} - {self.image}"
    
    def to_dic(self):
        return{
            "name":self.name,
            "image":self.image
        }

class Stat(models.Model):
    health = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defence = models.IntegerField()
    speed = models.IntegerField()
    pokemon = models.OneToOneField('Pokemon', on_delete=models.CASCADE)
    def __str__(self):
        return f"Health: {self.health}, Attack: {self.attack}, Defence: {self.defence}, sp_atk: {self.sp_attack}, sp_def: {self.sp_defence}, Speed: {self.speed}"
    
    def to_dic(self):
        return{
            "health":self.health,
            "attack":self.attack,
            "defence":self.defence,
            "sp_attack":self.sp_attack,
            "sp_defence":self.sp_defence,
            "speed":self.speed
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
        return f"{self.name} type: {self.type}"
    
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
    description = models.CharField(max_length=255)
    weight = models.DecimalField(default=0.00,max_digits=5, decimal_places=2)
    height = models.DecimalField(default=0.00,max_digits=5, decimal_places=2)
    moves = models.ManyToManyField(Move, blank=True, null=True)
    types = models.ManyToManyField(Type, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.pokemonId}"
    
    def to_dic(self):
        return{
            "image":self.image,
            "name":self.name,
            "number":self.pokemonId,
            "desc": self.description,
            "stat":self.stat.to_dic(),
            "height":self.height,
            "weight":self.weight,
            "moves": [move.to_dic() for move in self.moves.all()],
            "types": [type.to_dic() for type in self.types.all()]
        }
