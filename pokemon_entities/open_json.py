import json


with open('pokemons.json', encoding='utf-8') as database:
    pokemons = json.load(database)['pokemons']

print(type(pokemons))
print(pokemons)

with open('capitals.json', encoding='utf-8') as file:
    capitals = json.load(file)

print(type(capitals))
print(capitals)
