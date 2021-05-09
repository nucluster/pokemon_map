from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='имя покемона')
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    img_url = models.URLField(blank=True, null=True)
    previous_evolution = models.OneToOneField('self',
                                              verbose_name='Из кого '
                                                           'эволюционирует',
                                              null=True, blank=True,
                                              related_name='next_evolution',
                                              on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                related_name='entities')
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True,
                                 verbose_name='Здоровье')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name='Выносливость')
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name='Атака')

    def __str__(self):
        return self.pokemon.title_en + ' Entity'
