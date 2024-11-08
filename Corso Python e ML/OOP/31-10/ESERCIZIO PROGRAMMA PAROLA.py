"""scrivere programma che chiede all'utente una parola e restituisce in ouutput di quella parola le vocali
 all'interno della parola"""


parola = input("parola: ")
vocali = [(i, lettera) for i, lettera in enumerate(parola) if lettera.lower() in "aeiou"]

print("vocali presenti nella parola:", vocali)
