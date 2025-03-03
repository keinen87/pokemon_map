# Generated by Django 3.1.14 on 2023-01-16 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 13, 29, 28, 297775, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 16, 13, 29, 42, 251170, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
