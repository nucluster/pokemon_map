# Generated by Django 3.1.10 on 2021-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20210509_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]
