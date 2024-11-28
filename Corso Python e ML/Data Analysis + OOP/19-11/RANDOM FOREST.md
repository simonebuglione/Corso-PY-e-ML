```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

train_data = pd.read_csv(r"C:\Users\bugli\Desktop\GitHub\Corso-PY-e-ML\Corso Python e ML\Dataset\dati test Titanic.csv")
test_data = pd.read_csv(r"C:\Users\bugli\Desktop\GitHub\Corso-PY-e-ML\Corso Python e ML\Dataset\dati test Titanic.csv")

y = train_data["Sopravvissuto"]
features = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Sopravvissuto': predictions})
print(output)
output.to_csv(r'C:\Users\bugli\Desktop\submission.csv', index=False)
print("Il tuo invio è stato salvato con successo!")

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:3805, in Index.get_loc(self, key)
       3804 try:
    -> 3805     return self._engine.get_loc(casted_key)
       3806 except KeyError as err:
    

    File index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()
    

    File index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas\\_libs\\hashtable_class_helper.pxi:7081, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    File pandas\\_libs\\hashtable_class_helper.pxi:7089, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'Sopravvissuto'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    Cell In[14], line 7
          4 train_data = pd.read_csv(r"C:\Users\bugli\Desktop\GitHub\Corso-PY-e-ML\Corso Python e ML\Dataset\dati test Titanic.csv")
          5 test_data = pd.read_csv(r"C:\Users\bugli\Desktop\GitHub\Corso-PY-e-ML\Corso Python e ML\Dataset\dati test Titanic.csv")
    ----> 7 y = train_data["Sopravvissuto"]
          8 features = ["Pclass", "Sex", "SibSp", "Parch"]
         10 X = pd.get_dummies(train_data[features])
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4102, in DataFrame.__getitem__(self, key)
       4100 if self.columns.nlevels > 1:
       4101     return self._getitem_multilevel(key)
    -> 4102 indexer = self.columns.get_loc(key)
       4103 if is_integer(indexer):
       4104     indexer = [indexer]
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key)
       3807     if isinstance(casted_key, slice) or (
       3808         isinstance(casted_key, abc.Iterable)
       3809         and any(isinstance(x, slice) for x in casted_key)
       3810     ):
       3811         raise InvalidIndexError(key)
    -> 3812     raise KeyError(key) from err
       3813 except TypeError:
       3814     # If we have a listlike key, _check_indexing_error will raise
       3815     #  InvalidIndexError. Otherwise we fall through and re-raise
       3816     #  the TypeError.
       3817     self._check_indexing_error(key)
    

    KeyError: 'Sopravvissuto'



```python

```
