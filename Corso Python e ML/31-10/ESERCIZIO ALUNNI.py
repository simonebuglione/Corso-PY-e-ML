"""Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10"""


#dizionario vuoto dati alunni
alunni = {}


while True:
    nome = input("Scrivi il nome dell'alunno o scrivi 'media' per calcolare la media:")
    
    if nome.lower() == 'media':
        #se si sceglie media si procede con il calcolo e la stampa
        for alunno, voti in alunni.items():
            if voti:  #solo se ci sono voti calcola la media
                media = sum(voti) / len(voti)
                print(f"Nome: {alunno}, Media: {media:.2f}")
            else:
                print(f"Nome: {alunno}, Media: N/A")
        break  #esci dal ciclo dopo aver stampato le medie
    
    voti = input("Inserisci i voti separati da virgole: ")
    
    #converto la stringa dei voti in una lista numeri
    voti_lista = [float(voto) for voto in voti.split(',')]
    
    #aggiungi nome e voto alunni al dizionario
    alunni[nome] = voti_lista
