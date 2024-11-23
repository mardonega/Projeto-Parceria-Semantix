import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações do aplicativo
st.title("Painel Oncologia Brasil")
st.write(
    "Este painel apresenta dados interativos sobre os casos de oncologia registrados no Brasil. "
    "Você pode carregar uma base de dados semelhante para análises de anos futuros."
)

# Upload do arquivo
st.sidebar.title("Carregamento de Dados")
uploaded_file = st.sidebar.file_uploader("Envie um arquivo CSV com dados semelhantes", type=["csv"])

if uploaded_file is not None:
    try:
        # Carregar os dados enviados
        df = pd.read_csv(uploaded_file, encoding="utf-8")

        # Validar se as colunas principais existem
        required_columns = [
            "UF da residencia",
            "1 Regiao Norte",
            "2 Regiao Nordeste",
            "3 Regiao Sudeste",
            "4 Regiao Sul",
            "5 Regiao Centro-Oeste",
            "Total",
        ]
        if not all(col in df.columns for col in required_columns):
            st.error("Erro: O arquivo enviado não possui a estrutura esperada.")
            st.stop()

        st.success("Dados carregados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        st.stop()

    # Criar a coluna 'Regiao' com base nas colunas de regiões
    def identificar_regiao(row):
        if row["1 Regiao Norte"] > 0:
            return "Norte"
        elif row["2 Regiao Nordeste"] > 0:
            return "Nordeste"
        elif row["3 Regiao Sudeste"] > 0:
            return "Sudeste"
        elif row["4 Regiao Sul"] > 0:
            return "Sul"
        elif row["5 Regiao Centro-Oeste"] > 0:
            return "Centro-Oeste"
        return None

    df["Regiao"] = df.apply(identificar_regiao, axis=1)

    # Barra lateral para filtro por região
    regioes = df["Regiao"].dropna().unique()
    selected_region = st.sidebar.selectbox("Selecione uma Região", regioes)

    # Filtrar os dados com base na região selecionada
    filtered_data = df[df["Regiao"] == selected_region]

    # Exibir os dados filtrados
    st.subheader(f"Dados Filtrados - Região: {selected_region}")
    st.dataframe(filtered_data)

    # Download dos dados filtrados
    st.download_button(
        label="Baixar Dados Filtrados",
        data=filtered_data.to_csv(index=False, encoding="utf-8"),
        file_name=f"dados_filtrados_{selected_region}.csv",
        mime="text/csv",
    )

    # Gráfico de Barras: Total por UF
    if not filtered_data.empty:
        fig = px.bar(
            filtered_data,
            x="UF da residencia",
            y="Total",
            title=f"Total de Casos na Região {selected_region}",
            labels={"Total": "Número de Casos", "UF da residencia": "Unidade Federativa"}
        )
        st.plotly_chart(fig)
    else:
        st.warning("Nenhum dado disponível para a região selecionada.")

    # Gráfico de Comparação por Regiões
    region_totals = df.groupby("Regiao")["Total"].sum().reset_index()
    fig2 = px.bar(
        region_totals,
        x="Regiao",
        y="Total",
        title="Comparação de Casos por Região",
        labels={"Total": "Número de Casos", "Regiao": "Região"}
    )
    st.plotly_chart(fig2)
else:
    st.info("Envie um arquivo CSV para começar a análise.")
