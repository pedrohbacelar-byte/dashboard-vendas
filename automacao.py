from pathlib import Path

import pandas as pd

CAMINHO_DADOS = Path(__file__).parent / "dados.csv"


def carregar_dados(caminho: Path | str = CAMINHO_DADOS) -> pd.DataFrame:
    """Carrega os dados de vendas a partir de um CSV.

    O caminho padrão é resolvido em relação a este arquivo, de modo que o
    carregamento funciona independentemente do diretório de trabalho atual.
    Retorna um DataFrame vazio caso o arquivo não exista.
    """
    caminho = Path(caminho)
    if not caminho.exists():
        return pd.DataFrame()
    df = pd.read_csv(caminho)
    df.columns = df.columns.str.strip()
    return df
