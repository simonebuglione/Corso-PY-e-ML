#input richieste per l'utente
valore_stringa = input("Inserisci una stringa: ")
valore_booleano= input("Inserisci un valore booleano (True o False): ") == "True"
valore_numero =int(input("Inserisci un numero: "))



#creo il dizionario con le chiavi descrittive
dizionario = {
    "stringa": valore_stringa,
    "booleano": valore_booleano,
    "numero":valore_numero
}

# stampa del diz per fare una verifica
print(dizionario)
