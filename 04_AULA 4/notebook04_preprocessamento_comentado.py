{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NJNOQiFtR8d-"
      },
      "source": [
        "# Notebook 04 — Preparação de Dados"
      ],
      "id": "NJNOQiFtR8d-"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Pré-processamento e preparação de dados**\n",
        "##**Por que preparar os dados?**\n",
        "\n",
        "Antes de treinar um modelo de Machine Learning, é fundamental garantir que os dados estejam organizados e em boas condições para análise. Esse processo é chamado de pré-processamento de dados.\n",
        "\n",
        "Na prática, dados coletados de sistemas reais — como sensores industriais, registros de clientes ou logs de aplicações — raramente estão perfeitos. É comum encontrarmos problemas como:\n",
        "\n",
        "- valores faltantes\n",
        "\n",
        "- outliers (valores muito extremos)\n",
        "\n",
        "- dados duplicados\n",
        "\n",
        "- inconsistências de formato\n",
        "\n",
        "- variáveis irrelevantes\n",
        "\n",
        "Se esses problemas não forem tratados, o modelo de aprendizado de máquina pode:\n",
        "\n",
        "- aprender padrões incorretos\n",
        "\n",
        "- apresentar desempenho ruim\n",
        "\n",
        "- gerar previsões pouco confiáveis\n",
        "\n",
        "Por esse motivo, uma parte importante de qualquer projeto de Ciência de Dados ou Inteligência Artificial é dedicada à limpeza, organização e transformação dos dados antes do treinamento do modelo.\n",
        "\n",
        "Esse processo geralmente envolve etapas como:\n",
        "\n",
        "- carregamento e inspeção inicial do dataset\n",
        "\n",
        "- verificação de valores faltantes\n",
        "\n",
        "- tratamento ou remoção de dados inconsistentes\n",
        "\n",
        "- identificação de outliers\n",
        "\n",
        "- transformação ou normalização de variáveis\n",
        "\n",
        "- seleção das variáveis relevantes para o modelo\n",
        "\n",
        "Neste notebook utilizaremos a biblioteca Pandas, uma das ferramentas mais importantes do ecossistema Python para manipulação de dados."
      ],
      "metadata": {
        "id": "OUCb1QmHlelo"
      },
      "id": "OUCb1QmHlelo"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**A biblioteca Pandas**\n",
        "\n",
        "O Pandas é uma biblioteca Python amplamente utilizada para análise e manipulação de dados estruturados. Ela permite trabalhar com tabelas de dados de forma semelhante a uma planilha ou banco de dados.\n",
        "\n",
        "A principal estrutura de dados utilizada pelo Pandas é o DataFrame, que representa uma tabela com linhas e colunas.\n",
        "\n",
        "Exemplo de um DataFrame:\n",
        "\n",
        "![image.png](data:image/png;base64,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)\n",
        "\n",
        "Cada coluna representa uma variável e cada linha representa um registro.\n",
        "\n",
        "Com o Pandas, podemos:\n",
        "\n",
        "- carregar arquivos CSV\n",
        "\n",
        "- explorar dados rapidamente\n",
        "\n",
        "- limpar dados inconsistentes\n",
        "\n",
        "- transformar dados\n",
        "\n",
        "- preparar o dataset para uso em algoritmos de machine learning"
      ],
      "metadata": {
        "id": "Pm-g81lclzgs"
      },
      "id": "Pm-g81lclzgs"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Funções importantes do Pandas para preparação de dados**\n",
        "\n",
        "A seguir estão algumas funções muito utilizadas durante o processo de pré-processamento de dados."
      ],
      "metadata": {
        "id": "NwkUSYoHmaXL"
      },
      "id": "NwkUSYoHmaXL"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NHF4SBi9R8eC"
      },
      "outputs": [],
      "source": [
        "# Instalamos a biblioteca pandas\n",
        "\n",
        "!pip install pandas"
      ],
      "id": "NHF4SBi9R8eC"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QnledWNmR8eE"
      },
      "outputs": [],
      "source": [
        "# Importamos pandas\n",
        "import pandas as pd"
      ],
      "id": "QnledWNmR8eE"
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos um conjunto de dados de exemplo\n",
        "\n",
        "dados = {    \"idade\":[20,25,None,30],    \"salario\":[2000,3000,2500,None]}"
      ],
      "metadata": {
        "id": "VPMo-y_4mMDH"
      },
      "id": "VPMo-y_4mMDH",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(dados)"
      ],
      "metadata": {
        "id": "IRBbrGycMVvw"
      },
      "id": "IRBbrGycMVvw",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Leitura de dados**\n",
        "\n",
        "A função ```read_csv()``` é usada para carregar datasets armazenados em arquivos CSV."
      ],
      "metadata": {
        "id": "dFI7hnq7mTAl"
      },
      "id": "dFI7hnq7mTAl"
    },
    {
      "cell_type": "code",
      "source": [
        "# Leitura do arquivo .csv\n",
        "\n",
        "df=pd.read_csv(\"dataset_exemplo_preprocessamento_pandas.csv\")\n",
        "print(df)"
      ],
      "metadata": {
        "id": "G3ft-ZvLraTA"
      },
      "id": "G3ft-ZvLraTA",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criação de um dataframe para o conjunto de dados gerados anteriormente"
      ],
      "metadata": {
        "id": "Ekf5efiTru_T"
      },
      "id": "Ekf5efiTru_T"
    },
    {
      "cell_type": "code",
      "source": [
        "# Transformamos os dados em um DataFrame\n",
        "\n",
        "df1 = pd.DataFrame(dados)"
      ],
      "metadata": {
        "id": "25JxA3lGmQnE"
      },
      "id": "25JxA3lGmQnE",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1)"
      ],
      "metadata": {
        "id": "qrIa3HpSsIri"
      },
      "id": "qrIa3HpSsIri",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Visualização inicial dos dados**\n",
        "\n",
        "```head()```\n",
        "\n",
        "A função ```head()``` mostra as primeiras linhas do dataset."
      ],
      "metadata": {
        "id": "VL1KVi7emfhn"
      },
      "id": "VL1KVi7emfhn"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.head())"
      ],
      "metadata": {
        "id": "lV0mh9ExmiLE"
      },
      "id": "lV0mh9ExmiLE",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.head())"
      ],
      "metadata": {
        "id": "GcfFOZCZsOsi"
      },
      "id": "GcfFOZCZsOsi",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Isso permite verificar rapidamente:\n",
        "\n",
        "- estrutura do dataset\n",
        "\n",
        "- nomes das colunas\n",
        "\n",
        "- formato dos dados"
      ],
      "metadata": {
        "id": "Igiy7KNlmleI"
      },
      "id": "Igiy7KNlmleI"
    },
    {
      "cell_type": "markdown",
      "source": [
        "```info()```\n",
        "\n",
        "A função ```info()``` mostra informações importantes sobre o dataset."
      ],
      "metadata": {
        "id": "NXlaXlb8m7aj"
      },
      "id": "NXlaXlb8m7aj"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.info())"
      ],
      "metadata": {
        "id": "GGVd8EI9m9Jg"
      },
      "id": "GGVd8EI9m9Jg",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.info())"
      ],
      "metadata": {
        "id": "gU66bbAFsTN-"
      },
      "id": "gU66bbAFsTN-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ela exibe:\n",
        "\n",
        "- número de linhas\n",
        "\n",
        "- número de colunas\n",
        "\n",
        "- tipos de dados\n",
        "\n",
        "- presença de valores faltantes"
      ],
      "metadata": {
        "id": "ZDbSxrGqnAIE"
      },
      "id": "ZDbSxrGqnAIE"
    },
    {
      "cell_type": "markdown",
      "source": [
        "```describe()```\n",
        "\n",
        "A função ```describe()``` fornece estatísticas básicas das variáveis numéricas."
      ],
      "metadata": {
        "id": "bs3FgCKmnFOA"
      },
      "id": "bs3FgCKmnFOA"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.describe())"
      ],
      "metadata": {
        "id": "vOflTAiBs_Rv"
      },
      "id": "vOflTAiBs_Rv",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.describe())"
      ],
      "metadata": {
        "id": "AFvUzsgossMh"
      },
      "id": "AFvUzsgossMh",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Entre as informações apresentadas estão:\n",
        "\n",
        "- média\n",
        "\n",
        "- desvio padrão\n",
        "\n",
        "- valores mínimo e máximo\n",
        "\n",
        "- quartis\n",
        "\n",
        "Essas informações ajudam a identificar distribuições anormais ou possíveis outliers."
      ],
      "metadata": {
        "id": "OoToj-XHnIYt"
      },
      "id": "OoToj-XHnIYt"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Identificação de dados faltantes**\n",
        "\n",
        "Em muitos datasets existem valores ausentes. No Pandas, podemos verificar isso com a função ```isnull()```."
      ],
      "metadata": {
        "id": "GTnK1YrEnPDs"
      },
      "id": "GTnK1YrEnPDs"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.isnull().sum())"
      ],
      "metadata": {
        "id": "1TNqhS8lnUMI"
      },
      "id": "1TNqhS8lnUMI",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.isnull().sum())"
      ],
      "metadata": {
        "id": "sXMaE6x8uVZ4"
      },
      "id": "sXMaE6x8uVZ4",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Essa operação mostra quantos valores faltantes existem em cada coluna."
      ],
      "metadata": {
        "id": "3m7Fhpa2nV0L"
      },
      "id": "3m7Fhpa2nV0L"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Tratamento de valores faltantes**\n",
        "\n",
        "Uma abordagem comum é substituir os valores faltantes pela média da coluna."
      ],
      "metadata": {
        "id": "SEsYmCbvnYZ_"
      },
      "id": "SEsYmCbvnYZ_"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "GVvbECtbR8eE"
      },
      "outputs": [],
      "source": [
        "# fillna substitui valores ausentes\n",
        "\n",
        "# Aqui usamos a média da coluna para preencher valores faltantes\n",
        "\n",
        "print(df.fillna(df.mean()))"
      ],
      "id": "GVvbECtbR8eE"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df1.fillna(df.mean()))"
      ],
      "metadata": {
        "id": "_B_RWS8WuilB"
      },
      "id": "_B_RWS8WuilB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Outra alternativa é remover linhas com valores ausentes:"
      ],
      "metadata": {
        "id": "__d96bRQs2WK"
      },
      "id": "__d96bRQs2WK"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.dropna())"
      ],
      "metadata": {
        "id": "YTK59ZgLs5Lv"
      },
      "id": "YTK59ZgLs5Lv",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "A escolha da estratégia depende do contexto do problema."
      ],
      "metadata": {
        "id": "7wsOTYBLtX4Y"
      },
      "id": "7wsOTYBLtX4Y"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Seleção de colunas**\n",
        "\n",
        "Para trabalhar com variáveis específicas podemos selecionar colunas do DataFrame.\n",
        "\n",
        "Exemplo:"
      ],
      "metadata": {
        "id": "fGJTCealswj7"
      },
      "id": "fGJTCealswj7"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df[\"temperatura\"])"
      ],
      "metadata": {
        "id": "Nf0uxV7jtcAT"
      },
      "id": "Nf0uxV7jtcAT",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Selecionando várias colunas:"
      ],
      "metadata": {
        "id": "oz1FbZiJtfUD"
      },
      "id": "oz1FbZiJtfUD"
    },
    {
      "cell_type": "code",
      "source": [
        "print(df[[\"temperatura\", \"vibracao\"]])"
      ],
      "metadata": {
        "id": "6ZDDlMU9thLM"
      },
      "id": "6ZDDlMU9thLM",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Essa operação é importante para separar:\n",
        "\n",
        "- variáveis de entrada\n",
        "\n",
        "- variável alvo"
      ],
      "metadata": {
        "id": "XusSpw6xthrZ"
      },
      "id": "XusSpw6xthrZ"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Remoção de colunas**\n",
        "\n",
        "Caso existam colunas irrelevantes, podemos removê-las com drop()."
      ],
      "metadata": {
        "id": "YRIDFlbgtqOD"
      },
      "id": "YRIDFlbgtqOD"
    },
    {
      "cell_type": "code",
      "source": [
        "df2=df.drop(\"vibracao\", axis=1)\n",
        "print(df2)"
      ],
      "metadata": {
        "id": "AQZuhgcNtsZQ"
      },
      "id": "AQZuhgcNtsZQ",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Isso ajuda a manter o dataset apenas com as variáveis relevantes para o modelo."
      ],
      "metadata": {
        "id": "ojVxbkDRtvib"
      },
      "id": "ojVxbkDRtvib"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Criação de cópias do dataset**\n",
        "\n",
        "Durante o pré-processamento, é comum criar uma cópia do dataset original para evitar perda de dados."
      ],
      "metadata": {
        "id": "Tv-m_GmStwQT"
      },
      "id": "Tv-m_GmStwQT"
    },
    {
      "cell_type": "code",
      "source": [
        "df_tratado = df.copy()"
      ],
      "metadata": {
        "id": "iTdui39ttyj-"
      },
      "id": "iTdui39ttyj-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Assim, qualquer transformação será aplicada apenas à cópia."
      ],
      "metadata": {
        "id": "KRMpB-Prt3au"
      },
      "id": "KRMpB-Prt3au"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Conclusão**\n",
        "\n",
        "O pré-processamento de dados é uma etapa essencial em qualquer projeto de aprendizado de máquina. Um modelo bem treinado depende diretamente da qualidade dos dados utilizados.\n",
        "\n",
        "Neste notebook, utilizaremos a biblioteca Pandas para:\n",
        "\n",
        "- explorar o dataset\n",
        "\n",
        "- identificar problemas nos dados\n",
        "\n",
        "- tratar valores faltantes\n",
        "\n",
        "- preparar o dataset para o treinamento do modelo\n",
        "\n",
        "Essas etapas são fundamentais para garantir que o algoritmo consiga aprender padrões relevantes e produzir previsões confiáveis."
      ],
      "metadata": {
        "id": "QNJKv0bgt9H7"
      },
      "id": "QNJKv0bgt9H7"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exercício Prático — Pré-processamento e Preparação de Dados com Pandas**\n",
        "##**Contexto**\n",
        "\n",
        "Uma empresa industrial registrou dados de sensores de máquinas para acompanhar o funcionamento dos equipamentos. Antes de usar esses dados em um projeto de Machine Learning, é necessário fazer a análise e a preparação do dataset.\n",
        "\n",
        "O arquivo fornecido possui alguns problemas comuns em bases reais:\n",
        "\n",
        "- valores omissos\n",
        "\n",
        "- outliers\n",
        "\n",
        "- registro duplicado\n",
        "\n",
        "Seu objetivo é explorar o dataset e aplicar técnicas básicas de preparação de dados usando Pandas.\n",
        "\n",
        "##**Objetivos da atividade**\n",
        "\n",
        "Ao final do exercício, você deverá ser capaz de:\n",
        "\n",
        "- carregar um arquivo CSV com Pandas\n",
        "\n",
        "- inspecionar a estrutura do dataset\n",
        "\n",
        "- identificar valores faltantes\n",
        "\n",
        "- identificar possíveis outliers\n",
        "\n",
        "- verificar duplicatas\n",
        "\n",
        "-  aplicar tratamento básico aos dados"
      ],
      "metadata": {
        "id": "HdhSHLvUvJ3o"
      },
      "id": "HdhSHLvUvJ3o"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.x"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}