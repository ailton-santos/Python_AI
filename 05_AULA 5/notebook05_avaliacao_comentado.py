{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jnZC6ibowRIR"
      },
      "source": [
        "# Notebook 05 — Avaliação de Modelos"
      ],
      "id": "jnZC6ibowRIR"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Avaliação de Modelos de Machine Learning**\n",
        "##**Por que avaliar um modelo?**\n",
        "\n",
        "Após treinar um modelo de Machine Learning, é necessário verificar se ele realmente aprendeu padrões úteis a partir dos dados. Esse processo é chamado de avaliação de modelo.\n",
        "\n",
        "O objetivo da avaliação é medir o desempenho do modelo ao realizar previsões.\n",
        "\n",
        "Sem essa etapa, não seria possível saber se o modelo:\n",
        "\n",
        "- está fazendo previsões corretas\n",
        "\n",
        "- está generalizando bem para novos dados\n",
        "\n",
        "- ou se apenas memorizou os dados utilizados no treinamento\n",
        "\n",
        "Em projetos reais de Inteligência Artificial, a avaliação do modelo é essencial para garantir que a solução seja confiável e aplicável em situações reais."
      ],
      "metadata": {
        "id": "ve1liicBw2lW"
      },
      "id": "ve1liicBw2lW"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Dados de treino e dados de teste**\n",
        "\n",
        "Durante o desenvolvimento de modelos de aprendizado de máquina, o dataset geralmente é dividido em dois conjuntos principais:\n",
        "\n",
        "##**Dados de treino (training set)**\n",
        "\n",
        "Esse conjunto é utilizado para ensinar o modelo a reconhecer padrões presentes nos dados.\n",
        "\n",
        "O algoritmo utiliza esses exemplos para ajustar seus parâmetros."
      ],
      "metadata": {
        "id": "hzt9S72kw_Vl"
      },
      "id": "hzt9S72kw_Vl"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Dados de teste (test set)**\n",
        "\n",
        "Esse conjunto é utilizado para avaliar o modelo após o treinamento.\n",
        "\n",
        "Os dados de teste não são apresentados ao modelo durante o treinamento, permitindo verificar se ele consegue generalizar para novos dados."
      ],
      "metadata": {
        "id": "D7c1gdZgxEw3"
      },
      "id": "D7c1gdZgxEw3"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Métricas de avaliação**\n",
        "\n",
        "Para medir o desempenho de um modelo, utilizamos métricas de avaliação.\n",
        "\n",
        "Essas métricas comparam:\n",
        "\n",
        "- as previsões do modelo\n",
        "\n",
        "- com os valores reais do dataset\n",
        "\n",
        "No caso de problemas de classificação, algumas métricas muito utilizadas são:\n",
        "\n",
        "- Accuracy (acurácia)\n",
        "\n",
        "- Matriz de confusão\n",
        "\n",
        "- Precision\n",
        "\n",
        "- Recall\n",
        "\n",
        "- F1-score\n",
        "\n",
        "Neste notebook, vamos focar nas métricas mais básicas para introdução."
      ],
      "metadata": {
        "id": "WRF66jSlxI23"
      },
      "id": "WRF66jSlxI23"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Accuracy (Acurácia)**\n",
        "\n",
        "A acurácia mede a proporção de previsões corretas realizadas pelo modelo.\n",
        "\n",
        "Ela é calculada da seguinte forma:\n",
        "\n",
        "`Accuracy = número de previsões corretas / número total de previsões`\n",
        "\n",
        "Por exemplo:\n",
        "\n",
        "```\n",
        "80 previsões corretas em 100 exemplos\n",
        "accuracy = 0.80 (80%)\n",
        "```\n",
        "\n",
        "Embora seja uma métrica simples, a acurácia é bastante utilizada para obter uma visão geral do desempenho do modelo."
      ],
      "metadata": {
        "id": "u6knD5mtiAtP"
      },
      "id": "u6knD5mtiAtP"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Matriz de Confusão**\n",
        "\n",
        "A matriz de confusão é uma tabela que mostra quantas previsões foram:\n",
        "\n",
        "- corretas\n",
        "\n",
        "- incorretas\n",
        "\n",
        "Ela permite observar como o modelo está cometendo erros.\n",
        "\n",
        "Exemplo de matriz de confusão:\n",
        "\n",
        "![image.png](data:image/png;base64,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)\n",
        "\n",
        "Interpretação:\n",
        "\n",
        "- 40 acertos de casos normais\n",
        "\n",
        "- 12 acertos de casos de falha\n",
        "\n",
        "- 8 erros de classificação\n",
        "\n",
        "A matriz de confusão ajuda a entender onde o modelo está falhando."
      ],
      "metadata": {
        "id": "eWTyiGbfjUva"
      },
      "id": "eWTyiGbfjUva"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Classification Report**\n",
        "\n",
        "O classification report reúne várias métricas importantes em um único relatório:\n",
        "\n",
        "- Precision\n",
        "\n",
        "- Recall\n",
        "\n",
        "- F1-score\n",
        "\n",
        "- Support\n",
        "\n",
        "Essas métricas ajudam a entender melhor o desempenho do modelo em cada classe."
      ],
      "metadata": {
        "id": "jd0v9vJAjpP1"
      },
      "id": "jd0v9vJAjpP1"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Avaliação de modelos com Scikit-learn**\n",
        "\n",
        "A biblioteca Scikit-learn possui diversas funções prontas para calcular métricas de avaliação.\n",
        "\n",
        "As mais utilizadas neste projeto são:\n",
        "\n",
        "- accuracy_score\n",
        "- confusion_matrix\n",
        "- classification_report\n",
        "\n",
        "Essas funções recebem como entrada:\n",
        "\n",
        "- os valores reais\n",
        "\n",
        "- as previsões do modelo"
      ],
      "metadata": {
        "id": "3i8NG1ABj38O"
      },
      "id": "3i8NG1ABj38O"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Importando as funções de avaliação**\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "from sklearn.metrics import accuracy_score\n",
        "from sklearn.metrics import confusion_matrix\n",
        "from sklearn.metrics import classification_report\n",
        "```\n",
        "\n"
      ],
      "metadata": {
        "id": "Au0rsZVukEt3"
      },
      "id": "Au0rsZVukEt3"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Calculando a acurácia**\n",
        "\n",
        "Depois de realizar as previsões com o modelo, podemos calcular a acurácia:\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "# Exemplo:\n",
        "\n",
        "acc = accuracy_score(y_test, y_pred)\n",
        "\n",
        "print(\"Acurácia do modelo:\", acc)\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "xLnnSMFMkHy3"
      },
      "id": "xLnnSMFMkHy3"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Gerando a matriz de confusão**\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "# Exemplo:\n",
        "\n",
        "matriz = confusion_matrix(y_test, y_pred)\n",
        "\n",
        "print(\"Matriz de confusão:\")\n",
        "print(matriz)\n",
        "```\n",
        "\n"
      ],
      "metadata": {
        "id": "n2tQW2D-kUNK"
      },
      "id": "n2tQW2D-kUNK"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Gerando o classification report**\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "# Exemplo:\n",
        "\n",
        "print(classification_report(y_test, y_pred))\n",
        "```\n",
        "\n",
        "Esse relatório apresenta diversas métricas que ajudam a analisar o desempenho do modelo de forma mais detalhada."
      ],
      "metadata": {
        "id": "bxdJUcEZkXkJ"
      },
      "id": "bxdJUcEZkXkJ"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Interpretação dos resultados**\n",
        "\n",
        "Após calcular as métricas, é importante refletir sobre os resultados obtidos.\n",
        "\n",
        "Algumas perguntas importantes são:\n",
        "\n",
        "- O modelo apresentou boa acurácia?\n",
        "\n",
        "- Ele consegue identificar corretamente as duas classes?\n",
        "\n",
        "- Existem muitos erros de classificação?\n",
        "\n",
        "- O modelo poderia ser melhorado com mais dados ou outro algoritmo?\n",
        "\n",
        "Essas reflexões fazem parte do processo de desenvolvimento de sistemas baseados em Inteligência Artificial."
      ],
      "metadata": {
        "id": "Bg_QuU5Okq_E"
      },
      "id": "Bg_QuU5Okq_E"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo prático — Avaliação de modelo com Árvore de Decisão**\n",
        "##**Contexto da base**\n",
        "\n",
        "A base simula dados tratados de sensores industriais, com as colunas:\n",
        "\n",
        "- temperatura\n",
        "\n",
        "- vibracao\n",
        "\n",
        "- pressao\n",
        "\n",
        "- tempo_operacao\n",
        "\n",
        "- falha\n",
        "\n",
        "A coluna falha será a variável alvo:\n",
        "\n",
        "- 0 = funcionamento normal\n",
        "\n",
        "- 1 = possível falha"
      ],
      "metadata": {
        "id": "FjP4ezxLvdmk"
      },
      "id": "FjP4ezxLvdmk"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**1. Importação das bibliotecas**"
      ],
      "metadata": {
        "id": "VLiEVLijvnBl"
      },
      "id": "VLiEVLijvnBl"
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
      ],
      "metadata": {
        "id": "FKuxdV4XvqBM"
      },
      "id": "FKuxdV4XvqBM",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**2. Leitura do arquivo CSV**"
      ],
      "metadata": {
        "id": "jaUo0VSZvutc"
      },
      "id": "jaUo0VSZvutc"
    },
    {
      "cell_type": "code",
      "source": [
        "# Carregar a base de dados tratada\n",
        "df = pd.read_csv(\"dataset_tratado_avaliacao_modelo.csv\")\n",
        "\n",
        "# Visualizar as primeiras linhas\n",
        "df.head()"
      ],
      "metadata": {
        "id": "IKZIAo4Mvxh0"
      },
      "id": "IKZIAo4Mvxh0",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**3. Separação entre variáveis de entrada e variável alvo**"
      ],
      "metadata": {
        "id": "H2upjKRev1lM"
      },
      "id": "H2upjKRev1lM"
    },
    {
      "cell_type": "code",
      "source": [
        "# X = variáveis de entrada\n",
        "X = df.drop(\"falha\", axis=1)\n",
        "\n",
        "# y = variável alvo\n",
        "y = df[\"falha\"]\n",
        "\n",
        "print(\"Formato de X:\", X.shape)\n",
        "print(\"Formato de y:\", y.shape)"
      ],
      "metadata": {
        "id": "q1grQtVYv58N"
      },
      "id": "q1grQtVYv58N",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**4. Divisão da base em treino e teste**"
      ],
      "metadata": {
        "id": "22n7E2HKv8kN"
      },
      "id": "22n7E2HKv8kN"
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size=0.3,\n",
        "    random_state=42\n",
        ")\n",
        "\n",
        "print(\"X_train:\", X_train.shape)\n",
        "print(\"X_test:\", X_test.shape)\n",
        "print(\"y_train:\", y_train.shape)\n",
        "print(\"y_test:\", y_test.shape)"
      ],
      "metadata": {
        "id": "s2GMqyqLwAzl"
      },
      "id": "s2GMqyqLwAzl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Explicação\n",
        "\n",
        "- test_size=0.3 indica que 30% dos dados serão usados para teste.\n",
        "\n",
        "- random_state=42 garante reprodutibilidade da divisão."
      ],
      "metadata": {
        "id": "eiiU7T4CwEhl"
      },
      "id": "eiiU7T4CwEhl"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**5. Criação e treinamento do modelo**"
      ],
      "metadata": {
        "id": "HmbaLr_YzFih"
      },
      "id": "HmbaLr_YzFih"
    },
    {
      "cell_type": "code",
      "source": [
        "# Criar o modelo de árvore de decisão\n",
        "model = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# Treinar o modelo\n",
        "model.fit(X_train, y_train)\n",
        "\n",
        "print(\"Modelo treinado com sucesso.\")"
      ],
      "metadata": {
        "id": "n5pA6lsszHuK"
      },
      "id": "n5pA6lsszHuK",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**6. Realização das predições**"
      ],
      "metadata": {
        "id": "QkPVaTCqzOvB"
      },
      "id": "QkPVaTCqzOvB"
    },
    {
      "cell_type": "code",
      "source": [
        "# Gerar previsões com os dados de teste\n",
        "y_pred = model.predict(X_test)\n",
        "\n",
        "print(\"Primeiras previsões:\", y_pred[:10])\n",
        "print(\"Valores reais:\", y_test.values[:10])"
      ],
      "metadata": {
        "id": "fMyt_0tSzP1y"
      },
      "id": "fMyt_0tSzP1y",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**7. Avaliação do modelo**\n",
        "###**Acurácia**"
      ],
      "metadata": {
        "id": "876DtCM5zRmC"
      },
      "id": "876DtCM5zRmC"
    },
    {
      "cell_type": "code",
      "source": [
        "acc = accuracy_score(y_test, y_pred)\n",
        "print(f\"Acurácia do modelo: {acc:.2f}\")"
      ],
      "metadata": {
        "id": "NgM1OA_KzWKJ"
      },
      "id": "NgM1OA_KzWKJ",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Matriz de confusão**"
      ],
      "metadata": {
        "id": "rR4-Tpl1zYLS"
      },
      "id": "rR4-Tpl1zYLS"
    },
    {
      "cell_type": "code",
      "source": [
        "matriz = confusion_matrix(y_test, y_pred)\n",
        "print(\"Matriz de confusão:\")\n",
        "print(matriz)"
      ],
      "metadata": {
        "id": "W8oQ7caUzasa"
      },
      "id": "W8oQ7caUzasa",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Relatório de classificação**"
      ],
      "metadata": {
        "id": "lZkHn25UzcXC"
      },
      "id": "lZkHn25UzcXC"
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Relatório de classificação:\")\n",
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "id": "z-AjHs2CzfFS"
      },
      "id": "z-AjHs2CzfFS",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**8. Teste com nova amostra**"
      ],
      "metadata": {
        "id": "kMYqiOcVzhcy"
      },
      "id": "kMYqiOcVzhcy"
    },
    {
      "cell_type": "code",
      "source": [
        "# Nova amostra de exemplo\n",
        "nova_amostra = [[82, 4.1, 35, 185]]\n",
        "\n",
        "# Realizar predição\n",
        "pred = model.predict(nova_amostra)\n",
        "\n",
        "print(\"Predição:\", pred[0])\n",
        "\n",
        "if pred[0] == 0:\n",
        "    print(\"Classificação: funcionamento normal\")\n",
        "else:\n",
        "    print(\"Classificação: possível falha\")"
      ],
      "metadata": {
        "id": "XT4vPGDtzl9a"
      },
      "id": "XT4vPGDtzl9a",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Este exemplo mostra um fluxo básico de avaliação de modelo em Machine Learning:\n",
        "\n",
        "1. carregar a base de dados\n",
        "\n",
        "2. separar entradas e saída\n",
        "\n",
        "3. dividir em treino e teste\n",
        "\n",
        "4. treinar o modelo\n",
        "\n",
        "5. realizar predições\n",
        "\n",
        "6. avaliar o desempenho com métricas\n",
        "\n",
        "A Árvore de Decisão foi escolhida porque é um algoritmo simples, visualmente interpretável e adequado para alunos iniciantes.\n",
        "\n",
        "Na avaliação, podem ser observados:\n",
        "\n",
        "- **acurácia**: proporção de acertos do modelo\n",
        "\n",
        "- **matriz de confusão**: quantidade de acertos e erros em cada classe\n",
        "\n",
        "- **classification report**: métricas detalhadas por classe"
      ],
      "metadata": {
        "id": "PoADxuM7zrOq"
      },
      "id": "PoADxuM7zrOq"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Atividade prática para os alunos**\n",
        "1. Alterar o tamanho da divisão dos dados para teste e avaliar o modelo:\n",
        "\n",
        "a. test_size=0.2\n",
        "\n",
        "b. test_size=0.4\n",
        "\n",
        "2. Inserir dentro do modelo de árvore de decisão o seguinte parâmetro destacado, e avaliar o modelo:\n",
        "\n",
        "\n",
        "```\n",
        "DecisionTreeClassifier(**max_depth=3**, random_state=42)\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "SmDdcJ_0z_Gj"
      },
      "id": "SmDdcJ_0z_Gj"
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