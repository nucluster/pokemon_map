# Generated by Django 3.1.10 on 2021-05-07 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20210506_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
    ]
