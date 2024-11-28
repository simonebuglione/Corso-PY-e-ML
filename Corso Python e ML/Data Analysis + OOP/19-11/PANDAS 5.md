```python
#Unisci prima df1 e df2 includendo solo le chiavi comuni. Poi, unisci il risultato con df3 includendo tutte le chiavi di df3.

import pandas as pd

df1 = pd. DataFrame({
'chiave': ['K0', 'K1', 'K2', 'K3'],
'A': ['A0', 'A1', 'A2', 'A3']
})

df2 = pd. DataFrame({
'chiave': ['K0', 'K1', 'K2'],
'B': ['B0', 'B1', 'B2']
})

df3 = pd. DataFrame({
'chiave': ['K1', 'K2', 'K4'],
'C': ['C1', 'C2', 'C4']
})



#Unisci prima df1 e df2 includendo solo le chiavi comuni. 
df_merged_1_2 = pd.merge(df1, df2, on='chiave', how='inner')



#Poi, unisci il risultato con df3 includendo tutte le chiavi di df3.
result = pd.merge(df_merged_1_2, df3, on='chiave', how='left')

print(result)

```

      chiave   A   B    C
    0     K0  A0  B0  NaN
    1     K1  A1  B1   C1
    2     K2  A2  B2   C2
    


```python

```
