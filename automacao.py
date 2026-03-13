import pandas as pd
import os

def carregar_dados():
    caminho = 'dados.csv'
    if not os.path.exists(caminho):
        return pd.DataFrame()
    df = pd.read_csv(caminho)
    df.columns = df.columns.str.strip()
    return df