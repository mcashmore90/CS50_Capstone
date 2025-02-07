# Generated by Django 5.1.1 on 2025-01-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.SmallIntegerField()),
                ('attack', models.SmallIntegerField()),
                ('defence', models.SmallIntegerField()),
                ('sp_attack', models.SmallIntegerField()),
                ('sp_defence', models.SmallIntegerField()),
                ('speed', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='defence',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='health',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='sp_attack',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='sp_defence',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='speed',
        ),
    ]
