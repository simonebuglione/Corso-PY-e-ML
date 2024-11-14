import json
import requests

link1= "https://open-meteo.com/en/docs"
link2_part1= "https://geocoding-api.open-meteo.com/v1/search?name="
link2_part2="&count=1&language=en&format=json"


def request_dumper(link):
    response = requests.get(link)
    text_response= response.text
    json_response = json.loads(text_response)
    return json_response

input1= input("Dammi la città da cercare:")

link_completo=link2_part1+ input1 + link2_part2
json_citta=request_dumper(link_completo)

print(json_citta)

latitudine=json_citta.get("results")[0].get("latitude")
longitudine=json_citta.get("results")[0].get("longitude")

print (latitudine)
print (longitudine)