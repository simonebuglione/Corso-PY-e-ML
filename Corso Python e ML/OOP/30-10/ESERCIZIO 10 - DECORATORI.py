"""Sviluppa una funzione chiamata comprimi_stringa che prenda in input una stringa e restituisca una versione "compressa" di essa. La compressione dovrebbe funzionare in questo modo: per ogni gruppo consecutivo di caratteri identici nella stringa, la funzione dovrebbe aggiungere il carattere seguito dal numero dii volte che appare consecutivamente. Per esempio, la stringa "aaabbc" dovrebbe diventare a3b2c1". se la "compressione" non riduce la lunghezza della stringa, la fuzione dovrebbe semplicemente restiturire la stringa originale."""


def verifica_stringa(func):
    """
    decoratore per verificare la validità della stringa in input
    se la stringa è vuota, restituisce un messaggio di errore
    """
    def wrapper(stringa):
        if not stringa:
            return "la stringa fornita è vuota"
        return func(stringa)
    return wrapper

@verifica_stringa
def comprimi_stringa(stringa):
    """
    comprimi la stringa in input
    restituisce una versione compressa della stringa,
    o la stringa originale se la compressione non riduce la lunghezza
    """
    compressa = []
    conteggio = 1
    
    #scorri la stringa e conta i caratteri consecutivi
    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:
            conteggio += 1
        else:
            compressa.append(stringa[i - 1] + str(conteggio))
            conteggio = 1  #reset del conteggio per il nuovo carattere

    #aggiungi l'ultimo carattere e il suo conteggio
    compressa.append(stringa[-1] + str(conteggio))

    #unisci la lista compressa in una stringa
    stringa_compressa = ''.join(compressa)
    
    #restituisci la stringa compressa o quella originale
    return stringa_compressa if len(stringa_compressa) < len(stringa) else stringa

#funzione principale per gestire l'input dell'utente
def main():
    parola = input("Inserisci una parola da comprimere: ")  #riceve input dall'utente
    risultato = comprimi_stringa(parola)  #calcola la compressione
    print(f"Risultato della compressione: {risultato}")  #stampa il risultato

#punto di ingresso del programma
if __name__ == "__main__":
    main()  #avvia la funzione principale