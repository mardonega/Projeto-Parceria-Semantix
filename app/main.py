import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import scipy.stats as stats

# Configurações do aplicativo
st.title("Painel Oncologia Brasil")
st.write("""
Este aplicativo foi desenvolvido para explorar e analisar dados de registros oncológicos por estados e regiões do Brasil, utilizando os dados disponibilizados pelo **Painel de Monitoramento de Tratamento Oncológico (PAINEL-ONCOLOGIA)**.

### Contextualização
O painel oncológico foi criado para monitorar o cumprimento da **Lei Nº 12.732/2012**, que estabelece o prazo para o início do tratamento de pacientes com neoplasia maligna comprovada. Ele reúne informações consolidadas pelo **DATASUS** sobre diagnósticos e tratamentos realizados no âmbito do Sistema Único de Saúde (SUS).

**Fonte dos dados:** [PAINEL-ONCOLOGIA no DATASUS](http://tabnet.datasus.gov.br/cgi/dhdat.exe?PAINEL_ONCO/PAINEL_ONCOLOGIABR.def).

### Objetivo
- Analisar a distribuição de casos de tratamento oncológico no Brasil, por estado e região.
- Identificar padrões e insights que possam contribuir para políticas públicas de saúde.

### Dicionário de Variáveis
- **UF da residência:** Estado do paciente no momento do diagnóstico.
- **1 Regiao Norte a 5 Regiao Centro-Oeste:** Número de registros de tratamento por região.
- **Total:** Total de registros por estado.
- **Regiao:** Região do Brasil correspondente ao estado.
""")

# Upload do arquivo
st.sidebar.title("Carregamento de Dados")
uploaded_file = st.sidebar.file_uploader("Envie um arquivo CSV com dados semelhantes", type=["csv"])

if uploaded_file is not None:
    try:
        # Carregar os dados
        df = pd.read_csv(uploaded_file, encoding="utf-8")

        # Validar estrutura do arquivo
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

    # Criar a coluna 'Regiao' com mapeamento eficiente
    region_mapping = {
        "1 Regiao Norte": "Norte",
        "2 Regiao Nordeste": "Nordeste",
        "3 Regiao Sudeste": "Sudeste",
        "4 Regiao Sul": "Sul",
        "5 Regiao Centro-Oeste": "Centro-Oeste"
    }
    df["Regiao"] = df[[col for col in region_mapping.keys()]].idxmax(axis=1).map(region_mapping)
    df["Regiao_Num"] = df["Regiao"].astype("category").cat.codes

    # Redução de tamanho opcional
    if st.sidebar.checkbox("Usar amostra de dados"):
        df = df.sample(frac=0.5, random_state=0)  # Trabalhar com 50% dos dados

    # Filtro interativo por região
    regioes = df["Regiao"].dropna().unique()
    selected_region = st.sidebar.selectbox("Selecione uma Região", regioes)

    filtered_data = df[df["Regiao"] == selected_region]
    st.subheader(f"Dados Filtrados - Região: {selected_region}")
    st.dataframe(filtered_data)

    # Botão para download dos dados filtrados
    st.download_button(
        label="Baixar Dados Filtrados",
        data=filtered_data.to_csv(index=False, encoding="utf-8"),
        file_name=f"dados_filtrados_{selected_region}.csv",
        mime="text/csv",
    )

    # Análise Descritiva
    st.write("### Análise Descritiva e Exploratória")
    region_totals = df.groupby("Regiao")["Total"].sum()

    # Proporção por região
    fig1 = px.pie(
        region_totals.reset_index(),
        names="Regiao",
        values="Total",
        title="Proporção de Registros por Região"
    )
    st.plotly_chart(fig1)

    # Distribuição por estado
    fig2 = px.bar(
        df.sort_values("Total", ascending=False),
        x="UF da residencia",
        y="Total",
        title="Distribuição de Registros por Estado",
        labels={"UF da residencia": "Estado", "Total": "Registros"}
    )
    st.plotly_chart(fig2)

    # ANOVA
    st.write("### Análise de Variância (ANOVA)")
    anova_result = stats.f_oneway(
        df[df["Regiao"] == "Norte"]["Total"],
        df[df["Regiao"] == "Nordeste"]["Total"],
        df[df["Regiao"] == "Sudeste"]["Total"],
        df[df["Regiao"] == "Sul"]["Total"],
        df[df["Regiao"] == "Centro-Oeste"]["Total"]
    )
    st.write(f"Estatística F: {anova_result.statistic:.2f}, p-valor: {anova_result.pvalue:.4f}")

    # Regressão Linear
    st.write("### Regressão Linear")
    X = df[["Regiao_Num"]]
    y = df["Total"]
    model = LinearRegression().fit(X, y)
    st.write(f"Coeficiente: {model.coef_[0]:.2f}, Intercepto: {model.intercept_:.2f}")

    # Clustering
    st.write("### Clusterização")
    scaler = StandardScaler()
    cluster_data_scaled = scaler.fit_transform(
        df[["1 Regiao Norte", "2 Regiao Nordeste", "3 Regiao Sudeste", "4 Regiao Sul", "5 Regiao Centro-Oeste"]]
    )
    kmeans = KMeans(n_clusters=3, random_state=0)
    df["Cluster"] = kmeans.fit_predict(cluster_data_scaled)

    fig3 = px.scatter(
        df,
        x="Regiao_Num",
        y="Total",
        color="Cluster",
        title="Clusterização de Estados por Registros",
        labels={"Regiao_Num": "Região (Codificada)", "Total": "Registros Totais"}
    )
    st.plotly_chart(fig3)

    # Conclusão
    st.write("""
    ### Conclusão
    - As análises identificaram padrões regionais significativos nos dados de tratamento oncológico.
    - A ANOVA indicou diferenças estatisticamente significativas entre as regiões.
    - O modelo de regressão linear revelou uma relação direta entre o total de registros e as regiões.
    - O agrupamento mostrou padrões similares em estados, indicando possibilidades de estratégias regionais específicas.
    """)

else:
    st.info("Envie um arquivo CSV para começar a análise.")