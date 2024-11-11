"""Genera 5 numeri casuali e li salva in un file.
Legge il file e chiede all'utente di indovinare almeno due numeri tra quelli salvati.
Se l'utente non indovina almeno due numeri, perde."""




import random
indovinati=0

#genera 5 num casuali
numeri_casuali=[random.randint(1,100) for _ in range(5)]

#trascrizione su file
with open("numeri_casuali.txt", "w") as file: #w è la modalità scrittura
    for numero in numeri_casuali:
        file.write(f"{numero}\n")


#leggi num da file
with open("numeri_casuali.txt", "r") as file: #"r" per leggere i numeri senza modificarli
    numeri_salvati=[int(line.strip()) for line in file] #strip per pulire spazi extra

print("Benvenuto! indovina almeno due numeri tra quelli salvati")

indovinati=0

#chiwedi 5 numeri all'utente
for i in range(5):
    try:
        risposta= int(input("Indovina il numero:"))
        if risposta in numeri_salvati:
            indovinati += 1
    except ValueError: #except nel caso in cui sbaglia da errore
        print ("Numero non valido, prova di nuovo")

#verifica se ha indovinato almeno 2 numeri
if indovinati>=2:
    print(f"Complimenti, hai indovinato {indovinati} numeri corretti")
else:
    print(f"Ritenta! hai indovinato {indovinati} numeri")