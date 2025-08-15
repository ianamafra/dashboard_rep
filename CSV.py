import pandas as pd
import streamlit as st

st.title("Dashboard de Informações - REP 671")
st.markdown("Dados sistêmicos das Unidades Básicas de Saúde - Manaus/AM")

# Upload do CSV manual
uploaded_file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

    # Filtros
    st.sidebar.header("Filtros")
    grupo_disponivel = sorted(df['GRUPO'].astype(str).unique())
    grupo_disponivel = st.sidebar.multiselect("Grupo", grupo_disponivel, default=grupo_disponivel)

    app_status = sorted(df['REP 671 '].astype(str).unique())
    app_status = st.sidebar.multiselect("Status App", app_status, default=app_status)

    geo_status = sorted(df['GEOLOCALIZAÇÃO'].astype(str).unique())
    geo_status = st.sidebar.multiselect("GPS", geo_status, default=geo_status)

    df_filtro = df[
        (df['GRUPO'].isin(grupo_disponivel)) &
        (df["REP 671 "].isin(app_status)) &
        (df["GEOLOCALIZAÇÃO"].isin(geo_status))
    ]

    # KPI - Total de Unidades
    total_unidades = df_filtro['UNIDADE'].nunique()
    st.metric(label="Total de Unidades", value=total_unidades)

else:
    st.warning("Por favor, envie o arquivo CSV para continuar.")
