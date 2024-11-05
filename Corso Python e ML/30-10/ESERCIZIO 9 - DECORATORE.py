"""Crea uno script che chiede nome e un numero poi una chiama la funzione primo_o_no che determini se un numero dato è primo o no. la funzione dovrebbe restituire True se il numero è primo, e False altrimenti a quel punto se è primo lo salva e continua il ciclo altrimenti ti dice quante volte sta non divisore più piccolo"""

#inserisco un decoratore che raccoglie l'input dell'utente per nome e numero
def input_decorator(func):
    def wrapper():
        nome = input("nome: ")  
        numero = int(input("numero: "))  
        return func(nome, numero)  #denomino la funzione originale con nome e numero come argomenti
    return wrapper

#funzione decorata per verificare se un numero è primo
@input_decorator
def verifica_primo(nome, numero):
    if primo_o_no(numero):  #controlla se il numero è primo
        print(f"{nome}, il numero {numero} è primo")  
        return True  # se esce True il numero è primo
    else:
        min_divisori = conta_min_divisori(numero)  #calcola i divisori NON primi
        print(f"{nome}, il numero {numero} NON è primo. Ha {min_divisori} divisori NON primi più piccoli")  
        return False  #False se il numero NON è primo



#Funzione per capire se un numero è primo
def primo_o_no(num):
    if num <= 1:  #i numeri minori o uguali a 1 NON sono primi
        return False
    for i in range(2, int(num ** 0.5) + 1):  #Controlld dei divisori fino alla radice quadrata del numero
        if num % i == 0:  #Se il numero è divisibile per i, NON è primo
            return False
    return True  #esce True se il numero è primo

#funzione per contare i divisori NON primi di un numero
def conta_min_divisori(num):
    #creazione lista di divisori NON primi
    divisori = [i for i in range(2, num) if num % i == 0 and primo_o_no(i) == False]
    return len(divisori)  #Restituisce il numero di divisori NON primi



#funzione principale per gestire il ciclo di input
def main():
    while True:  #ciclo infinito per continuare a chiedere input
        verifica_primo()  #chiama la funzione che verifica se il numero è primo

#punto di ingresso del programma
if __name__ == "__main__":
    main()  #avvia la funzione principale
