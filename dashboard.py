import streamlit as st
import automacao

st.set_page_config(page_title="Dashboard BI", layout="wide")
st.title("📊 Painel de Performance Comercial")

df = automacao.carregar_dados()

# Filtros na Sidebar
st.sidebar.header("Filtros")
vendedores = st.sidebar.multiselect("Vendedor:", options=sorted(df['Sales_Rep_Name'].unique()))
anos = st.sidebar.multiselect("Ano:", options=sorted(df['Year'].unique()))
produtos = st.sidebar.multiselect("Produto:", options=sorted(df['Produto'].unique()))

# Lógica de Filtragem
df_f = df.copy()
if vendedores: df_f = df_f[df_f['Sales_Rep_Name'].isin(vendedores)]
if anos: df_f = df_f[df_f['Year'].isin(anos)]
if produtos: df_f = df_f[df_f['Produto'].isin(produtos)]

aba1, aba2 = st.tabs(["📈 Visão Geral", "📋 Dados Detalhados"])

with aba1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Faturamento Total", f"R$ {df_f['Value'].sum():,.2f}")
    col2.metric("Total de Vendas", len(df_f))
    col3.metric("Produtos Únicos", len(df_f['Produto'].unique()))
    st.divider()
    st.subheader("Performance por Produto")
    st.bar_chart(df_f.groupby('Produto')['Value'].sum())

with aba2:
    st.dataframe(df_f)