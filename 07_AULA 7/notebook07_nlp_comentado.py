{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d0RrXESsbFJX"
      },
      "source": [
        "# Notebook 07 — Processamento de Linguagem Natural"
      ],
      "id": "d0RrXESsbFJX"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Processamento de Linguagem Natural (NLP)**\n",
        "##**O que é NLP?**\n",
        "\n",
        "O Processamento de Linguagem Natural ou NLP (Natural Language Processing) é uma área da Inteligência Artificial que permite aos computadores entender, analisar, interpretar e gerar linguagem humana.\n",
        "\n",
        "Em outras palavras, o NLP busca fazer com que máquinas consigam trabalhar com textos e falas de maneira semelhante à forma como os seres humanos lidam com a linguagem.\n",
        "\n",
        "Como os computadores não entendem palavras da mesma forma que as pessoas, é necessário transformar os textos em formatos que possam ser processados matematicamente."
      ],
      "metadata": {
        "id": "aqLs0dkfb5vc"
      },
      "id": "aqLs0dkfb5vc"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Onde o NLP é aplicado?**\n",
        "\n",
        "O NLP está presente em várias tecnologias do dia a dia. Alguns exemplos são:\n",
        "\n",
        "- chatbots e assistentes virtuais\n",
        "\n",
        "- tradutores automáticos\n",
        "\n",
        "- corretores ortográficos\n",
        "\n",
        "- análise de sentimentos\n",
        "\n",
        "- classificação automática de textos\n",
        "\n",
        "- busca inteligente em documentos\n",
        "\n",
        "- resumo automático\n",
        "\n",
        "- recomendação de respostas em atendimentos\n",
        "\n",
        "Na indústria e nas empresas, o NLP pode ser usado para:\n",
        "\n",
        "- analisar mensagens de clientes\n",
        "\n",
        "- classificar chamados técnicos\n",
        "\n",
        "- identificar reclamações recorrentes\n",
        "\n",
        "- organizar documentos\n",
        "\n",
        "- automatizar respostas"
      ],
      "metadata": {
        "id": "ZtRxwUl0cDvd"
      },
      "id": "ZtRxwUl0cDvd"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Como um computador trabalha com palavras?**\n",
        "\n",
        "Antes de comparar ou analisar palavras, o texto normalmente passa por algumas etapas de preparação.\n",
        "\n",
        "Essas etapas podem incluir:\n",
        "\n",
        "1. converter tudo para minúsculas\n",
        "\n",
        "2. remover pontuação\n",
        "\n",
        "3. separar o texto em palavras\n",
        "\n",
        "4. remover palavras pouco relevantes\n",
        "\n",
        "5. contar frequência das palavras\n",
        "\n",
        "6. comparar palavras ou frases\n",
        "\n",
        "Esse processo ajuda a transformar o texto em uma estrutura mais adequada para análise computacional."
      ],
      "metadata": {
        "id": "MRfF5MDpcNlr"
      },
      "id": "MRfF5MDpcNlr"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Formas de identificar ou comparar palavras**\n",
        "\n",
        "Existem diferentes maneiras de trabalhar com palavras em NLP. Para alunos iniciantes, as principais são:\n",
        "\n",
        "###**1. Tokenização**\n",
        "\n",
        "A **tokenização** é o processo de dividir um texto em partes menores, geralmente palavras.\n",
        "\n",
        "Exemplo:\n",
        "\n",
        "```\n",
        "\"Eu gosto de inteligência artificial\"\n",
        "```\n",
        "\n",
        "pode ser dividido em:\n",
        "\n",
        "```\n",
        "[\"Eu\", \"gosto\", \"de\", \"inteligência\", \"artificial\"]\n",
        "```\n",
        "\n",
        "Essas partes são chamadas de **tokens**."
      ],
      "metadata": {
        "id": "Syg91IANclnr"
      },
      "id": "Syg91IANclnr"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**2. Frequência de palavras**\n",
        "\n",
        "Uma forma simples de analisar um texto é contar quantas vezes cada palavra aparece.\n",
        "\n",
        "Isso ajuda a identificar termos mais importantes ou mais repetidos em um conjunto de textos.\n",
        "\n",
        "Exemplo:\n",
        "\n",
        "```\n",
        "\"IA é importante e IA está em crescimento\"\n",
        "```\n",
        "\n",
        "A palavra **IA** aparece 2 vezes."
      ],
      "metadata": {
        "id": "x_6gqXF3c9wu"
      },
      "id": "x_6gqXF3c9wu"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**3. Comparação por ocorrência**\n",
        "\n",
        "Também podemos comparar palavras ou frases verificando:\n",
        "\n",
        "- se determinadas palavras aparecem no texto\n",
        "\n",
        "- quantas vezes aparecem\n",
        "\n",
        "- quais palavras dois textos têm em comum\n",
        "\n",
        "Isso é muito útil em tarefas como:\n",
        "\n",
        "- classificação\n",
        "\n",
        "- busca textual\n",
        "\n",
        "- análise de conteúdo"
      ],
      "metadata": {
        "id": "lQB3fwc3dLRF"
      },
      "id": "lQB3fwc3dLRF"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**4. Vetorização de texto**\n",
        "\n",
        "Como modelos de machine learning trabalham com números, uma técnica comum é transformar palavras em vetores numéricos.\n",
        "\n",
        "Uma forma simples de fazer isso é usando o **CountVectorizer**, que converte o texto em uma matriz de contagem de palavras.\n",
        "\n",
        "Exemplo:\n",
        "\n",
        "![image.png](data:image/png;base64,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)\n",
        "\n",
        "Assim, o texto passa a ser representado numericamente."
      ],
      "metadata": {
        "id": "lGVEC0xmdV48"
      },
      "id": "lGVEC0xmdV48"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo em Python — Passo a passo**\n",
        "\n",
        "A seguir está um exemplo simples para mostrar como o NLP pode ser feito em Python.\n",
        "\n",
        "##**Objetivo do exemplo**\n",
        "\n",
        "Vamos:\n",
        "\n",
        "- criar pequenos textos\n",
        "\n",
        "- transformar os textos em minúsculas\n",
        "\n",
        "- remover pontuação\n",
        "\n",
        "- separar palavras\n",
        "\n",
        "- contar frequência\n",
        "\n",
        "- comparar textos com ```CountVectorizer```"
      ],
      "metadata": {
        "id": "rDM5HUvQdk9g"
      },
      "id": "rDM5HUvQdk9g"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 1 — Criar textos**"
      ],
      "metadata": {
        "id": "0jDjQU2Nd2lV"
      },
      "id": "0jDjQU2Nd2lV"
    },
    {
      "cell_type": "code",
      "source": [
        "textos = [\n",
        "    \"A inteligência artificial está presente na indústria.\",\n",
        "    \"A indústria utiliza dados e inteligência artificial.\",\n",
        "    \"Modelos de linguagem ajudam na análise de textos.\"\n",
        "]\n",
        "\n",
        "for texto in textos:\n",
        "    print(texto)"
      ],
      "metadata": {
        "id": "kP7Je7Ynd5gi"
      },
      "id": "kP7Je7Ynd5gi",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Aqui criamos uma lista com três frases.\n",
        "Cada frase será tratada como um pequeno documento para análise."
      ],
      "metadata": {
        "id": "bIv-Uk6pd88O"
      },
      "id": "bIv-Uk6pd88O"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 2 — Colocar tudo em minúsculas**"
      ],
      "metadata": {
        "id": "WMWWnAVjeB-B"
      },
      "id": "WMWWnAVjeB-B"
    },
    {
      "cell_type": "code",
      "source": [
        "textos_minusculos = [texto.lower() for texto in textos]\n",
        "\n",
        "for texto in textos_minusculos:\n",
        "    print(texto)"
      ],
      "metadata": {
        "id": "RTIBA5U1eGVv"
      },
      "id": "RTIBA5U1eGVv",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Transformar tudo em minúsculas ajuda a evitar que palavras iguais sejam tratadas como diferentes.\n",
        "\n",
        "Exemplo:\n",
        "\n",
        "```Indústria```\n",
        "\n",
        "```indústria```\n",
        "\n",
        "Sem padronização, o computador pode interpretar como palavras diferentes."
      ],
      "metadata": {
        "id": "YNzIM-mKeJNz"
      },
      "id": "YNzIM-mKeJNz"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 3 — Remover pontuação**"
      ],
      "metadata": {
        "id": "sAWjntH8eUjF"
      },
      "id": "sAWjntH8eUjF"
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "textos_limpos = [re.sub(r\"[^\\w\\s]\", \"\", texto) for texto in textos_minusculos]\n",
        "\n",
        "for texto in textos_limpos:\n",
        "    print(texto)"
      ],
      "metadata": {
        "id": "Qa_ryIOUeesB"
      },
      "id": "Qa_ryIOUeesB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Aqui usamos a biblioteca re para remover sinais de pontuação, como:\n",
        "\n",
        "- ponto\n",
        "\n",
        "- vírgula\n",
        "\n",
        "- exclamação\n",
        "\n",
        "Isso deixa o texto mais limpo para análise."
      ],
      "metadata": {
        "id": "mvtvWV-aeiEj"
      },
      "id": "mvtvWV-aeiEj"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Etapa 4 — Tokenização simples**"
      ],
      "metadata": {
        "id": "tSEkpl8wepXR"
      },
      "id": "tSEkpl8wepXR"
    },
    {
      "cell_type": "code",
      "source": [
        "tokens = [texto.split() for texto in textos_limpos]\n",
        "\n",
        "for lista_tokens in tokens:\n",
        "    print(lista_tokens)"
      ],
      "metadata": {
        "id": "FV-aXPj2euO_"
      },
      "id": "FV-aXPj2euO_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "A função ```split()``` separa o texto em palavras.\n",
        "\n",
        "Assim, cada frase é transformada em uma lista de tokens."
      ],
      "metadata": {
        "id": "0zyATtnVeyQv"
      },
      "id": "0zyATtnVeyQv"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 5 — Contar frequência de palavras**"
      ],
      "metadata": {
        "id": "JDbtmG1Ce45s"
      },
      "id": "JDbtmG1Ce45s"
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "\n",
        "for i, texto in enumerate(tokens):\n",
        "    contagem = Counter(texto)\n",
        "    print(f\"Texto {i+1}:\")\n",
        "    print(contagem)\n",
        "    print()"
      ],
      "metadata": {
        "id": "Lpj83Xzhe8Yz"
      },
      "id": "Lpj83Xzhe8Yz",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "```Counter``` conta quantas vezes cada palavra aparece.\n",
        "\n",
        "Isso permite identificar as palavras mais frequentes em cada texto."
      ],
      "metadata": {
        "id": "kLddrn_LfCA9"
      },
      "id": "kLddrn_LfCA9"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 6 — Comparar textos com CountVectorizer**"
      ],
      "metadata": {
        "id": "ldLpLCEqfN7I"
      },
      "id": "ldLpLCEqfN7I"
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "\n",
        "vectorizer = CountVectorizer()\n",
        "\n",
        "X = vectorizer.fit_transform(textos_limpos)"
      ],
      "metadata": {
        "id": "YwloRBaFfQlw"
      },
      "id": "YwloRBaFfQlw",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "```CountVectorizer``` transforma os textos em números.\n",
        "\n",
        "Ele cria uma representação baseada na quantidade de vezes que cada palavra aparece."
      ],
      "metadata": {
        "id": "1oqqXsp8fVkn"
      },
      "id": "1oqqXsp8fVkn"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 7 — Visualizar a matriz gerada**"
      ],
      "metadata": {
        "id": "iIoz8aptfclm"
      },
      "id": "iIoz8aptfclm"
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df_bow = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())\n",
        "\n",
        "df_bow"
      ],
      "metadata": {
        "id": "TyHJe_Djfn4E"
      },
      "id": "TyHJe_Djfn4E",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Aqui transformamos a saída do CountVectorizer em um DataFrame para facilitar a visualização.\n",
        "\n",
        "Cada:\n",
        "\n",
        "- **linha** representa um texto\n",
        "\n",
        "- **coluna** representa uma palavra\n",
        "\n",
        "- **valor** representa a frequência da palavra naquele texto"
      ],
      "metadata": {
        "id": "7y9MznR7fo55"
      },
      "id": "7y9MznR7fo55"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 8 — Ver palavras em comum entre textos**"
      ],
      "metadata": {
        "id": "Qg6LgY9pf4xb"
      },
      "id": "Qg6LgY9pf4xb"
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Palavras identificadas pelo vetor:\")\n",
        "print(vectorizer.get_feature_names_out())"
      ],
      "metadata": {
        "id": "JrYWE_mXf7Zu"
      },
      "id": "JrYWE_mXf7Zu",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Essa etapa mostra o vocabulário aprendido pelo modelo.\n",
        "\n",
        "Com isso, os alunos conseguem observar quais palavras foram encontradas e comparadas."
      ],
      "metadata": {
        "id": "DshluYm2f_X-"
      },
      "id": "DshluYm2f_X-"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Exemplo de interpretação**\n",
        "\n",
        "Se a palavra inteligência aparece em dois textos, o modelo percebe que existe uma semelhança entre eles.\n",
        "\n",
        "Se um texto possui muitas palavras em comum com outro, eles tendem a ser mais parecidos.\n",
        "\n",
        "Esse tipo de comparação é a base para tarefas como:\n",
        "\n",
        "- classificação de texto\n",
        "\n",
        "- agrupamento de documentos\n",
        "\n",
        "- recomendação\n",
        "\n",
        "- busca semântica inicial"
      ],
      "metadata": {
        "id": "HRpRdl3_gLdR"
      },
      "id": "HRpRdl3_gLdR"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Conclusão**\n",
        "\n",
        "O Processamento de Linguagem Natural permite que os computadores trabalhem com textos de forma estruturada.\n",
        "\n",
        "Para isso, o texto precisa passar por etapas de preparação, como:\n",
        "\n",
        "- padronização\n",
        "\n",
        "- limpeza\n",
        "\n",
        "- tokenização\n",
        "\n",
        "- vetorização\n",
        "\n",
        "Neste exemplo, vimos como:\n",
        "\n",
        "- dividir textos em palavras\n",
        "\n",
        "- contar frequências\n",
        "\n",
        "- transformar textos em números\n",
        "\n",
        "- comparar palavras entre diferentes frases\n",
        "\n",
        "Esses procedimentos são fundamentais para aplicações mais avançadas de NLP."
      ],
      "metadata": {
        "id": "qoBG67B1gZtd"
      },
      "id": "qoBG67B1gZtd"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exercício**\n",
        "\n",
        "Utilize três novas frases de sua escolha e faça:\n",
        "\n",
        "- conversão para minúsculas\n",
        "\n",
        "- remoção de pontuação\n",
        "\n",
        "- tokenização\n",
        "\n",
        "- contagem de palavras\n",
        "\n",
        "- vetorização com ```CountVectorizer```\n",
        "\n",
        "Depois responda:\n",
        "\n",
        "1. quais palavras aparecem em mais de um texto?\n",
        "\n",
        "2. qual texto parece mais parecido com outro?\n",
        "\n",
        "3. quais palavras são mais frequentes?"
      ],
      "metadata": {
        "id": "sBovqkFEgvix"
      },
      "id": "sBovqkFEgvix"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo simples — Análise de sentimento de avaliações de restaurante**\n",
        "##**Contexto**\n",
        "\n",
        "Um restaurante quer analisar automaticamente os comentários deixados pelos clientes para identificar:\n",
        "\n",
        "- elogios\n",
        "\n",
        "- reclamações\n",
        "\n",
        "- comentários neutros\n",
        "\n",
        "Neste exemplo, vamos criar uma pequena base de frases e classificar o sentimento com base em palavras que indicam satisfação ou insatisfação."
      ],
      "metadata": {
        "id": "8-BeLm3zhT0v"
      },
      "id": "8-BeLm3zhT0v"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 1 — Criar os comentários**"
      ],
      "metadata": {
        "id": "kMVArv6phhL1"
      },
      "id": "kMVArv6phhL1"
    },
    {
      "cell_type": "code",
      "source": [
        "comentarios = [\n",
        "    \"A comida estava deliciosa e o atendimento foi excelente.\",\n",
        "    \"Demorou muito para entregar e a comida chegou fria.\",\n",
        "    \"O ambiente é agradável, mas o pedido veio errado.\",\n",
        "    \"Gostei bastante da sobremesa e do atendimento.\",\n",
        "    \"A comida estava sem sabor e o serviço foi ruim.\",\n",
        "    \"O restaurante é bonito e o preço está dentro do esperado.\"\n",
        "]\n",
        "\n",
        "for comentario in comentarios:\n",
        "    print(comentario)"
      ],
      "metadata": {
        "id": "f8Zqz_xBhTde"
      },
      "id": "f8Zqz_xBhTde",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Aqui criamos uma lista com comentários de clientes.\n",
        "\n",
        "Alguns comentários são:\n",
        "\n",
        "- positivos\n",
        "\n",
        "- negativos\n",
        "\n",
        "- mistos ou neutros"
      ],
      "metadata": {
        "id": "aYqy_0_0hqJL"
      },
      "id": "aYqy_0_0hqJL"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 2 — Colocar tudo em minúsculas e remover pontuação**"
      ],
      "metadata": {
        "id": "wTstnR7oiGhe"
      },
      "id": "wTstnR7oiGhe"
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "comentarios_minusculos = [comentario.lower() for comentario in comentarios]\n",
        "\n",
        "comentarios_limpos = [re.sub(r\"[^\\w\\s]\", \"\", comentario) for comentario in comentarios_minusculos]\n",
        "\n",
        "for comentario in comentarios_limpos:\n",
        "    print(comentario)"
      ],
      "metadata": {
        "id": "v5I1_IV0iLgz"
      },
      "id": "v5I1_IV0iLgz",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Nesta etapa fazemos duas coisas importantes:\n",
        "\n",
        "- transformamos tudo em minúsculas\n",
        "\n",
        "- removemos a pontuação\n",
        "\n",
        "Isso facilita a comparação de palavras.\n",
        "\n",
        "Exemplo:\n",
        "\n",
        "- ```Ruim```\n",
        "\n",
        "- ```ruim```\n",
        "\n",
        "- ```ruim!```\n",
        "\n",
        "Depois da limpeza, tudo fica mais padronizado."
      ],
      "metadata": {
        "id": "7ZnI0KGsiU5I"
      },
      "id": "7ZnI0KGsiU5I"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 3 — Criar listas de palavras positivas e negativas**"
      ],
      "metadata": {
        "id": "apZWv2nWilXJ"
      },
      "id": "apZWv2nWilXJ"
    },
    {
      "cell_type": "code",
      "source": [
        "palavras_positivas = [\n",
        "    \"deliciosa\", \"excelente\", \"agradável\", \"gostei\", \"bonito\", \"bom\"\n",
        "]\n",
        "\n",
        "palavras_negativas = [\n",
        "    \"demorou\", \"fria\", \"errado\", \"ruim\", \"sem\", \"sabor\"\n",
        "]"
      ],
      "metadata": {
        "id": "vFkuQ7POiqJD"
      },
      "id": "vFkuQ7POiqJD",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Essas listas funcionam como um vocabulário simples para análise de sentimento.\n",
        "\n",
        "Se o comentário tiver mais palavras negativas, ele tende a ser classificado como **negativo**.\n",
        "Se tiver mais palavras positivas, tende a ser **positivo**."
      ],
      "metadata": {
        "id": "PwqJYdf4ivgt"
      },
      "id": "PwqJYdf4ivgt"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 4 — Criar uma função para classificar o sentimento**"
      ],
      "metadata": {
        "id": "K9OZsZIMi4e3"
      },
      "id": "K9OZsZIMi4e3"
    },
    {
      "cell_type": "code",
      "source": [
        "def classificar_sentimento(texto):\n",
        "    palavras = texto.split()\n",
        "\n",
        "    positivas = 0\n",
        "    negativas = 0\n",
        "\n",
        "    for palavra in palavras:\n",
        "        if palavra in palavras_positivas:\n",
        "            positivas += 1\n",
        "        if palavra in palavras_negativas:\n",
        "            negativas += 1\n",
        "\n",
        "    if negativas > positivas:\n",
        "        return \"negativo\"\n",
        "    elif positivas > negativas:\n",
        "        return \"positivo\"\n",
        "    else:\n",
        "        return \"neutro\""
      ],
      "metadata": {
        "id": "kpuL9DJ6lkSa"
      },
      "id": "kpuL9DJ6lkSa",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação passo a passo**\n",
        "\n",
        "- ```texto.split()``` separa o comentário em palavras\n",
        "\n",
        "- o programa conta quantas palavras positivas aparecem\n",
        "\n",
        "- depois conta quantas palavras negativas aparecem\n",
        "\n",
        "- ao final, compara as quantidades\n",
        "\n",
        "Regras:\n",
        "\n",
        "- mais negativas → **negativo**\n",
        "\n",
        "- mais positivas → **positivo**\n",
        "\n",
        "- empate → **neutro**"
      ],
      "metadata": {
        "id": "V9sPXBXMjCqB"
      },
      "id": "V9sPXBXMjCqB"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 5 — Aplicar a função nos comentários**"
      ],
      "metadata": {
        "id": "Zmo0ff2zjTnx"
      },
      "id": "Zmo0ff2zjTnx"
    },
    {
      "cell_type": "code",
      "source": [
        "for comentario in comentarios_limpos:\n",
        "    sentimento = classificar_sentimento(comentario)\n",
        "    print(f\"Comentário: {comentario}\")\n",
        "    print(f\"Sentimento: {sentimento}\")\n",
        "    print(\"-\" * 50)"
      ],
      "metadata": {
        "id": "qE1ur9BEjaP2"
      },
      "id": "qE1ur9BEjaP2",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 6 — Organizar em DataFrame**"
      ],
      "metadata": {
        "id": "iSxJKYwLjiLT"
      },
      "id": "iSxJKYwLjiLT"
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.DataFrame({\n",
        "    \"comentario_original\": comentarios,\n",
        "    \"comentario_limpo\": comentarios_limpos\n",
        "})\n",
        "\n",
        "df[\"sentimento\"] = df[\"comentario_limpo\"].apply(classificar_sentimento)\n",
        "\n",
        "df"
      ],
      "metadata": {
        "id": "BNGK3fQrjlV_"
      },
      "id": "BNGK3fQrjlV_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Aqui organizamos os resultados em uma tabela, o que facilita:\n",
        "\n",
        "- visualização\n",
        "\n",
        "- análise\n",
        "\n",
        "- exportação para CSV"
      ],
      "metadata": {
        "id": "PoEyhp5GjiJd"
      },
      "id": "PoEyhp5GjiJd"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Etapa 7 — Filtrar apenas reclamações**\n",
        "\n",
        "Se o objetivo for identificar reclamações do restaurante, podemos filtrar apenas os comentários negativos."
      ],
      "metadata": {
        "id": "V4dTsVdhj04P"
      },
      "id": "V4dTsVdhj04P"
    },
    {
      "cell_type": "code",
      "source": [
        "reclamacoes = df[df[\"sentimento\"] == \"negativo\"]\n",
        "\n",
        "reclamacoes"
      ],
      "metadata": {
        "id": "50PDh-Wgj4rc"
      },
      "id": "50PDh-Wgj4rc",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Explicação**\n",
        "\n",
        "Agora o restaurante consegue localizar rapidamente os comentários com maior chance de representar reclamações."
      ],
      "metadata": {
        "id": "u1TZApCbj6_2"
      },
      "id": "u1TZApCbj6_2"
    },
    {
      "cell_type": "markdown",
      "source": [
        "Com essa atividade, os alunos entendem:\n",
        "\n",
        "- como limpar textos\n",
        "\n",
        "- como separar palavras\n",
        "\n",
        "- como comparar palavras com listas\n",
        "\n",
        "- como criar uma classificação simples\n",
        "\n",
        "- como filtrar reclamações em um conjunto de comentários"
      ],
      "metadata": {
        "id": "kWRLxpAGkBYQ"
      },
      "id": "kWRLxpAGkBYQ"
    },
    {
      "cell_type": "markdown",
      "source": [
        "###**Limitação importante do exemplo**\n",
        "\n",
        "Esse método é **simples e didático**, mas possui limitações.\n",
        "\n",
        "Por exemplo, ele pode errar em frases como:\n",
        "\n",
        "```\n",
        "\"O atendimento não foi ruim\"\n",
        "```\n",
        "\n",
        "A palavra **ruim** aparece, mas o sentido da frase não é exatamente negativo.\n",
        "\n",
        "Por isso, em projetos mais avançados usamos:\n",
        "\n",
        "- modelos treinados\n",
        "\n",
        "- embeddings\n",
        "\n",
        "- bibliotecas específicas de NLP\n",
        "\n",
        "- modelos de linguagem\n",
        "\n",
        "Mas, para começar, esse exemplo é excelente."
      ],
      "metadata": {
        "id": "LO1d0DtskHi4"
      },
      "id": "LO1d0DtskHi4"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Exercício para os alunos**\n",
        "\n",
        "Faça:\n",
        "\n",
        "- adicionar 5 novos comentários\n",
        "\n",
        "- incluir novas palavras positivas e negativas\n",
        "\n",
        "- verificar como a classificação muda\n",
        "\n",
        "- separar apenas os comentários negativos"
      ],
      "metadata": {
        "id": "LDzF5rAgkaV5"
      },
      "id": "LDzF5rAgkaV5"
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