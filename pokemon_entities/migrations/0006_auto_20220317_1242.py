# Generated by Django 3.1.14 on 2022-03-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220317_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, default=7),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, default=6),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, default=6),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, default=7),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, default=3),
        ),
    ]