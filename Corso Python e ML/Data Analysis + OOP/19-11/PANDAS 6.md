```python
#Riorganizza il DataFrame in modo che ogni categoria diventi una colonna e i valori siano distribuiti di conseguenza per ogni data.
```


```python
import pandas as pd

data = {
    'Data': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'Categoria': ['A', 'B', 'A', 'B'],
    'Valore': [10, 20, 15, 25]
}

df = pd.DataFrame(data)
```


```python
df_riorg=df.pivot(index='Data', columns='Categoria', values='Valore')

print(df_riorg)
```

    Categoria   A   B
    Data             
    2024-01    10  20
    2024-02    15  25
    


```python

```
