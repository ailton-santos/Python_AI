{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WHPVLrLabn4Y"
      },
      "source": [
        "# Notebook 09 — Aplicação de IA em Dados Industriais"
      ],
      "id": "WHPVLrLabn4Y"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Detecção de risco de falha em equipamentos**"
      ],
      "metadata": {
        "id": "-zx-RckFdF8B"
      },
      "id": "-zx-RckFdF8B"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 1. Contextualização**\n",
        "###**Indústria 4.0 e análise de dados**\n",
        "\n",
        "Com o avanço da Indústria 4.0, empresas passaram a coletar grandes volumes de dados por meio de sensores instalados em máquinas industriais.\n",
        "\n",
        "Esses dados permitem:\n",
        "\n",
        "- monitoramento contínuo de equipamentos\n",
        "\n",
        "- identificação de padrões de comportamento\n",
        "\n",
        "- detecção precoce de falhas\n",
        "\n",
        "- redução de custos com manutenção\n",
        "\n",
        "Neste contexto, a análise de dados combinada com Inteligência Artificial possibilita a criação de modelos capazes de prever riscos de falha antes que eles ocorram."
      ],
      "metadata": {
        "id": "uv91q5IAdOJh"
      },
      "id": "uv91q5IAdOJh"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 2. Problema do projeto**\n",
        "\n",
        "Uma empresa industrial deseja desenvolver um modelo capaz de:\n",
        "\n",
        "👉 identificar situações que indiquem risco de falha em equipamentos\n",
        "\n",
        "No entanto, o dataset apresenta problemas comuns:\n",
        "\n",
        "- valores faltantes\n",
        "\n",
        "- outliers\n",
        "\n",
        "- inconsistências"
      ],
      "metadata": {
        "id": "A-Gcgfopdaxa"
      },
      "id": "A-Gcgfopdaxa"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🎯 3. Objetivo do notebook**\n",
        "\n",
        "Neste notebook, você irá:\n",
        "\n",
        "- analisar o dataset\n",
        "\n",
        "- tratar dados inconsistentes\n",
        "\n",
        "- preparar os dados\n",
        "\n",
        "- treinar um modelo de Machine Learning\n",
        "\n",
        "- realizar predições\n",
        "\n",
        "- avaliar o desempenho"
      ],
      "metadata": {
        "id": "IwjateoqdihB"
      },
      "id": "IwjateoqdihB"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🧠 4. Algoritmo utilizado**\n",
        "###**Árvore de decisão (Decision Tree)**\n",
        "\n",
        "A Árvore de Decisão é um algoritmo de classificação que funciona como uma sequência de decisões lógicas.\n",
        "\n",
        "Ela divide os dados com base em regras, como:\n",
        "\n",
        "```\n",
        "Se temperatura > 80 → risco alto\n",
        "Se vibração > 4 → risco alto\n",
        "```\n",
        "\n",
        "Vantagens:\n",
        "\n",
        "- fácil interpretação\n",
        "\n",
        "- bom desempenho em problemas simples\n",
        "\n",
        "- não exige normalização dos dados"
      ],
      "metadata": {
        "id": "SfytrXMwdsZB"
      },
      "id": "SfytrXMwdsZB"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 5. Etapa 1 — Análise do dataset**\n",
        "###**📌 Objetivo**\n",
        "\n",
        "Compreender a estrutura dos dados antes de aplicar qualquer modelo."
      ],
      "metadata": {
        "id": "-Wf4SoJieII5"
      },
      "id": "-Wf4SoJieII5"
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Código**"
      ],
      "metadata": {
        "id": "pJ4h_PsxfLSq"
      },
      "id": "pJ4h_PsxfLSq"
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv(\"dataset_sensores_industriais_200_registros.csv\")\n",
        "\n",
        "df.head()"
      ],
      "metadata": {
        "id": "7wPU4iNSfFQB"
      },
      "id": "7wPU4iNSfFQB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Informações gerais**"
      ],
      "metadata": {
        "id": "zvGUuBy-fPsa"
      },
      "id": "zvGUuBy-fPsa"
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "LKBWOBLcfURK"
      },
      "id": "LKBWOBLcfURK",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Estatísticas descritivas**"
      ],
      "metadata": {
        "id": "KjuNg78TfWhK"
      },
      "id": "KjuNg78TfWhK"
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "id": "6e_pbpUKfcux"
      },
      "id": "6e_pbpUKfcux",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**🔍 Identificação de valores faltantes**"
      ],
      "metadata": {
        "id": "_RLlhV4yfjya"
      },
      "id": "_RLlhV4yfjya"
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "id": "KT8m9lXnfmBq"
      },
      "id": "KT8m9lXnfmBq",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**📊 Visualização de outliers**"
      ],
      "metadata": {
        "id": "8elc2f2ufohq"
      },
      "id": "8elc2f2ufohq"
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "df.boxplot(figsize=(10,6))\n",
        "plt.title(\"Visualização de possíveis outliers\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "heeSdlyCfqqy"
      },
      "id": "heeSdlyCfqqy",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**🧠 Explicação didática**\n",
        "\n",
        "Nesta etapa, você está:\n",
        "\n",
        "- entendendo os dados\n",
        "\n",
        "- identificando problemas\n",
        "\n",
        "- preparando o terreno para o modelo"
      ],
      "metadata": {
        "id": "_RZ2hnqffvFa"
      },
      "id": "_RZ2hnqffvFa"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 6. Etapa 2 — Preparação dos dados**\n",
        "###**📌 Objetivo**\n",
        "\n",
        "Garantir que os dados estejam adequados para o treinamento do modelo."
      ],
      "metadata": {
        "id": "YcTtczOsfz1y"
      },
      "id": "YcTtczOsfz1y"
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Tratamento de valores faltantes**"
      ],
      "metadata": {
        "id": "XOUCBMq2f7L6"
      },
      "id": "XOUCBMq2f7L6"
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.fillna(df.mean(numeric_only=True))"
      ],
      "metadata": {
        "id": "yLtj2THNf_Hj"
      },
      "id": "yLtj2THNf_Hj",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "👉 Substitui valores faltantes pela média da coluna"
      ],
      "metadata": {
        "id": "EZoAQhtDgBZS"
      },
      "id": "EZoAQhtDgBZS"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Tratamento de outliers (exemplo simples)**\n",
        "\n",
        "***Observação: executar o tratamento dos outliers e treinar e realizar a predição. Em seguida, realizar o treinamento e a predição do modelo novamente, agora sem tratar os outliers.***\n",
        "\n",
        "Comparar os resultados com e sem tratamento dos outliers."
      ],
      "metadata": {
        "id": "k66Sn6FvgEZN"
      },
      "id": "k66Sn6FvgEZN"
    },
    {
      "cell_type": "code",
      "source": [
        "for col in df.select_dtypes(include=['float64', 'int64']):\n",
        "    q1 = df[col].quantile(0.25)\n",
        "    q3 = df[col].quantile(0.75)\n",
        "    iqr = q3 - q1\n",
        "\n",
        "    limite_inferior = q1 - 1.5 * iqr\n",
        "    limite_superior = q3 + 1.5 * iqr\n",
        "\n",
        "    df[col] = df[col].clip(limite_inferior, limite_superior)"
      ],
      "metadata": {
        "id": "XjMdZAROgJK8"
      },
      "id": "XjMdZAROgJK8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Separação de entrada e saída**"
      ],
      "metadata": {
        "id": "VVXVFcZNgL58"
      },
      "id": "VVXVFcZNgL58"
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop(\"falha\", axis=1)\n",
        "y = df[\"falha\"]"
      ],
      "metadata": {
        "id": "IzQvtOS1gWF-"
      },
      "id": "IzQvtOS1gWF-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 7. Etapa 3 — Treinamento do modelo**\n",
        "###**Divisão treino e teste**"
      ],
      "metadata": {
        "id": "HLGApQDogax1"
      },
      "id": "HLGApQDogax1"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X, y,\n",
        "    test_size=0.3,\n",
        "    random_state=42\n",
        ")"
      ],
      "metadata": {
        "id": "w9szvcyngfR2"
      },
      "id": "w9szvcyngfR2",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "####**Treinamento com Decision Tree**"
      ],
      "metadata": {
        "id": "Ovy6gR7dgizP"
      },
      "id": "Ovy6gR7dgizP"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.tree import DecisionTreeClassifier\n",
        "\n",
        "model = DecisionTreeClassifier()\n",
        "\n",
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "id": "Eymyt2HUgk-_"
      },
      "id": "Eymyt2HUgk-_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 8. Etapa 4 — Predição**"
      ],
      "metadata": {
        "id": "ZAmPJdyFgpuX"
      },
      "id": "ZAmPJdyFgpuX"
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test)\n",
        "\n",
        "print(y_pred[:10])"
      ],
      "metadata": {
        "id": "24b2mh69gpAf"
      },
      "id": "24b2mh69gpAf",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exemplos para teste de predição do modelo treinado\n",
        "amostras_teste = [\n",
        "    [72, 3.1, 31, 140],   # tendência: normal\n",
        "    [88, 5.2, 41, 230],   # tendência: falha\n",
        "    [76, 3.6, 33, 165],   # tendência: normal\n",
        "    [95, 6.4, 45, 260],   # tendência: falha\n",
        "    [73, 5.0, 32, 150]    # caso intermediário\n",
        "]\n",
        "\n",
        "predicoes = model.predict(amostras_teste)\n",
        "\n",
        "for i, pred in enumerate(predicoes):\n",
        "    print(f\"Amostra {i+1}: {amostras_teste[i]}\")\n",
        "    if pred == 0:\n",
        "        print(\"Predição: funcionamento normal\")\n",
        "    else:\n",
        "        print(\"Predição: possível falha\")\n",
        "    print(\"-\" * 40)"
      ],
      "metadata": {
        "id": "HKQU0OTbZoM9"
      },
      "id": "HKQU0OTbZoM9",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 9. Etapa 5 — Avaliação do modelo**\n",
        "###**Accuracy**"
      ],
      "metadata": {
        "id": "UjNd1MeVguqR"
      },
      "id": "UjNd1MeVguqR"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "\n",
        "print(\"Accuracy:\", accuracy)"
      ],
      "metadata": {
        "id": "AVO1ew_YgzSR"
      },
      "id": "AVO1ew_YgzSR",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Matriz de confusão**"
      ],
      "metadata": {
        "id": "1AizUytjg1Ap"
      },
      "id": "1AizUytjg1Ap"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix\n",
        "\n",
        "cm = confusion_matrix(y_test, y_pred)\n",
        "\n",
        "print(cm)"
      ],
      "metadata": {
        "id": "g6EZJ0wEg4K5"
      },
      "id": "g6EZJ0wEg4K5",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Classification Report (opcional)**"
      ],
      "metadata": {
        "id": "QlBynL3gg8sp"
      },
      "id": "QlBynL3gg8sp"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "id": "yU84d8t9g_sq"
      },
      "id": "yU84d8t9g_sq",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 10. Interpretação dos resultados**\n",
        "###**Perguntas orientadoras**\n",
        "\n",
        "- O modelo apresentou boa acurácia?\n",
        "\n",
        "- Ele erra mais em qual classe?\n",
        "\n",
        "- Os dados influenciaram o desempenho?\n",
        "\n",
        "- O tratamento de outliers ajudou?"
      ],
      "metadata": {
        "id": "4H0s4ZHEhGga"
      },
      "id": "4H0s4ZHEhGga"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 11. Aplicação no contexto industrial**\n",
        "\n",
        "Esse modelo pode ser utilizado para:\n",
        "\n",
        "- prever falhas em máquinas\n",
        "\n",
        "- apoiar manutenção preventiva\n",
        "\n",
        "- reduzir custos operacionais\n",
        "\n",
        "- evitar paradas inesperadas"
      ],
      "metadata": {
        "id": "7A17SM8ihP3j"
      },
      "id": "7A17SM8ihP3j"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 12. Boas práticas aplicadas**\n",
        "\n",
        "Neste projeto você aplicou:\n",
        "\n",
        "✔ análise exploratória\n",
        "\n",
        "✔ tratamento de dados\n",
        "\n",
        "✔ separação treino/teste\n",
        "\n",
        "✔ uso de algoritmo supervisionado\n",
        "\n",
        "✔ avaliação de desempenho"
      ],
      "metadata": {
        "id": "06lxew43hWwr"
      },
      "id": "06lxew43hWwr"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 13. Desafio opcional**\n",
        "###**K-Means (clusterização)**\n",
        "\n",
        "Você pode testar uma abordagem alternativa:"
      ],
      "metadata": {
        "id": "wFi6UblMheor"
      },
      "id": "wFi6UblMheor"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.cluster import KMeans\n",
        "\n",
        "kmeans = KMeans(n_clusters=2)\n",
        "\n",
        "kmeans.fit(X)"
      ],
      "metadata": {
        "id": "wWyU1uFohtXM"
      },
      "id": "wWyU1uFohtXM",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exemplos para teste de predição do modelo treinado\n",
        "amostras_teste = [\n",
        "    [72, 3.1, 31, 140],   # tendência: normal\n",
        "    [88, 5.2, 41, 230],   # tendência: falha\n",
        "    [76, 3.6, 33, 165],   # tendência: normal\n",
        "    [95, 6.4, 45, 260],   # tendência: falha\n",
        "    [73, 5.0, 32, 150]    # caso intermediário\n",
        "]\n",
        "\n",
        "predicoes = kmeans.predict(amostras_teste)\n",
        "\n",
        "for i, pred in enumerate(predicoes):\n",
        "    print(f\"Amostra {i+1}: {amostras_teste[i]}\")\n",
        "    if pred == 0:\n",
        "        print(\"Predição: funcionamento normal\")\n",
        "    else:\n",
        "        print(\"Predição: possível falha\")\n",
        "    print(\"-\" * 40)"
      ],
      "metadata": {
        "id": "wgQqHXHjmuhl"
      },
      "id": "wgQqHXHjmuhl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "👉 Compare os resultados com o modelo supervisionado."
      ],
      "metadata": {
        "id": "R92J4uH9h3Ms"
      },
      "id": "R92J4uH9h3Ms"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔷 14. Conclusão**\n",
        "\n",
        "Neste projeto, foi possível:\n",
        "\n",
        "- aplicar técnicas de ciência de dados\n",
        "\n",
        "- construir um modelo de Machine Learning\n",
        "\n",
        "- interpretar resultados\n",
        "\n",
        "- conectar a solução com um problema real da indústria"
      ],
      "metadata": {
        "id": "dD-h-8Fmh4h1"
      },
      "id": "dD-h-8Fmh4h1"
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