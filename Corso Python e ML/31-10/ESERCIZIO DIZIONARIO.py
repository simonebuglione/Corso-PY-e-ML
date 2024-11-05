"""Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}"""


#input all'utente
stringa = input("Inserisci una stringa:")


#dizionario per la frequenza di comparsa
frequenza = {}

#ciclo attraverso ogni carattere nella stringa
for carattere in stringa:
    if carattere in frequenza:
        frequenza[carattere] += 1  #se il carattere è già stato trovato lo incrementa di 1
    else:
        frequenza[carattere] = 1  #altrimenti la frequenza rimane 1

#stampa del dizionario della frequenza
print(frequenza)
