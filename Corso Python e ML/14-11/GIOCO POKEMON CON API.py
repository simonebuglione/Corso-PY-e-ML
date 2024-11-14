import json
import requests as rq
import random
def carica_pokemon(numero):
    link_carica = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    res = rq.get(link_carica)
    if res.status_code == 200:
       data = res.json()
       # Estrarre i dettagli con le chiavi esatte come presenti nell'API
       pokedex = {
           "id_pokemon": data["id"],
           "nome": data["name"],
           "abilita": [ability["ability"]["name"] for ability in data["abilities"]],
           "XP": data["base_experience"],
           "peso": data["weight"],
           "altezza": data["height"]
       }
       return pokedex 
    else:
        print(f"Errore in importazione id:{numero}")
        return None 

# Test: Caricare un Pokémon con ID 5
pokemon = carica_pokemon(5)
if pokemon:
   print(pokemon)