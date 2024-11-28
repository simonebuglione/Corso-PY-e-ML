```python
#Unisci df1 e df2 sulle colonne 'chiave1' e 'chiave2' includendo tutte le righe di df1. Qual è il DataFrame risultante?
```


```python
import pandas as pd

df1 = pd.DataFrame({
    'chiave1': ['K0', 'K1', 'K2'],
    'chiave2': ['K0', 'K1', 'K0'],
    'A': ['A0', 'A1', 'A2']
})

df2 = pd.DataFrame({
    'chiave1': ['K0', 'K1', 'K3'],
    'chiave2': ['K0', 'K0', 'K0'],
    'B': ['B0', 'B1', 'B3']
})
```


```python
result = pd.merge(df1, df2, on=['chiave1', 'chiave2'], how='left')

```


```python
print(result)
```

      chiave1 chiave2   A    B
    0      K0      K0  A0   B0
    1      K1      K1  A1  NaN
    2      K2      K0  A2  NaN
    
