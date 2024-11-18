import pandas as pd
import numpy as np

#genero numeri casuali
data=np.random.rand(10, 3)

#crea df con colonne

data = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3'])

#mostra df
print(data)