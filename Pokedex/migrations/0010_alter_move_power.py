# Generated by Django 5.1.1 on 2025-02-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokedex', '0009_alter_pokemon_height_alter_pokemon_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='power',
            field=models.IntegerField(default=0),
        ),
    ]
