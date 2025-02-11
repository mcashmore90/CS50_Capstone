from django.contrib import admin
from .models import Type, Stat, Move, Pokemon
# Register your models here.
admin.site.register(Type)
admin.site.register(Stat)
admin.site.register(Move)
admin.site.register(Pokemon)