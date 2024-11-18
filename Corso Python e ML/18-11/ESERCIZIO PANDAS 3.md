```python
"""calcolare la media dei voti per ogni materia

calcolare la media dei voti di ogni studente

calcolare la media di ogni studente in ogni materia"""
```


```python
import pandas as pd
import numpy as np
```


```python

```


```python
data = {
    'Studente': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Soggetto': ['Matematica', 'Matematica', 'Matematica', 'Scienze', 'Scienze', 'Scienze', 'Inglese', 'Inglese', 'Inglese'],
    'Punteggio': [85, 90, 95, 80, 70, 75, 88, 92, 85]
}

df = pd.DataFrame(data)

```


```python
#calcolare la media dei voti per ogni materia

media_per_materia = df.groupby('Soggetto')['Punteggio'].mean()
media_per_materia

```




    Soggetto
    Inglese       88.333333
    Matematica    90.000000
    Scienze       75.000000
    Name: Punteggio, dtype: float64


#calcolare la media dei voti di ogni studente
media_voti_per_studente = df.groupby('Studente')['Punteggio'].mean()


```python
#calcolare la media di ogni studente in ogni materia
media_per_materia_studente = df.groupby(['Studente','Soggetto'])['Punteggio'].mean()

```


```python
#risultati
media_per_materia, media_voti_per_studente, media_per_materia_studente
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[65], line 2
          1 #risultati
    ----> 2 media_per_materia, media_voti_per_studente, media_per_materia_studente
    

    NameError: name 'media_voti_per_studente' is not defined



```python

```


```python

```
