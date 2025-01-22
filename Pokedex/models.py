from django.db import models

# Create your models here.
#Pokemon
class Pokemon(models.Model):
    picture = models.CharField(max_length=250)
    name = models.CharField(max_length=25)
    number = models.SmallIntegerField()
    
#Stats    
class Stats(models.Model):
    health = models.SmallIntegerField(default=0)
    attack = models.SmallIntegerField(default=0)
    defence = models.SmallIntegerField(default=0)
    sp_attack = models.SmallIntegerField(default=0)
    sp_defence = models.SmallIntegerField(default=0)
    speed = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return F"Hp: {self.health}, attack: {self.attack}"
    
        
#Moves
class Move(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(100)
    accuracy = models.SmallIntegerField()
    power = models.SmallIntegerField()
    pp = models.SmallIntegerField()

#Type
class Type(models.Model):
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=250)
