def palindroma(s):
    #tolgo spazi e rendo tutto minuscolo
    stringa_pulita = ''.join(c.lower() for c in s if c.isalnum()) #prendo ogni carattere in stringa, isalnum lo uso per controllare se sono caratteri alfanumerici e join per unire tutti i pezzi 
    #confronto della stringa con la sua versione inversa
    return stringa_pulita == stringa_pulita[::-1] #inverto la stringa con slicing start stop step

#input di richiesta all'utente della stringa
input_utente = input("Inserisci una parola o frase:")

#controlla se la stringa è palindroma e stampa il risultato
if palindroma(input_utente):
    print("è palindroma")
else:
    print("non è palindroma")
