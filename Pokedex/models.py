from django.db import models

# Create your models here.
#Pokemon
class Pokemon(models.Model):
    picture = models.CharField(max_length=250)
    name = models.CharField(max_length=25)
    number = models.SmallIntegerField()
    health = models.SmallIntegerField()
    attack = models.SmallIntegerField()
    defence = models.SmallIntegerField()
    sp_attack = models.SmallIntegerField()
    sp_defence = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    
    
#Abilities

#Types

#Attacks