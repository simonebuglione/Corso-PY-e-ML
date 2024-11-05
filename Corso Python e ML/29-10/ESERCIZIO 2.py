#lista per tenere traccia dei numeri inseriti
numeri_inseriti = []  

#inizio un ciclo infinito per poter permettere ripetizioni
while True: 
    scelta = input("Vuoi inserire un numero (n) o una stringa (s)?: ").lower()
    
    if scelta == 'n':
        numero = int(input("Inserisci un numero: ")) 

        # aggiunge il numero alla lista 
        numeri_inseriti.append(numero)  

        #capisce se il numero è pari o dispari
        if numero % 2 == 0:
            print(f"{numero} è un numero pari")  
        else:
            print(f"{numero} è un numero dispari") 
        
        #aggiungo un comando extra: statistiche sulle operazioni fatte
        print(f"Numeri inseriti finora: {numeri_inseriti}")
        print(f"Somma totale: {sum(numeri_inseriti)}")
        print(f"Numero massimo: {max(numeri_inseriti)}")
        print(f"Numero minimo: {min(numeri_inseriti)}")

    elif scelta == 's':
        stringa = input("Inserisci una stringa: ")  
        print(f"Hai inserito la stringa: '{stringa}'")  
        
    else:
        #se la scelta non è valida mando questo messaggio
        print("Scelta non valida. Scegli tra 'n' o 's'")  

    ripetere = input("Vuoi ripetere? (si/no): ").lower()  
    if ripetere != 'si':  # se non sceglie 'si' allora esce dal ciclo
        break  #esce dal ciclo e il programma termina
