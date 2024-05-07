import pandas as pd
import numpy as np

ubicacion = "input/kc_house_data.csv"
df = pd.read_csv(ubicacion)


rng1 = np.random.default_rng()
delete_cant = 9500
headers = list(df.columns.values)
for i in range(delete_cant):
    index_header = np.random.randint(len(headers))
    get_header = headers[index_header]
    get_index = np.random.randint(len(df[get_header]))
    df[get_header][get_index] = None

df.to_csv('output/kc_house_data.csv')