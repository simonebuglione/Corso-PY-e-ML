"""2. Esercizio Avanzato: Sequenza di Fibonacci fino a N Descrizione: Chiedi all'utente di inserire un numero N. Il programma dovrebbe stampare la sequenza di Fibonacci fino a N. Ad esempio, se l'utente inserisce 100, il programma dovrebbe stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100."""

def fibonacci_fino_a_n(n):
    #lista per memorizzare la sequenza di Fibonacci
    fibonacci_sequence = []
    
    #inizializza i primi due numeri della sequenza per poter generare il resto dei numeri
    a, b = 0, 1 #quindi a sta per 0 e b sta per 1
    
    #genera la sequenza fino a N
    while a <= n: #esegue il codice fin quando a <= n, quindi il ciclo genera i numeri della seq di Fib finché il numero corrente (a) è minore o uguale al valore fornito dall'utente (n).
        fibonacci_sequence.append(a)  #aggiungi il numero corrente alla lista
        a, b = b, a + b  #aggiorna a e b
    
    return fibonacci_sequence


def main():
    #chiedi all'utente di inserire un numero N.
    while True:
        try:
            n = int(input("Inserisci un numero N per stampare la sequenza di Fibonacci fino a N: "))
            if n < 0:
                print("devi inserire un numero intero positivo, riprova")
                continue
            break  #sw l'input è valido esci dal ciclo
        except ValueError:
            print("inserisci un numero valido")
    
    #ottieni la sequenza di Fibonacci fino a N
    sequenza = fibonacci_fino_a_n(n)
    

    #stampa la sequenza
    print(f"La sequenza di Fibonacci fino a {n} è: {sequenza}")

#chiamata alla funzione principale per avviare il programma
main()



