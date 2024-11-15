"""ogni volta che verrà cercato un pokemon viene generato un numero, messo il numero restituisce un json che contiene nome pokemon, mosse che può fare ecc. possiamo scegliere se catturarlo o lasciarlo andare. se il pokemon è già presente nel nostro pokedex non c'è bisogno di catturarlo ovviamente. salvare un database che chiamiamo pokedex in modo da poter salvare poi tutti i pokemon nel databaseCreate un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il numero identificativo, nome, abilità, xp (punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""


import requests
import json
import random

# funzione per caricare il Pokédex
def carica_pokedex():
    try:
        with open("pokedex.json", "r") as file:
            pokedex = json.load(file)
    except:
        pokedex = {}
    return pokedex

# funzione per salvare il Pokédex nel file JSON
def salva_pokedex(pokedex):
    with open("pokedex.json", "w") as file:
        json.dump(pokedex, file, indent=4)

# funzione per ottenere un Pokémon dall'API
def ottieni_pokemon_da_api(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon = {
            "numero": numero,
            "nome": data["name"],
            "abilita": data["abilities"][0]["ability"]["name"],
            "xp": data["base_experience"],
            "peso": data["weight"] / 10,  
            "altezza": data["height"] / 10  
        }
        return pokemon
    else:
        print(f"Errore nel recupero del Pokémon con ID {numero}")
        return None

# funzione per aggiungere un Pokémon al Pokédex
def aggiungi_al_pokedex(pokedex, pokemon):
    pokedex[str(pokemon["numero"])] = pokemon
    salva_pokedex(pokedex)

# funzione per mostrare il Pokédex
def mostra_pokedex(pokedex):
    if not pokedex:
        print("Il Pokédex è vuoto")
    else:
        for numero, pokemon in pokedex.items():
            print(f"ID: {numero}, Nome: {pokemon['nome']}, Abilità: {pokemon['abilita']}, XP: {pokemon['xp']}, Peso: {pokemon['peso']}kg, Altezza: {pokemon['altezza']}m")

# funzione per aggiungere XP a un Pokémon
def aggiungi_xp(pokemon, pokedex):
    xp_vittoria = 40  # XP guadagnati per ogni vittoria

    # Controlliamo se il Pokémon è già nel Pokédex e aggiorniamo gli XP
    if str(pokemon['numero']) in pokedex:
        pokedex[str(pokemon['numero'])]['xp'] += xp_vittoria
    else:
        # Se il Pokémon non è nel Pokédex, lo aggiungiamo con gli XP
        pokemon['xp'] = xp_vittoria
        pokedex[str(pokemon['numero'])] = pokemon

    salva_pokedex(pokedex)  # Salviamo il Pokédex aggiornato
    return pokedex[str(pokemon['numero'])]['xp']

# simula una sfida tra due Pokémon
def sfida_pokemon(pokemon1, pokemon2, pokedex):
    print(f"\nInizia la sfida tra {pokemon1['nome']} e {pokemon2['nome']}!")
    hp1, hp2 = 100, 100  # HP iniziali

    for turno in range(1, 4):
        print(f"\n--- Turno {turno} ---")
        danno1 = random.randint(5, 30)
        danno2 = random.randint(5, 30)

        hp1 -= danno2
        hp2 -= danno1

        print(f"{pokemon1['nome']} infligge {danno1} danni a {pokemon2['nome']}. HP di {pokemon2['nome']}: {hp2}")
        print(f"{pokemon2['nome']} infligge {danno2} danni a {pokemon1['nome']}. HP di {pokemon1['nome']}: {hp1}")

        if hp1 <= 0 or hp2 <= 0:
            break

    print("\n--- Fine della sfida ---")
    if hp1 > hp2:
        print(f"{pokemon1['nome']} vince la sfida con {hp1} HP rimanenti!")
        xp_totali = aggiungi_xp(pokemon1, pokedex)  # Aggiungiamo XP dopo la vittoria
        print(f"XP totali di {pokemon1['nome']}: {xp_totali}")
        return True  # pokemon1 vince
    else:
        print(f"{pokemon2['nome']} vince la sfida con {hp2} HP rimanenti!")
        return False  # pokemon2 vince

# funzione principale per catturare Pokémon
def cattura_pokemon():
    pokedex = carica_pokedex()

    while True:
        print("\n--- Menu ---")
        print("1. Cerca un Pokémon")
        print("2. Mostra il Pokédex")
        print("3. Simula una sfida")
        print("4. Esci dal gioco")
        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            numero = random.randint(1, 1025)
            print(f"Hai trovato un Pokémon con ID: {numero}!")

            if str(numero) in pokedex:
                print(f"{pokedex[str(numero)]['nome']} è già nel tuo Pokédex, non hai bisogno di catturarlo!")
            else:
                pokemon = ottieni_pokemon_da_api(numero)
                if pokemon:
                    print(f"Hai incontrato {pokemon['nome']}!")
                    cattura = input("Vuoi catturarlo? (s/n): ").strip().lower()
                    if cattura == "s":
                        aggiungi_al_pokedex(pokedex, pokemon)
                        print(f"Hai catturato {pokemon['nome']}! È stato aggiunto al tuo Pokédex")
                    else:
                        print(f"Hai deciso di lasciare andare {pokemon['nome']}")
        elif scelta == "2":
            mostra_pokedex(pokedex)
        elif scelta == "3":
            if len(pokedex) < 1:
                print("Hai bisogno di almeno un Pokémon nel Pokédex per simulare una sfida!")
            else:
                pokedex_lista = random.choice(list(pokedex.keys()))
                pokemon1 = pokedex[pokedex_lista]
                pokemon2 = ottieni_pokemon_da_api(random.randint(1, 1025))

                if pokemon2:
                    if sfida_pokemon(pokemon1, pokemon2, pokedex):
                        print(f"{pokemon2['nome']} è stato sconfitto ed è stato aggiunto al tuo Pokédex!")
                        aggiungi_al_pokedex(pokedex, pokemon2)
        elif scelta == "4":
            print("Esci dal gioco")
            break
        else:
            print("Opzione non valida. Riprova")

# avvio del programma
cattura_pokemon()