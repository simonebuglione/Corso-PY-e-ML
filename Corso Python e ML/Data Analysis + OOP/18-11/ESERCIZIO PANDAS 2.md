```python
""" Esercizio 2: Manipolazione e Aggregazione dei Dati
 Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
 pandas.
 Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
 città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
 Caricare i dati in un DataFrame.
 Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
 Quantità e Prezzo Unitario.
 Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
 ciascun prodotto.
 Trovare il prodotto più venduto in termini di Quantità.
 Identificare la città con il maggior volume di vendite totali.
 Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
 valore (es., 1000 euro).
 Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
 decrescente.
 Visualizzare il numero di vendite per ogni città"""






import pandas as pd

#dataset vendite
data = {
    'Prodotto': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Quantità': [10, 5, 20, 7, 10, 15, 8, 9, 6, 12],
    'Prezzo Unitario': [20, 50, 20, 30, 50, 20, 30, 50, 30, 20],
    'Città': ['Roma', 'Milano', 'Roma', 'Milano', 'Roma', 'Napoli', 'Napoli', 'Milano', 'Roma', 'Napoli']
}

df = pd.DataFrame(data)
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prodotto</th>
      <th>Quantità</th>
      <th>Prezzo Unitario</th>
      <th>Città</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>10</td>
      <td>20</td>
      <td>Roma</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>50</td>
      <td>Milano</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>20</td>
      <td>20</td>
      <td>Roma</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>7</td>
      <td>30</td>
      <td>Milano</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>10</td>
      <td>50</td>
      <td>Roma</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>15</td>
      <td>20</td>
      <td>Napoli</td>
    </tr>
    <tr>
      <th>6</th>
      <td>C</td>
      <td>8</td>
      <td>30</td>
      <td>Napoli</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B</td>
      <td>9</td>
      <td>50</td>
      <td>Milano</td>
    </tr>
    <tr>
      <th>8</th>
      <td>C</td>
      <td>6</td>
      <td>30</td>
      <td>Roma</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>12</td>
      <td>20</td>
      <td>Napoli</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Aggiungere una colonna "Totale Vendite"
df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario'] #per avere totale faccio quantià per prezzo unitario
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prodotto</th>
      <th>Quantità</th>
      <th>Prezzo Unitario</th>
      <th>Città</th>
      <th>Totale Vendite</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>10</td>
      <td>20</td>
      <td>Roma</td>
      <td>200</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>50</td>
      <td>Milano</td>
      <td>250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>20</td>
      <td>20</td>
      <td>Roma</td>
      <td>400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>7</td>
      <td>30</td>
      <td>Milano</td>
      <td>210</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>10</td>
      <td>50</td>
      <td>Roma</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>15</td>
      <td>20</td>
      <td>Napoli</td>
      <td>300</td>
    </tr>
    <tr>
      <th>6</th>
      <td>C</td>
      <td>8</td>
      <td>30</td>
      <td>Napoli</td>
      <td>240</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B</td>
      <td>9</td>
      <td>50</td>
      <td>Milano</td>
      <td>450</td>
    </tr>
    <tr>
      <th>8</th>
      <td>C</td>
      <td>6</td>
      <td>30</td>
      <td>Roma</td>
      <td>180</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>12</td>
      <td>20</td>
      <td>Napoli</td>
      <td>240</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Raggruppare i dati per prodotto e calcolare il totale delle vendite per ciascun prodotto

totale_vendite_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
totale_vendite_prodotto
```




    Prodotto
    A    1140
    B    1200
    C     630
    Name: Totale Vendite, dtype: int64




```python
#Trovare il prodotto più venduto in termini di quantità
quantita_per_prodotto = df.groupby('Prodotto')['Quantità'].sum()
prodotto_piu_venduto = quantita_per_prodotto.idxmax()
prodotto_piu_venduto, quantita_per_prodotto.max()
```




    ('A', 57)




```python
#Identificare la città con il maggior volume di vendite totali
vendite_per_citta = df.groupby('Città')['Totale Vendite'].sum()
citta_max_vendite = vendite_per_citta.idxmax()
citta_max_vendite, vendite_per_citta.max()

```




    ('Roma', 1280)




```python
#Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore
vendite_superiori_250 = df[df['Totale Vendite'] > 250]
vendite_superiori_250

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prodotto</th>
      <th>Quantità</th>
      <th>Prezzo Unitario</th>
      <th>Città</th>
      <th>Totale Vendite</th>
      <th>prodotto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>20</td>
      <td>20</td>
      <td>Roma</td>
      <td>400</td>
      <td>400</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>10</td>
      <td>50</td>
      <td>Roma</td>
      <td>500</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>15</td>
      <td>20</td>
      <td>Napoli</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B</td>
      <td>9</td>
      <td>50</td>
      <td>Milano</td>
      <td>450</td>
      <td>450</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente

df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
df_ordinato

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prodotto</th>
      <th>Quantità</th>
      <th>Prezzo Unitario</th>
      <th>Città</th>
      <th>Totale Vendite</th>
      <th>prodotto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>10</td>
      <td>50</td>
      <td>Roma</td>
      <td>500</td>
      <td>500</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B</td>
      <td>9</td>
      <td>50</td>
      <td>Milano</td>
      <td>450</td>
      <td>450</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A</td>
      <td>20</td>
      <td>20</td>
      <td>Roma</td>
      <td>400</td>
      <td>400</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A</td>
      <td>15</td>
      <td>20</td>
      <td>Napoli</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>50</td>
      <td>Milano</td>
      <td>250</td>
      <td>250</td>
    </tr>
    <tr>
      <th>6</th>
      <td>C</td>
      <td>8</td>
      <td>30</td>
      <td>Napoli</td>
      <td>240</td>
      <td>240</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>12</td>
      <td>20</td>
      <td>Napoli</td>
      <td>240</td>
      <td>240</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>7</td>
      <td>30</td>
      <td>Milano</td>
      <td>210</td>
      <td>210</td>
    </tr>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>10</td>
      <td>20</td>
      <td>Roma</td>
      <td>200</td>
      <td>200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>C</td>
      <td>6</td>
      <td>30</td>
      <td>Roma</td>
      <td>180</td>
      <td>180</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Visualizzare il numero di vendite per ogni città

numero_vendite_per_citta = df.groupby('Città').size()
numero_vendite_per_citta

```




    Città
    Milano    3
    Napoli    3
    Roma      4
    dtype: int64




```python

```
