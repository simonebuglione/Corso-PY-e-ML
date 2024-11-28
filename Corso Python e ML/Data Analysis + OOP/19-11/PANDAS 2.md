```python
import pandas as pd
```


```python
#fare Inner join su Key

df1 = pd.DataFrame({
    'chiave': ['A', 'B', 'C'],
    'valore1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'chiave': ['A', 'B', 'D'],
    'valore2': [4, 5, 6]
})
```


```python
result = pd.merge(df1, df2, on='chiave', how='inner')
```


```python
print(result)

```

      chiave  valore1  valore2
    0      A        1        4
    1      B        2        5
    


```python
#Step due: sugli stessi dataframe creare una join che mostri tutte le righe di entrambi


df1 = pd.DataFrame({
    'chiave': ['A', 'B', 'C'],
    'valore1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'chiave': ['A', 'B', 'D'],
    'valore2': [4, 5, 6]
})
```


```python


result_outer = pd.merge(df1, df2, on='chiave', how='outer')

```
print(result_outer)

```python

```
