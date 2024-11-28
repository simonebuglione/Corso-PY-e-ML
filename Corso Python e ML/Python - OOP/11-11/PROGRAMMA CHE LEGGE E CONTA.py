"""Create un file.txt con uno script python e testo preso da https://it.lipsum.com/ , dopo
averlo fatto scrivete un programma che legge il documento e ci restituisce il numero di parole, righe e caratteri."""


#creo file .txt con del testo Lorem Ipsum
lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu pharetra nec, mattis ac neque.
Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero,
faucibus adipiscing, commodo quis, gravida id, est. Nulla facilisi. Phasellus eu ligula. Vestibulum sit amet purus nec
augue elementum imperdiet. Duis ac turpis. Integer rutrum ante eu lacus. Vestibulum libero nisl, porta vel, scelerisque
enim. Vivamus vestibulum ntulla nec ante. Praesent placerat risus mi. Nulla sit amet est. Mauris eu elit. Etiam tempor
urna eu ullamcorper. Duis at nulla sed arcu vulputate vehicula. Nunc viverra imperdiet enim. Fusce est. Vivamus a
ante. Pellentesque nonummy sem. Nulla et lectus vestibulum urna frrt mollis accumsan. Fusce id pellentesque urna
non venenatis dolor.
"""

#salvo testo in file.txt
with open('lorem_ipsum.txt', 'w', encoding='utf-8') as f: #utf 8 codifica caratteri in formato standard
    f.write(lorem_ipsum)

#funzione leggttura file e calcolo righe colonne e caratteri
def leggi_file_e_conta_righe_colonne():
    with open('lorem_ipsum.txt', 'r', encoding='utf-8') as file:
        testo=file.read()

    #conteggio righe
    righe = testo.splitlines()  #divido testo in righe
    numero_righe = len(righe)

    #per il numero di colonne, conto il numero di colonne nella prima riga (con spazio come delimitatore)
    if righe:
        prima_riga =righe[0].strip()  #rimuove spazi extra
        colonne =prima_riga.split()  #usa lo spazio come delimitatore per le colonne
        numero_colonne = len(colonne)
    else:
        numero_colonne = 0

    #calcolo numero totale di parole e caratteri
    numero_parole = len(testo.split())  # Dividiamo il testo in parole e contiamo
    numero_caratteri = len(testo)  # Conta il numero di caratteri

    #stampa risultati
    print(f"Numero di righe: {numero_righe}")
    print(f"Numero di colonne (della prima riga): {numero_colonne}")
    print(f"Numero di parole: {numero_parole}")
    print(f"Numero di caratteri: {numero_caratteri}")

#eseguo la funzione
leggi_file_e_conta_righe_colonne()
