import streamlit as st 
import pandas as pd 
import plotly.express as px 

st.set_page_config(
    page_title="Controle de Ponto Eletrônico - REP 671",
    page_icon="📊",
    layout="wide",
)

df_local =  pd.read_csv(r'C:\Users\iana.mafra\Documents\Dashboard\ControleDePontoEletronico_new.csv', encoding='ISO-8859-1')

# Tenta carregar localmente
if os.path.exists(df_local):
    df = pd.read_csv(df_local, encoding='ISO-8859-1')
else:
    st.warning("Arquivo local não encontrado. Faça o upload do CSV.")
    arquivo = st.file_uploader("Envie o arquivo CSV", type=["csv"])
    if arquivo is not None:
        df = pd.read_csv(arquivo, encoding='ISO-8859-1')
    else:
        st.stop()  # para o app até o arquivo ser carregado

st.sidebar.header("Filtros")

#Filtro de Grupo 
grupo_disponivel = sorted(df['GRUPO'].astype(str).unique())
grupo_disponivel = st.sidebar.multiselect("Grupo", grupo_disponivel, default=grupo_disponivel)

#Filtro de Status de Atualização do App 
app_status = sorted(df['REP 671 '].astype(str).unique())
app_status = st.sidebar.multiselect("Status App", app_status, default=app_status)
                                    
#Filtro de Status da Geolocalização 
geo_status = sorted(df['GEOLOCALIZAÇÃO'].astype(str).unique())
geo_status = st.sidebar.multiselect("GPS", geo_status, default=geo_status)

#Filtro de Unidades
unidade_ubs = sorted(df['UNIDADE '].astype(str).unique())
unidade_ubs = st.sidebar.multiselect("UNIDADE ",unidade_ubs, default=unidade_ubs)

#Filtro do Dataframe 
df_filtro = df[
    (df['GRUPO'].isin(grupo_disponivel)) &
    (df["REP 671 "].isin(app_status)) &
    (df["GEOLOCALIZAÇÃO"].isin(geo_status))  &
    (df["UNIDADE "].isin(unidade_ubs))
]

#Descrição do objetivo do dashboard
st.title("Dashboard de Informações - REP 671")
st.markdown("Dados sistêmicos das Unidades Básicas de Saúde - Manaus/AM")

## KPIs ## 
st.subheader("Geral")
#KPIs - Total de Unidades 
total_unidades = df_filtro['UNIDADE '].unique()

st.metric(label="Total de UBS's", value=total_unidades)

# Tabela de Informações - CSV #
st.subheader("Dados Detalhados")
st.dataframe(df_filtro)




