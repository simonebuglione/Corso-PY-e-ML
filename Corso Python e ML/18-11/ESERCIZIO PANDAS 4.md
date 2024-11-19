```python
"""la media dello stipendio e dell'esperienza per ogni dipartimento

trovare i dipendenti con uno stipendio sopra la media

aggiungere una nuova colonna che rappresenta il rank (consiglio cercate la funzione rank di pandas) di ogni dipendente all'interno del suo dipartimento

Mostrare il dataframe raggruppato per dipartimento e ogni dipendente in ordine dal rank più alto al più basso

Rango in base allo stipendio"""
```


```python
import pandas as pd
import numpy as np

dati = {
'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack', 'Kara', 'Liam'],
'Dipartimento': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'IT', 'HR', 'IT', 'Finance', 'IT'],
'Stipendio': [50000, 60000, 70000, 52000, 58000, 72000, 55000, 62000, 75000, 51000, 63000, 76000],
'Esperienza': [2, 5, 8, 3, 4, 10, 4, 6, 12, 1, 7, 15]
}
df = pd. DataFrame(dati)


#media dello stipendio e dell'esperienza per ogni dipartimento

media_per_dipartimento = df.groupby('Dipartimento')[['Stipendio', 'Esperienza']].mean()




#dipendenti con stipendio sopra la media del loro dipartimento
stipendio_medio = df['Stipendio'].mean()
dipendenti_sopra_media = df[df['Stipendio'] > stipendio_medio]
   


#colonna "Rank" calcolata sullo stipendio all'interno del dipartimento
df['Rank'] = df.groupby('Dipartimento')['Stipendio'].rank(ascending=False)


#Mostrare il DataFrame raggruppato per dipartimento e ordinato dal rank più alto al più basso
df_ordinato = df.sort_values(by=['Dipartimento', 'Rank'], ascending=[True, True])


#risultati
media_per_dipartimento, dipendenti_sopra_media, df

(                 Stipendio  Esperienza
 Dipartimento                          
 Finance       60333.333333    5.333333
 HR            58000.000000    5.250000
 IT            66200.000000    8.000000,
        Nome Dipartimento  Stipendio  Esperienza
 2   Charlie           IT      70000           8
 5     Frank           IT      72000          10
 8       Ian           HR      75000          12
 10     Kara      Finance      63000           7
 11     Liam           IT      76000          15,
        Nome Dipartimento  Stipendio  Esperienza  Rank
 0     Alice           HR      50000           2   4.0
 1       Bob      Finance      60000           5   2.0
 2   Charlie           IT      70000           8   3.0
 3     David           HR      52000           3   3.0
 4       Eva      Finance      58000           4   3.0
 5     Frank           IT      72000          10   2.0
 6     Grace           HR      55000           4   2.0
 7    Hannah           IT      62000           6   4.0
 8       Ian           HR      75000          12   1.0
 9      Jack           IT      51000           1   5.0
 10     Kara      Finance      63000           7   1.0
 11     Liam           IT      76000          15   1.0)
