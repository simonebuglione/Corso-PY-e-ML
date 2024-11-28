```python
#Crea una tabella pivot che mostri la somma delle vendite per ogni venditore e mese.
```


```python
import pandas as pd
```


```python
data = {
'Venditore': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],
'Mese': ['Gennaio', 'Gennaio', 'Febbraio', 'Febbraio', 'Gennaio'],
'Vendite': [200, 150, 300, 250, 100]
}

df = pd. DataFrame(data)
```


```python
tab_pivot=df.pivot_table(index='Venditore', columns='Mese', values='Vendite', aggfunc='sum')

```
print(tab_pivot)


```python

```
