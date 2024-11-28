```python
#Combina df1 e df2 affiancandoli, allineando gli indici.
```


```python
import pandas as pd

```


```python
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=[0, 1, 2])

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=[0, 2, 3])
```


```python
result = pd.concat([df1, df2], axis=1)

```


```python
print(result)

```

         A    B    C    D
    0   A0   B0   C0   D0
    1   A1   B1  NaN  NaN
    2   A2   B2   C1   D1
    3  NaN  NaN   C2   D2
    


```python

```
