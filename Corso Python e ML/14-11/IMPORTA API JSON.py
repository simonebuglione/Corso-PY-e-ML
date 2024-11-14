"""Create un programma python che permette tramite le api
https://open-meteo.com/en/docs (per le previsioni metereologiche) e
(per l'ottenimento in automatico della propria
langitudine e latitudine tramite l'indirizzo ip), di vedere le previsioni
metereologiche.
L'utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni."""



import json
import requests

#richieste http e risposte json
def richiesta_dati(link):
    response = requests.get(link)
    text_response = response.text
    json_response = json.loads(text_response)
    return json_response


#richiesta nome città
input1 = input("Dammi la città da cercare: ")

#link per ottenere latitudine e longitudine della città
link2_part1 = "https://geocoding-api.open-meteo.com/v1/search?name="
link2_part2 = "&count=1&language=en&format=json"

#costruzione del link completo per ottenere la latitudine e longitudine
link_completo = link2_part1 + input1 + link2_part2
json_citta = richiesta_dati(link_completo)

#estrazione di latitudine e longitudine
latitudine =json_citta.get("results")[0].get("latitude")
longitudine =json_citta.get("results")[0].get("longitude")

print(f"Latitudine: {latitudine}")
print(f"Longitudine: {longitudine}")

#richiesta di quanti giorni vuole le previsioni meteo (1, 3 o 7)
giorni =int(input("Quanti giorni di previsioni vuoi vedere? (1, 3 o 7): "))

#costruzione link per le previsioni meteo
link_meteo =f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&forecast_days={giorni}&timezone=Europe%2FRome"
json_meteo =richiesta_dati(link_meteo)

#estrazione dati meteo e print
print("\nPrevisioni meteo:")
for i in range(giorni):
    data = json_meteo["daily"]["time"][i]
    temp_massima =json_meteo["daily"]["temperature_2m_max"][i]
    temp_minima =json_meteo["daily"]["temperature_2m_min"][i]
    precipitazioni =json_meteo["daily"]["precipitation_sum"][i]
    vento = json_meteo["daily"]["wind_speed_10m_max"][i]
    print(f"\nData: {data}")
    print(f"Temperatura massima: {temp_massima}°C")
    print(f"Temperatura minima: {temp_minima}°C")
    print(f"Precipitazioni: {precipitazioni} mm")
    print(f"Velocità del vento: {vento} km/h")
