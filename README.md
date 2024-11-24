
# **Projeto Parceria Semantix: Painel Oncologia Brasil**

## **Descrição do Projeto**
Este projeto faz parte de uma parceria com a **Semantix** e foi desenvolvido para analisar dados do **Painel de Monitoramento de Tratamento Oncológico (PAINEL-ONCOLOGIA)**. O objetivo principal é fornecer insights sobre a distribuição de casos oncológicos no Brasil, por estados e regiões, utilizando ferramentas interativas e estatísticas.

---

## **Contextualização**
O Painel Oncológico foi criado para acompanhar o cumprimento da **Lei Nº 12.732/2012**, que estabelece o prazo máximo de 60 dias para início do tratamento de pacientes com diagnóstico de neoplasia maligna. Este painel é uma iniciativa do **DATASUS** para monitorar e disponibilizar informações sobre diagnósticos e tratamentos realizados pelo SUS.

### **Fonte dos Dados**
Os dados utilizados neste projeto foram extraídos do **DATASUS**. Acesse a base de dados oficial:
- [Painel de Monitoramento Oncológico - DATASUS](http://tabnet.datasus.gov.br/cgi/dhdat.exe?PAINEL_ONCO/PAINEL_ONCOLOGIABR.def)

---

## **Funcionalidades do Aplicativo**
O aplicativo interativo desenvolvido com **Streamlit** oferece as seguintes funcionalidades:

1. **Carregamento de Dados Personalizado**:
   - Permite o upload de bases de dados no formato CSV com estrutura similar à base oficial.
   
2. **Filtros Interativos**:
   - Filtragem dos dados por região para análise específica.
   - Exibição de tabelas com os dados filtrados.

3. **Gráficos Interativos**:
   - Proporção de registros por região (gráfico de pizza).
   - Distribuição de registros por estado (gráfico de barras).

4. **Modelagem Estatística**:
   - **Análise de Variância (ANOVA):** Compara médias de registros entre regiões.
   - **Regressão Linear:** Previsão do número total de registros com base nas regiões.

5. **Agrupamento (Clustering)**:
   - Utilização de **K-Means** para segmentar estados com padrões similares de registros.

6. **Download de Dados**:
   - Exportação dos dados filtrados diretamente pelo aplicativo.

7. **Conclusões e Insights**:
   - Reflexões sobre os resultados estatísticos e padrões identificados.

---

## **Como Executar o Aplicativo**
Para executar o aplicativo localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/mardonega/Projeto-Parceria-Semantix.git
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd Projeto-Parceria-Semantix
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo:
   ```bash
   streamlit run app/main.py
   ```
5. Abra o navegador e acesse o endereço fornecido (geralmente `http://localhost:8501`).

---

## **Tecnologias Utilizadas**
- **Linguagem:** Python
- **Bibliotecas:**
  - Streamlit (interface interativa)
  - Pandas (manipulação de dados)
  - Plotly (gráficos interativos)
  - Scikit-learn (modelagem estatística e clustering)
  - Scipy (estatísticas)
- **Ambiente:** Jupyter Notebook (para análises interativas)

---

## **Contribuições**
Contribuições são bem-vindas! Sinta-se à vontade para abrir **Issues** ou enviar um **Pull Request** com melhorias ou sugestões.

---

## **Licença**
Este projeto é distribuído sob a Licença MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

---

## **Demonstração**
Confira o vídeo demonstrativo do funcionamento do aplicativo:

[![Demonstração do Aplicativo] clique [aqui para acessar diretamente o vídeo](video/novo_video_semantix.webm).

---

## **Próximos Passos**
- Implementar análises adicionais com foco em correlações mais profundas.
- Criar dashboards dinâmicos para visualização de dados em tempo real.

---

## **Contato**
- **Desenvolvedor:** Mardonega  
- **E-mail:** [mardonega@gmail.com](mailto:mardonega@gmail.com)

 ```
3. Verifique no GitHub se o README aparece corretamente formatado.

---
