```python
import pandas as pd

data = {
    'Regione': ['Nord', 'Sud', 'Nord'],
    'Prodotto': ['A', 'A', 'B'],
    'Vendite': [100, 150, 200],
    'Categoria': ['Alta', 'Media', 'Bassa']
}
df = pd.DataFrame(data)

#mostrare la media delle vendite di ogni combinazione di Regione e Prodotto
```


```python
media_vendite = df.pivot_table(values='Vendite', index='Regione', columns='Prodotto', aggfunc='dev')

print(media_vendite)

```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[17], line 1
    ----> 1 media_vendite = df.pivot_table(values='Vendite', index='Regione', columns='Prodotto', aggfunc='dev')
          3 print(media_vendite)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:9509, in DataFrame.pivot_table(self, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
       9492 @Substitution("")
       9493 @Appender(_shared_docs["pivot_table"])
       9494 def pivot_table(
       (...)
       9505     sort: bool = True,
       9506 ) -> DataFrame:
       9507     from pandas.core.reshape.pivot import pivot_table
    -> 9509     return pivot_table(
       9510         self,
       9511         values=values,
       9512         index=index,
       9513         columns=columns,
       9514         aggfunc=aggfunc,
       9515         fill_value=fill_value,
       9516         margins=margins,
       9517         dropna=dropna,
       9518         margins_name=margins_name,
       9519         observed=observed,
       9520         sort=sort,
       9521     )
    

    File ~\anaconda3\Lib\site-packages\pandas\core\reshape\pivot.py:102, in pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
         99     table = concat(pieces, keys=keys, axis=1)
        100     return table.__finalize__(data, method="pivot_table")
    --> 102 table = __internal_pivot_table(
        103     data,
        104     values,
        105     index,
        106     columns,
        107     aggfunc,
        108     fill_value,
        109     margins,
        110     dropna,
        111     margins_name,
        112     observed,
        113     sort,
        114 )
        115 return table.__finalize__(data, method="pivot_table")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\reshape\pivot.py:183, in __internal_pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort)
        173 if observed is lib.no_default and any(
        174     ping._passed_categorical for ping in grouped._grouper.groupings
        175 ):
        176     warnings.warn(
        177         "The default value of observed=False is deprecated and will change "
        178         "to observed=True in a future version of pandas. Specify "
       (...)
        181         stacklevel=find_stack_level(),
        182     )
    --> 183 agged = grouped.agg(aggfunc)
        185 if dropna and isinstance(agged, ABCDataFrame) and len(agged.columns):
        186     agged = agged.dropna(how="all")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\groupby\generic.py:1432, in DataFrameGroupBy.aggregate(self, func, engine, engine_kwargs, *args, **kwargs)
       1429     kwargs["engine_kwargs"] = engine_kwargs
       1431 op = GroupByApply(self, func, args=args, kwargs=kwargs)
    -> 1432 result = op.agg()
       1433 if not is_dict_like(func) and result is not None:
       1434     # GH #52849
       1435     if not self.as_index and is_list_like(func):
    

    File ~\anaconda3\Lib\site-packages\pandas\core\apply.py:187, in Apply.agg(self)
        184 kwargs = self.kwargs
        186 if isinstance(func, str):
    --> 187     return self.apply_str()
        189 if is_dict_like(func):
        190     return self.agg_dict_like()
    

    File ~\anaconda3\Lib\site-packages\pandas\core\apply.py:603, in Apply.apply_str(self)
        601         else:
        602             self.kwargs["axis"] = self.axis
    --> 603 return self._apply_str(obj, func, *self.args, **self.kwargs)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\apply.py:706, in Apply._apply_str(self, obj, func, *args, **kwargs)
        704 else:
        705     msg = f"'{func}' is not a valid function for '{type(obj).__name__}' object"
    --> 706     raise AttributeError(msg)
    

    AttributeError: 'dev' is not a valid function for 'DataFrameGroupBy' object



```python

```
