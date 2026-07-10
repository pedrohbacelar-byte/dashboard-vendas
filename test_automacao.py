import pandas as pd

import automacao


def test_carregar_dados_retorna_dataframe_preenchido():
    df = automacao.carregar_dados()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_colunas_esperadas_presentes():
    df = automacao.carregar_dados()
    for coluna in ["Sales_Rep_Name", "Year", "Value", "Produto"]:
        assert coluna in df.columns


def test_colunas_sem_espacos_nas_bordas():
    df = automacao.carregar_dados()
    assert all(coluna == coluna.strip() for coluna in df.columns)


def test_arquivo_inexistente_retorna_dataframe_vazio(tmp_path):
    df = automacao.carregar_dados(tmp_path / "nao_existe.csv")
    assert isinstance(df, pd.DataFrame)
    assert df.empty
