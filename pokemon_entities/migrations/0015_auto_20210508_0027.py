# Generated by Django 3.1.10 on 2021-05-07 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20210508_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='previous_evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolution', to='pokemon_entities.pokemon', verbose_name='В кого эволюционирует '),
        ),
    ]
