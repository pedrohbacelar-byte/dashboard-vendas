import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Título do dashboard
st.title("Dashboard de Vendas")

# Ler planilha
dados = pd.read_excel("dados.xlsx")

# Limpar coluna Value (remover $ e converter para número)
dados["Value"] = (
    dados["Value"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# =========================
# MÉTRICAS
# =========================

total_vendas = dados["Value"].sum()

st.metric("Total de vendas", f"${total_vendas:,.2f}")

# =========================
# VENDAS POR VENDEDOR
# =========================

st.subheader("Vendas por vendedor")

vendas_vendedor = dados.groupby("Sales_Rep_Name")["Value"].sum()

fig1, ax1 = plt.subplots()
vendas_vendedor.plot(kind="bar", ax=ax1)

st.pyplot(fig1)

# =========================
# VENDAS POR ANO
# =========================

st.subheader("Vendas por ano")

vendas_ano = dados.groupby("Year")["Value"].sum()

fig2, ax2 = plt.subplots()
vendas_ano.plot(kind="line", marker="o", ax=ax2)

st.pyplot(fig2)

# =========================
# TABELA DE DADOS
# =========================

st.subheader("Tabela de dados")

st.dataframe(dados)