import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon_marker(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.entities.all():
            add_pokemon_marker(
                folium_map, pokemon_entity.lat,
                pokemon_entity.lon,
                pokemon.img_url
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.img_url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entities.filter(
            pokemon=requested_pokemon):
        add_pokemon_marker(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.img_url
        )

    context = {'map': folium_map._repr_html_(), 'pokemon': requested_pokemon} 

    if requested_pokemon.next_evolutions.all():
        context.update({
        'pokemon_next_evolutions': requested_pokemon.next_evolutions.all(),
        'pokemon_next_evolutions_id': requested_pokemon.next_evolutions.all()[0].id,
        'pokemon_next_evolutions_img_url': requested_pokemon.next_evolutions.all()[0].img_url,
        'pokemon_next_evolutions_title_ru': requested_pokemon.next_evolutions.all()[0].title_ru,
        })

    return render(request, 'pokemon.html', context=context)

