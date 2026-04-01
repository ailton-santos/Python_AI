{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a0th9x32QZqQ"
      },
      "source": [
        "# Notebook 03 — Introdução ao Machine Learning"
      ],
      "id": "a0th9x32QZqQ"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Introdução ao Scikit-learn e ao algoritmo de Árvore de Decisão**\n",
        "##**A biblioteca Scikit-learn**\n",
        "\n",
        "O Scikit-learn (também chamado de sklearn) é uma das bibliotecas mais utilizadas em Python para aprendizado de máquina (Machine Learning). Ela fornece diversas ferramentas que permitem criar, treinar e avaliar modelos capazes de aprender padrões a partir de dados.\n",
        "\n",
        "Essa biblioteca foi construída sobre outras bibliotecas científicas muito importantes do ecossistema Python, como:\n",
        "\n",
        "- NumPy – para cálculos numéricos e manipulação de arrays\n",
        "\n",
        "- SciPy – para computação científica\n",
        "\n",
        "- Pandas – para manipulação e análise de dados\n",
        "\n",
        "- Matplotlib – para visualização de dados\n",
        "\n",
        "O objetivo do Scikit-learn é facilitar o desenvolvimento de soluções de machine learning, oferecendo implementações prontas de vários algoritmos.\n",
        "\n",
        "O objetivo do Scikit-learn é facilitar o desenvolvimento de soluções de machine learning, oferecendo implementações prontas de vários algoritmos.\n",
        "\n",
        "Entre as principais funcionalidades da biblioteca estão:\n",
        "\n",
        "- algoritmos de classificação\n",
        "\n",
        "- algoritmos de regressão\n",
        "\n",
        "- algoritmos de clusterização\n",
        "\n",
        "- pré-processamento de dados\n",
        "\n",
        "- divisão de conjuntos de dados em treino e teste\n",
        "\n",
        "- avaliação de modelos\n",
        "\n",
        "Um dos grandes diferenciais do Scikit-learn é que ele possui uma interface simples e padronizada, permitindo que diferentes algoritmos sejam utilizados de maneira muito semelhante.\n",
        "\n",
        "Normalmente, o fluxo de trabalho com Scikit-learn segue algumas etapas principais:\n",
        "\n",
        "1. Carregar ou preparar os dados\n",
        "\n",
        "2. Separar dados de treino e teste\n",
        "\n",
        "3. Escolher o algoritmo\n",
        "\n",
        "4. Treinar o modelo\n",
        "\n",
        "5. Realizar previsões\n",
        "\n",
        "6. Avaliar o desempenho do modelo\n",
        "\n",
        "Esse fluxo será aplicado no exemplo do dataset Iris, um conjunto de dados muito conhecido utilizado para introdução ao aprendizado de máquina."
      ],
      "metadata": {
        "id": "_egKer9Pto3d"
      },
      "id": "_egKer9Pto3d"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris"
      ],
      "metadata": {
        "id": "8jkvctNe0E9i"
      },
      "id": "8jkvctNe0E9i",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# data.data contém as características das flores\n",
        "data = load_iris()\n",
        "print(data.data[:5])"
      ],
      "metadata": {
        "id": "2MxGJXIApEw8"
      },
      "id": "2MxGJXIApEw8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**O algoritmo de Árvore de Decisão**\n",
        "\n",
        "A Árvore de Decisão é um dos algoritmos mais intuitivos de aprendizado de máquina. Ele recebe esse nome porque seu funcionamento se assemelha à estrutura de uma árvore, composta por:\n",
        "\n",
        "- nós de decisão\n",
        "\n",
        "- ramificações\n",
        "\n",
        "- folhas (resultados finais)\n",
        "\n",
        "Cada nó da árvore representa uma pergunta ou condição sobre os dados, e cada ramificação representa um possível resultado dessa condição.\n",
        "\n",
        "Por exemplo, um modelo pode aprender regras como:\n",
        "\n",
        "```\n",
        "Se comprimento da pétala < 2 cm → espécie = setosa\n",
        "Caso contrário → verificar largura da pétala\n",
        "```\n",
        "\n",
        "Essas regras são organizadas em forma de árvore até que o modelo consiga classificar corretamente os dados."
      ],
      "metadata": {
        "id": "hu3LJ3BvvOrf"
      },
      "id": "hu3LJ3BvvOrf"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8srShWq0QZqV"
      },
      "outputs": [],
      "source": [
        "# Importamos ferramentas para dividir dados e criar modelo\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.tree import DecisionTreeClassifier"
      ],
      "id": "8srShWq0QZqV"
    },
    {
      "cell_type": "code",
      "source": [
        "# X representa as variáveis de entrada\n",
        "\n",
        "X = data.data"
      ],
      "metadata": {
        "id": "p3aBPoTsdGG8"
      },
      "id": "p3aBPoTsdGG8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# y representa os rótulos (classes)\n",
        "\n",
        "y = data.target"
      ],
      "metadata": {
        "id": "C8Sl0PAtdOV9"
      },
      "id": "C8Sl0PAtdOV9",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Dividimos dados em treino e teste\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)"
      ],
      "metadata": {
        "id": "BNAMahFrdRT_"
      },
      "id": "BNAMahFrdRT_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos o modelo de árvore de decisão\n",
        "\n",
        "model = DecisionTreeClassifier()"
      ],
      "metadata": {
        "id": "qlr_9KXjdTrS"
      },
      "id": "qlr_9KXjdTrS",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Como funciona uma Árvore de Decisão**\n",
        "\n",
        "Durante o treinamento, o algoritmo analisa os dados e tenta encontrar divisões que melhor separem as classes existentes.\n",
        "\n",
        "Ele faz isso utilizando critérios matemáticos como:\n",
        "\n",
        "- Gini impurity\n",
        "\n",
        "- Entropia\n",
        "\n",
        "- Information gain\n",
        "\n",
        "Essas métricas ajudam o algoritmo a escolher qual característica usar para dividir os dados em cada etapa da árvore.\n",
        "\n",
        "O objetivo é criar divisões que tornem os grupos cada vez mais homogêneos."
      ],
      "metadata": {
        "id": "D6QKhSzqv2xv"
      },
      "id": "D6QKhSzqv2xv"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Treinamento de modelo**"
      ],
      "metadata": {
        "id": "RDhW-r7zp59H"
      },
      "id": "RDhW-r7zp59H"
    },
    {
      "cell_type": "code",
      "source": [
        "# Treinamos o modelo com os dados de treino\n",
        "\n",
        "model.fit(X_train, y_train)\n",
        "\n",
        "print(\"Modelo treinado com sucesso\")"
      ],
      "metadata": {
        "id": "VDE-BmmVdWaz"
      },
      "id": "VDE-BmmVdWaz",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Realizando a predição no conjunto de teste**"
      ],
      "metadata": {
        "id": "t-yR8BdPpxgU"
      },
      "id": "t-yR8BdPpxgU"
    },
    {
      "cell_type": "code",
      "source": [
        "# Usamos o modelo treinado para prever as classes do conjunto de teste\n",
        "y_pred = model.predict(X_test)"
      ],
      "metadata": {
        "id": "fj7oyjRApoiF"
      },
      "id": "fj7oyjRApoiF",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exibimos as primeiras previsões\n",
        "print(\"Primeiras previsões do modelo:\")\n",
        "print(y_pred[:10])"
      ],
      "metadata": {
        "id": "3mt2fkftpp66"
      },
      "id": "3mt2fkftpp66",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exibimos os valores reais para comparação\n",
        "print(\"\\nValores reais:\")\n",
        "print(y_test[:10])"
      ],
      "metadata": {
        "id": "Pr-RCUaEpstl"
      },
      "id": "Pr-RCUaEpstl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Avaliando o desempenho do modelo**"
      ],
      "metadata": {
        "id": "fty210-UqNTg"
      },
      "id": "fty210-UqNTg"
    },
    {
      "cell_type": "code",
      "source": [
        "# Importamos métricas de avaliação\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report"
      ],
      "metadata": {
        "id": "zQpy-t37qPps"
      },
      "id": "zQpy-t37qPps",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Calculamos a acurácia do modelo\n",
        "acc = accuracy_score(y_test, y_pred)"
      ],
      "metadata": {
        "id": "w-IrX0MmqU4b"
      },
      "id": "w-IrX0MmqU4b",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Acurácia do modelo: {acc:.2f}\")"
      ],
      "metadata": {
        "id": "-8STiQjNqWOE"
      },
      "id": "-8STiQjNqWOE",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Matriz de confusão**"
      ],
      "metadata": {
        "id": "ABWgS4Xfqb9e"
      },
      "id": "ABWgS4Xfqb9e"
    },
    {
      "cell_type": "code",
      "source": [
        "# Geramos a matriz de confusão\n",
        "matriz = confusion_matrix(y_test, y_pred)"
      ],
      "metadata": {
        "id": "q8amOQ77qcrH"
      },
      "id": "q8amOQ77qcrH",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Matriz de confusão:\")\n",
        "print(matriz)"
      ],
      "metadata": {
        "id": "J7ENnNihqgnd"
      },
      "id": "J7ENnNihqgnd",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Relatório de classificação**"
      ],
      "metadata": {
        "id": "TwK0oq4oqkSJ"
      },
      "id": "TwK0oq4oqkSJ"
    },
    {
      "cell_type": "code",
      "source": [
        "# Exibimos o relatório com precisão, recall e f1-score\n",
        "nomes_classes = data.target_names"
      ],
      "metadata": {
        "id": "cZfioMHKqiSi"
      },
      "id": "cZfioMHKqiSi",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Relatório de classificação:\")\n",
        "print(classification_report(y_test, y_pred, target_names=nomes_classes))"
      ],
      "metadata": {
        "id": "wv5IJTAWqsyq"
      },
      "id": "wv5IJTAWqsyq",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo prático com o dataset Iris**\n",
        "\n",
        "No dataset Iris, cada flor possui quatro características principais:\n",
        "\n",
        "- comprimento da sépala\n",
        "\n",
        "- largura da sépala\n",
        "\n",
        "- comprimento da pétala\n",
        "\n",
        "- largura da pétala\n",
        "\n",
        "A partir dessas medidas, o algoritmo aprende a identificar três espécies diferentes:\n",
        "\n",
        "- Iris setosa\n",
        "\n",
        "- Iris versicolor\n",
        "\n",
        "- Iris virginica\n",
        "\n",
        "Durante o treinamento, a árvore de decisão analisa essas características e cria regras para separar as espécies.\n",
        "\n",
        "Por exemplo, ela pode aprender algo como:\n",
        "\n",
        "```\n",
        "Se petal length < 2.5 → setosa\n",
        "\n",
        "Se petal length ≥ 2.5 e petal width < 1.8 → versicolor\n",
        "\n",
        "Se petal width ≥ 1.8 → virginica\n",
        "```\n",
        "\n",
        "Assim, quando um novo exemplo é apresentado ao modelo, ele percorre a árvore seguindo as condições até chegar a uma classe prevista."
      ],
      "metadata": {
        "id": "10tUSH67wR-R"
      },
      "id": "10tUSH67wR-R"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Gráficos com os tipos de iris**\n",
        "Organizando os dados em um DataFrame"
      ],
      "metadata": {
        "id": "jNESI4BEqyeS"
      },
      "id": "jNESI4BEqyeS"
    },
    {
      "cell_type": "code",
      "source": [
        "# Importamos pandas para organizar melhor os dados\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "AW9mxHVBq2ev"
      },
      "id": "AW9mxHVBq2ev",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos um DataFrame com as características das flores\n",
        "df_iris = pd.DataFrame(data.data, columns=data.feature_names)"
      ],
      "metadata": {
        "id": "IRyoGy7Nq4rg"
      },
      "id": "IRyoGy7Nq4rg",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Adicionamos a coluna com a classe numérica\n",
        "df_iris[\"target\"] = data.target"
      ],
      "metadata": {
        "id": "qvUadWGFq6f1"
      },
      "id": "qvUadWGFq6f1",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos uma coluna com o nome da espécie\n",
        "df_iris[\"species\"] = df_iris[\"target\"].map({\n",
        "    0: data.target_names[0],\n",
        "    1: data.target_names[1],\n",
        "    2: data.target_names[2]\n",
        "})"
      ],
      "metadata": {
        "id": "MH5w4ecMq9XD"
      },
      "id": "MH5w4ecMq9XD",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exibimos as primeiras linhas\n",
        "df_iris.head()"
      ],
      "metadata": {
        "id": "Uk2Z-dB6rA2m"
      },
      "id": "Uk2Z-dB6rA2m",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Gráfico de dispersão: comprimento x largura da pétala**\n",
        "\n",
        "Esse gráfico costuma separar bem as espécies."
      ],
      "metadata": {
        "id": "L4OepKlOrGHO"
      },
      "id": "L4OepKlOrGHO"
    },
    {
      "cell_type": "code",
      "source": [
        "# Importamos matplotlib para gerar gráficos\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "DOdXqFhqrJAS"
      },
      "id": "DOdXqFhqrJAS",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Separamos os dados por espécie\n",
        "setosa = df_iris[df_iris[\"species\"] == \"setosa\"]\n",
        "versicolor = df_iris[df_iris[\"species\"] == \"versicolor\"]\n",
        "virginica = df_iris[df_iris[\"species\"] == \"virginica\"]"
      ],
      "metadata": {
        "id": "cyDg6mi6rL7X"
      },
      "id": "cyDg6mi6rL7X",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos o gráfico\n",
        "plt.figure(figsize=(8, 6))\n",
        "plt.scatter(setosa[\"petal length (cm)\"], setosa[\"petal width (cm)\"], label=\"setosa\")\n",
        "plt.scatter(versicolor[\"petal length (cm)\"], versicolor[\"petal width (cm)\"], label=\"versicolor\")\n",
        "plt.scatter(virginica[\"petal length (cm)\"], virginica[\"petal width (cm)\"], label=\"virginica\")"
      ],
      "metadata": {
        "id": "ucpdBrR_rPpL"
      },
      "id": "ucpdBrR_rPpL",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Título e rótulos\n",
        "plt.title(\"Dispersão das espécies de Iris\")\n",
        "plt.xlabel(\"Comprimento da pétala (cm)\")\n",
        "plt.ylabel(\"Largura da pétala (cm)\")\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "# Exibimos o gráfico\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "qlplQMw7rTKt"
      },
      "id": "qlplQMw7rTKt",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Gráfico de dispersão: comprimento x largura da sépala**"
      ],
      "metadata": {
        "id": "J46z2V1frh5h"
      },
      "id": "J46z2V1frh5h"
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 6))\n",
        "\n",
        "plt.scatter(setosa[\"sepal length (cm)\"], setosa[\"sepal width (cm)\"], label=\"setosa\")\n",
        "plt.scatter(versicolor[\"sepal length (cm)\"], versicolor[\"sepal width (cm)\"], label=\"versicolor\")\n",
        "plt.scatter(virginica[\"sepal length (cm)\"], virginica[\"sepal width (cm)\"], label=\"virginica\")\n",
        "\n",
        "plt.title(\"Dispersão das espécies de Iris pela sépala\")\n",
        "plt.xlabel(\"Comprimento da sépala (cm)\")\n",
        "plt.ylabel(\"Largura da sépala (cm)\")\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "SrdINuCVriZi"
      },
      "id": "SrdINuCVriZi",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Gráfico de barras com a quantidade de exemplos por espécie**"
      ],
      "metadata": {
        "id": "Znd37qZgro86"
      },
      "id": "Znd37qZgro86"
    },
    {
      "cell_type": "code",
      "source": [
        "# Contamos quantas flores existem de cada espécie\n",
        "contagem = df_iris[\"species\"].value_counts()"
      ],
      "metadata": {
        "id": "z1DSe6QarrDm"
      },
      "id": "z1DSe6QarrDm",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos o gráfico de barras\n",
        "plt.figure(figsize=(8, 5))\n",
        "plt.bar(contagem.index, contagem.values)\n",
        "\n",
        "plt.title(\"Quantidade de amostras por espécie\")\n",
        "plt.xlabel(\"Espécie\")\n",
        "plt.ylabel(\"Quantidade\")\n",
        "plt.grid(axis=\"y\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "-Lk5pDiSr2ox"
      },
      "id": "-Lk5pDiSr2ox",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Fazendo uma predição com uma nova flor**\n",
        "\n",
        "Aqui o aluno pode testar valores manualmente."
      ],
      "metadata": {
        "id": "d2Xky18zr_hB"
      },
      "id": "d2Xky18zr_hB"
    },
    {
      "cell_type": "code",
      "source": [
        "# Exemplo de nova flor:\n",
        "# [sepal length, sepal width, petal length, petal width]\n",
        "nova_flor = [[5.1, 3.5, 1.4, 0.2]]"
      ],
      "metadata": {
        "id": "QbOYaYnIsHTg"
      },
      "id": "QbOYaYnIsHTg",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# O modelo prevê a classe\n",
        "predicao = model.predict(nova_flor)"
      ],
      "metadata": {
        "id": "I1CmN0DmsJ0v"
      },
      "id": "I1CmN0DmsJ0v",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Convertendo a classe numérica para o nome da espécie\n",
        "especie_prevista = data.target_names[predicao[0]]\n",
        "\n",
        "print(\"Classe prevista:\", predicao[0])\n",
        "print(\"Espécie prevista:\", especie_prevista)"
      ],
      "metadata": {
        "id": "LfxcttLYsOk7"
      },
      "id": "LfxcttLYsOk7",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Teste interativo para o aluno**"
      ],
      "metadata": {
        "id": "DcXZ99HSsSMv"
      },
      "id": "DcXZ99HSsSMv"
    },
    {
      "cell_type": "code",
      "source": [
        "# Entrada manual dos dados da flor\n",
        "sepal_length = float(input(\"Digite o comprimento da sépala (cm): \"))\n",
        "sepal_width = float(input(\"Digite a largura da sépala (cm): \"))\n",
        "petal_length = float(input(\"Digite o comprimento da pétala (cm): \"))\n",
        "petal_width = float(input(\"Digite a largura da pétala (cm): \"))"
      ],
      "metadata": {
        "id": "PwzQSDIbsSz5"
      },
      "id": "PwzQSDIbsSz5",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Organizamos os dados no formato esperado pelo modelo\n",
        "amostra = [[sepal_length, sepal_width, petal_length, petal_width]]"
      ],
      "metadata": {
        "id": "2X8JZxiRsXIM"
      },
      "id": "2X8JZxiRsXIM",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Fazemos a previsão\n",
        "pred = model.predict(amostra)"
      ],
      "metadata": {
        "id": "VZmdXl9ysZLa"
      },
      "id": "VZmdXl9ysZLa",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Mostramos o resultado\n",
        "print(\"Espécie prevista:\", data.target_names[pred[0]])"
      ],
      "metadata": {
        "id": "HoTjuVeQscW0"
      },
      "id": "HoTjuVeQscW0",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Reflexão final**\n",
        "\n",
        "- O modelo conseguiu prever corretamente as espécies?\n",
        "- Quais características ajudaram mais na separação das flores?\n",
        "- Em qual gráfico a distinção entre as classes ficou mais visível?\n",
        "- Como esse processo se relaciona com problemas reais de classificação em IA?"
      ],
      "metadata": {
        "id": "LF2o6SnzskLY"
      },
      "id": "LF2o6SnzskLY"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exercício Prático – Classificação com Árvore de Decisão**\n",
        "##**Objetivo**\n",
        "\n",
        "Neste exercício você irá construir um modelo de classificação utilizando o algoritmo de Árvore de Decisão.\n",
        "\n",
        "Ao final da atividade você será capaz de:\n",
        "\n",
        "- dividir um dataset em dados de treino e teste\n",
        "\n",
        "- treinar um modelo de aprendizado de máquina\n",
        "\n",
        "- realizar predições\n",
        "\n",
        "- avaliar o desempenho do modelo\n",
        "\n",
        "O dataset utilizado será o Iris, que contém informações sobre flores de três espécies diferentes."
      ],
      "metadata": {
        "id": "C1DUTI9Gxov3"
      },
      "id": "C1DUTI9Gxov3"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 1 – Importar as bibliotecas**\n",
        "\n",
        "Complete o código abaixo para importar as bibliotecas necessárias."
      ],
      "metadata": {
        "id": "jDiLlAxhx7ma"
      },
      "id": "jDiLlAxhx7ma"
    },
    {
      "cell_type": "code",
      "source": [
        "# Importar dataset iris\n",
        "from sklearn.datasets import ______\n",
        "\n",
        "# Importar função para dividir dados\n",
        "from sklearn.model_selection import ______\n",
        "\n",
        "# Importar algoritmo de árvore de decisão\n",
        "from sklearn.tree import ______\n",
        "\n",
        "# Importar métrica de avaliação\n",
        "from sklearn.metrics import ______"
      ],
      "metadata": {
        "id": "NDQkYCoyx-xS"
      },
      "id": "NDQkYCoyx-xS",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 2 – Carregar o dataset**\n",
        "\n",
        "Complete o código para carregar o dataset Iris."
      ],
      "metadata": {
        "id": "gjdg8mq_yDbD"
      },
      "id": "gjdg8mq_yDbD"
    },
    {
      "cell_type": "code",
      "source": [
        "# Carregar dataset\n",
        "iris = ______()\n",
        "\n",
        "# Variáveis de entrada\n",
        "X = iris.data\n",
        "\n",
        "# Variável alvo (espécie da flor)\n",
        "y = iris.target\n",
        "\n",
        "print(\"Quantidade de amostras:\", len(X))"
      ],
      "metadata": {
        "id": "tHYQspOGyINs"
      },
      "id": "tHYQspOGyINs",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 3 – Dividir dados em treino e teste**\n",
        "\n",
        "Agora vamos dividir os dados em dois conjuntos:\n",
        "\n",
        "- treino → usado para ensinar o modelo\n",
        "\n",
        "- teste → usado para avaliar o modelo\n",
        "\n",
        "Complete o código abaixo."
      ],
      "metadata": {
        "id": "UcAZ7e64yMuz"
      },
      "id": "UcAZ7e64yMuz"
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size = _____,\n",
        "    random_state = _____\n",
        ")"
      ],
      "metadata": {
        "id": "d7k6mwchyZHA"
      },
      "id": "d7k6mwchyZHA",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 4 – Criar o modelo**\n",
        "\n",
        "Agora vamos criar o modelo de Árvore de Decisão."
      ],
      "metadata": {
        "id": "_HJopFt_ylwM"
      },
      "id": "_HJopFt_ylwM"
    },
    {
      "cell_type": "code",
      "source": [
        "# Criar o modelo\n",
        "model = ______()\n",
        "\n",
        "# Treinar o modelo\n",
        "model.fit(_____, _____)\n",
        "\n",
        "print(\"Modelo treinado com sucesso!\")"
      ],
      "metadata": {
        "id": "Fyf4HH8VyoGl"
      },
      "id": "Fyf4HH8VyoGl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 5 – Realizar predições**\n",
        "\n",
        "Depois do treinamento, podemos usar o modelo para prever a classe das flores no conjunto de teste.\n",
        "\n",
        "Complete o código:"
      ],
      "metadata": {
        "id": "AXE9dLdwyrbK"
      },
      "id": "AXE9dLdwyrbK"
    },
    {
      "cell_type": "code",
      "source": [
        "# Fazer previsões\n",
        "y_pred = model._____(X_test)\n",
        "\n",
        "# Mostrar primeiras previsões\n",
        "print(\"Previsões:\")\n",
        "print(y_pred[:10])\n",
        "\n",
        "print(\"Valores reais:\")\n",
        "print(y_test[:10])"
      ],
      "metadata": {
        "id": "r48vKFlsyvna"
      },
      "id": "r48vKFlsyvna",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 6 – Avaliar o modelo**\n",
        "\n",
        "Agora vamos calcular a acurácia, que indica a proporção de previsões corretas."
      ],
      "metadata": {
        "id": "EXmC4q_wy3Fq"
      },
      "id": "EXmC4q_wy3Fq"
    },
    {
      "cell_type": "code",
      "source": [
        "acc = accuracy_score(_____, _____)\n",
        "\n",
        "print(\"Acurácia do modelo:\", acc)"
      ],
      "metadata": {
        "id": "shSHwL3CzDkA"
      },
      "id": "shSHwL3CzDkA",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 7 – Fazer uma nova previsão**\n",
        "\n",
        "Agora vamos testar o modelo com uma nova flor.\n",
        "\n",
        "Complete o código:"
      ],
      "metadata": {
        "id": "IBiFsXZ1zMZ6"
      },
      "id": "IBiFsXZ1zMZ6"
    },
    {
      "cell_type": "code",
      "source": [
        "# Nova flor\n",
        "nova_flor = [[5.1, 3.5, 1.4, 0.2]]\n",
        "\n",
        "# Realizar previsão\n",
        "pred = model._____(nova_flor)\n",
        "\n",
        "print(\"Classe prevista:\", pred)\n",
        "print(\"Espécie:\", iris.target_names[pred[0]])"
      ],
      "metadata": {
        "id": "L6Hd79sLzTW9"
      },
      "id": "L6Hd79sLzTW9",
      "execution_count": null,
      "outputs": []
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