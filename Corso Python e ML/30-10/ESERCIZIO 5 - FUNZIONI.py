""" 1. Esercizio base: indovina il numero
Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è stato generato. 
Dopo ogni tentativo, il programma dovrebbe dire all'utente se il nuumero da indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina quando l'utente indovina il numero o decide di uscire. """


import random

def gioco_indovina_numero():
    #genera un numero casuale tra 1 e 100 (inclusi)
    numero_da_indovinare = random.randint(1, 100)
    print("Prova ad indovinare il numero tra 1 e 100 che ho scelto")

    while True:
        #Sezione di inserimento del numero da parte dell'utente
        tentativo = input("Inserisci il tuo tentativo o scrivi 'esci' per uscire: ")

        #ccontrolla se l'utente vuole uscire
        if tentativo.lower() == 'esci':
            print("Sei uscito dal gioco, grazie per aver partecipato")
            break
        
        #Prova a convertire l'input in un numero intero
        try:
            tentativo = int(tentativo)
            
            #controlla se il numero è nel range consentito
            if tentativo < 1 or tentativo > 100:
                print("Numero non valido, il numero deve essere compreso tra 1 e 100")
                continue
            
            #Controlla se il tentativo è corretto
            if tentativo < numero_da_indovinare:
                print("Il numero da indovinare è più alto")
            elif tentativo > numero_da_indovinare:
                print("Il numero da indovinare è più basso")
            else:
                print(f"Hai indovinato il numero!!: {numero_da_indovinare}!")
                break  #Se l'utente indovina chiudi il programma

        except ValueError:
            print("inserisci un numero valido o 'esci' per uscire.")

#chiamata alla funzione per avviare il gioco
gioco_indovina_numero()
