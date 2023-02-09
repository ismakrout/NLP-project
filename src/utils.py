import pandas as pd 

def read_input(path, encod, **kwargs):
    dtype_values = kwargs.get('dtype_values', None)
    df = pd.read_csv(path, sep=';', encoding=encod, dtype=dtype_values)
    return df