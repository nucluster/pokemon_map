from django.db import models

    
class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.pokemon.title + ' Entity'