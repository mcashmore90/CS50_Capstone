# Generated by Django 5.1.1 on 2025-02-12 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pokedex', '0017_remove_pokemon_stat_stat_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='pokemonId',
        ),
    ]
