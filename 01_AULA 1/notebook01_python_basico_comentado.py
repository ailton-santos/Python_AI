{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Lag-Y9KXmk25"
      },
      "source": [
        "# Notebook 01 — Revisão de Python para Inteligência Artificial\n",
        "\n",
        "Este notebook revisa conceitos básicos da linguagem Python necessários para acompanhar o restante do curso.Execute cada célula e leia os comentários cuidadosamente."
      ],
      "id": "Lag-Y9KXmk25"
    },
    {
      "cell_type": "code",
      "source": [
        "# print() é uma função utilizada para exibir informações na tela\n",
        "\n",
        "# Ela é muito útil para verificar resultados durante a programação\n",
        "\n",
        "print(\"Ambiente pronto para iniciar os estudos de IA!\")"
      ],
      "metadata": {
        "id": "KBxTaTYroWpj"
      },
      "id": "KBxTaTYroWpj",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IkejI23Hmk2-"
      },
      "source": [
        "#**Variáveis**"
      ],
      "id": "IkejI23Hmk2-"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dRP6d7cTmk2-"
      },
      "outputs": [],
      "source": [
        "# Criamos uma variável chamada 'nome'\n",
        "\n",
        "# Variáveis armazenam valores na memória\n",
        "\n",
        "nome = \"Inteligência Artificial\""
      ],
      "id": "dRP6d7cTmk2-"
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos outra variável chamada 'ano'\n",
        "\n",
        "ano = 2026"
      ],
      "metadata": {
        "id": "dGFVm_AjocV3"
      },
      "id": "dGFVm_AjocV3",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# A função print() exibe o conteúdo das variáveis\n",
        "\n",
        "print(nome)"
      ],
      "metadata": {
        "id": "1HzKZBKpof1H"
      },
      "id": "1HzKZBKpof1H",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(ano)"
      ],
      "metadata": {
        "id": "TA_AtqiUoiSP"
      },
      "id": "TA_AtqiUoiSP",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Identificar uma variável com a função type():\n",
        "print(type(nome))"
      ],
      "metadata": {
        "id": "aE0RJLIup2pv"
      },
      "id": "aE0RJLIup2pv",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(ano))"
      ],
      "metadata": {
        "id": "qedxbZ56qDCN"
      },
      "id": "qedxbZ56qDCN",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zuO7lxc-mk2_"
      },
      "source": [
        "#**Estruturas condicionais**"
      ],
      "id": "zuO7lxc-mk2_"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yhv71vcKmk2_"
      },
      "outputs": [],
      "source": [
        "# Criamos uma variável com valor numérico\n",
        "\n",
        "nota = 8"
      ],
      "id": "yhv71vcKmk2_"
    },
    {
      "cell_type": "code",
      "source": [
        "# Estrutura condicional if\n",
        "\n",
        "# Permite executar diferentes blocos de código dependendo da condição\n",
        "\n",
        "if nota >= 7:    # Este bloco executa se a condição for verdadeira\n",
        "  print(\"Aprovado\")\n",
        "else:    # Este bloco executa se a condição for falsa\n",
        "  print(\"Revisar conteúdo\")"
      ],
      "metadata": {
        "id": "epvdDSxuooj0"
      },
      "id": "epvdDSxuooj0",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 1: Verificação de idade**"
      ],
      "metadata": {
        "id": "sCaA-9foqglA"
      },
      "id": "sCaA-9foqglA"
    },
    {
      "cell_type": "code",
      "source": [
        "# Usar input() para a entrada de valores pelo teclado.\n",
        "\n",
        "idade = input(\"Digite sua idade: \")"
      ],
      "metadata": {
        "id": "N_QjlM1jqYxA"
      },
      "id": "N_QjlM1jqYxA",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if idade < 18:\n",
        "  print(\"Você é menor de idade.\")\n",
        "elif idade == 18:\n",
        "  print(\"Você acabou de atingir a maioridade!\")\n",
        "else:\n",
        "  print(\"Você é maior de idade.\")"
      ],
      "metadata": {
        "id": "LgOaHy6Tw_Jy"
      },
      "id": "LgOaHy6Tw_Jy",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(idade))"
      ],
      "metadata": {
        "id": "fHsGf7R0w__i"
      },
      "id": "fHsGf7R0w__i",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# int() converte os valores do tipo str de input() em número inteiro\n",
        "\n",
        "idade = int(input(\"Digite sua idade: \"))"
      ],
      "metadata": {
        "id": "Id2opt1sw2gl"
      },
      "id": "Id2opt1sw2gl",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if idade < 18:\n",
        "  print(\"Você é menor de idade.\")\n",
        "elif idade == 18:\n",
        "  print(\"Você acabou de atingir a maioridade!\")\n",
        "else:\n",
        "  print(\"Você é maior de idade.\")"
      ],
      "metadata": {
        "id": "snj_ff7nqkjj"
      },
      "id": "snj_ff7nqkjj",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 2: Classificação de notas**"
      ],
      "metadata": {
        "id": "xno5I-ifrdsz"
      },
      "id": "xno5I-ifrdsz"
    },
    {
      "cell_type": "code",
      "source": [
        "# float() converte a\n",
        "\n",
        "nota = float(input(\"Digite a nota do aluno: \"))"
      ],
      "metadata": {
        "id": "pn5Xbw7ergay"
      },
      "id": "pn5Xbw7ergay",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(type(nota))"
      ],
      "metadata": {
        "id": "QaQGRIjixLjY"
      },
      "id": "QaQGRIjixLjY",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if nota >= 9.0:\n",
        "    print(\"Excelente!\")\n",
        "elif nota >= 7.0:\n",
        "    print(\"Bom desempenho.\")\n",
        "elif nota >= 5.0:\n",
        "    print(\"Você passou, mas pode melhorar.\")\n",
        "else:\n",
        "    print(\"Reprovado.\")"
      ],
      "metadata": {
        "id": "nQ0w-hAGrjpz"
      },
      "id": "nQ0w-hAGrjpz",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 3: Checando números**"
      ],
      "metadata": {
        "id": "dnb-wAxXrr5d"
      },
      "id": "dnb-wAxXrr5d"
    },
    {
      "cell_type": "code",
      "source": [
        "numero = int(input(\"Digite a nota do aluno: \"))"
      ],
      "metadata": {
        "id": "EWAlAfd8rxE8"
      },
      "id": "EWAlAfd8rxE8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if numero > 0:\n",
        "    print(\"O número é positivo.\")\n",
        "elif numero < 0:\n",
        "    print(\"O número é negativo.\")\n",
        "else:\n",
        "    print(\"O número é zero.\")"
      ],
      "metadata": {
        "id": "2gDmBycLr19t"
      },
      "id": "2gDmBycLr19t",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V6r07Defmk2_"
      },
      "source": [
        "#**Estrutura de repetição**"
      ],
      "id": "V6r07Defmk2_"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9HSednx0mk3A"
      },
      "outputs": [],
      "source": [
        "# A função range(5) cria uma sequência de números de 0 até 4\n",
        "# O laço for executa o código repetidamente\n",
        "\n",
        "for i in range(5):    # A variável i assume valores da sequência\n",
        "  print(\"Execução número:\", i)"
      ],
      "id": "9HSednx0mk3A"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 1: Percorrendo uma lista**"
      ],
      "metadata": {
        "id": "3WJTpKV9sVA1"
      },
      "id": "3WJTpKV9sVA1"
    },
    {
      "cell_type": "markdown",
      "source": [
        "🔹 O que são listas?\n",
        "- Coleção ordenada: os elementos mantêm a ordem em que foram inseridos.\n",
        "- Mutáveis: você pode alterar, adicionar ou remover itens após a criação.\n",
        "- Heterogêneas: podem conter diferentes tipos de dados (números, strings, booleanos, até outras listas).\n",
        "- Dinâmicas: o tamanho pode crescer ou diminuir conforme necessário.\n"
      ],
      "metadata": {
        "id": "jiTWO9o2ta7n"
      },
      "id": "jiTWO9o2ta7n"
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista vazia\n",
        "lista_vazia = []"
      ],
      "metadata": {
        "id": "6EblKqibtdC3"
      },
      "id": "6EblKqibtdC3",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(lista_vazia)"
      ],
      "metadata": {
        "id": "FFteQpmExj45"
      },
      "id": "FFteQpmExj45",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista com elementos\n",
        "numeros = [1, 2, 3, 4, 5]\n",
        "frutas = [\"maçã\", \"banana\", \"laranja\"]"
      ],
      "metadata": {
        "id": "lVnK-hyUt0hq"
      },
      "id": "lVnK-hyUt0hq",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(numeros)"
      ],
      "metadata": {
        "id": "uRdUypWBxe0F"
      },
      "id": "uRdUypWBxe0F",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(frutas)"
      ],
      "metadata": {
        "id": "3JtfwG84xhO3"
      },
      "id": "3JtfwG84xhO3",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista mista\n",
        "misto = [1, \"texto\", 3.14, True, [10, 20]]"
      ],
      "metadata": {
        "id": "g32Pw737t3qD"
      },
      "id": "g32Pw737t3qD",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(misto)"
      ],
      "metadata": {
        "id": "URbERkiwxota"
      },
      "id": "URbERkiwxota",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Métodos úteis**\n",
        "- ```append()``` → adiciona no final\n",
        "- ```insert(pos, valor)``` → insere em posição específica\n",
        "- ```remove(valor)``` → remove o primeiro valor encontrado\n",
        "- ```pop()``` → remove e retorna o último elemento\n",
        "- ```sort()``` → ordena a lista\n",
        "- ```len(lista)``` → retorna o tamanho da lista\n"
      ],
      "metadata": {
        "id": "C3dpdtsYtmLx"
      },
      "id": "C3dpdtsYtmLx"
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = [10, 5, 8, 3]"
      ],
      "metadata": {
        "id": "aZVhd81Tt7Z2"
      },
      "id": "aZVhd81Tt7Z2",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numeros.sort()\n",
        "print(numeros)  # [3, 5, 8, 10]"
      ],
      "metadata": {
        "id": "htK9YE7-tqUy"
      },
      "id": "htK9YE7-tqUy",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numeros.append(12)\n",
        "print(numeros)  # [3, 5, 8, 10, 12]"
      ],
      "metadata": {
        "id": "c3n38ncktxdU"
      },
      "id": "c3n38ncktxdU",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "frutas = [\"maçã\", \"banana\", \"laranja\"]"
      ],
      "metadata": {
        "id": "hFf-WxBYsXuP"
      },
      "id": "hFf-WxBYsXuP",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for fruta in frutas:\n",
        "    print(\"Eu gosto de\", fruta)"
      ],
      "metadata": {
        "id": "vzfeO7xXsfrF"
      },
      "id": "vzfeO7xXsfrF",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 2: Usando** ```range()```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "Fqqe7-zCsk74"
      },
      "id": "Fqqe7-zCsk74"
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5):\n",
        "    print(\"Número:\", i)"
      ],
      "metadata": {
        "id": "WGT2SCnxsrfm"
      },
      "id": "WGT2SCnxsrfm",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 3: Iterando sobre um dicionário**"
      ],
      "metadata": {
        "id": "SgJBktRws0X2"
      },
      "id": "SgJBktRws0X2"
    },
    {
      "cell_type": "code",
      "source": [
        "pessoa = {\"nome\": \"Diego\", \"idade\": 30, \"cidade\": \"Guarulhos\"}\n",
        "\n",
        "for chave, valor in pessoa.items():\n",
        "    print(chave, \":\", valor) # Aqui o for percorre as chaves e valores de um dicionário"
      ],
      "metadata": {
        "id": "Hu4dHbSgs1Y_"
      },
      "id": "Hu4dHbSgs1Y_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-Q9rJG-umk3A"
      },
      "source": [
        "##**Exercício**\n",
        "\n",
        "Crie um programa que:\n",
        "\n",
        "1. Peça o nome do usuário\n",
        "\n",
        "2. Exiba uma mensagem de boas-vindas três vezes"
      ],
      "id": "-Q9rJG-umk3A"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WU4zEjPLmk3A"
      },
      "outputs": [],
      "source": [
        "# input() permite receber dados digitados pelo usuário\n",
        "\n",
        "nome = input(\"Digite seu nome: \")"
      ],
      "id": "WU4zEjPLmk3A"
    },
    {
      "cell_type": "code",
      "source": [
        "# O laço for será executado três vezes\n",
        "\n",
        "for i in range(3):\n",
        "  print(\"Bem-vindo ao curso de IA,\", nome)"
      ],
      "metadata": {
        "id": "hghl3gfWpB6G"
      },
      "id": "hghl3gfWpB6G",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        " Vamos comparar com o for criando três exemplos de estruturas de repetição com while:"
      ],
      "metadata": {
        "id": "bq_q7Wg_uQ_u"
      },
      "id": "bq_q7Wg_uQ_u"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 1: Contagem simples**"
      ],
      "metadata": {
        "id": "DPIf9HsmuUq4"
      },
      "id": "DPIf9HsmuUq4"
    },
    {
      "cell_type": "code",
      "source": [
        "contador = 0"
      ],
      "metadata": {
        "id": "1zMnGSo8pYV6"
      },
      "id": "1zMnGSo8pYV6",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while contador < 5:\n",
        "    print(\"Contador:\", contador)\n",
        "    contador += 1 # Aqui o loop continua enquanto a condição (contador < 5) for verdadeira"
      ],
      "metadata": {
        "id": "tS-HNyWsuZP-"
      },
      "id": "tS-HNyWsuZP-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 2: Validação de entrada**"
      ],
      "metadata": {
        "id": "faOTnhT-uiTf"
      },
      "id": "faOTnhT-uiTf"
    },
    {
      "cell_type": "code",
      "source": [
        "senha = \"\""
      ],
      "metadata": {
        "id": "oTPpkjKruj1J"
      },
      "id": "oTPpkjKruj1J",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while senha != \"python123\":\n",
        "    senha = input(\"Digite a senha: \")\n",
        "\n",
        "print(\"Acesso permitido!\") # O programa só termina quando o usuário digita a senha correta"
      ],
      "metadata": {
        "id": "_p1cXM0Tunxd"
      },
      "id": "_p1cXM0Tunxd",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**🔹 Exemplo 3: Loop infinito com condição de saída**"
      ],
      "metadata": {
        "id": "s5NZFGg4uvau"
      },
      "id": "s5NZFGg4uvau"
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "    resposta = input(\"Digite 'sair' para encerrar: \")\n",
        "    if resposta == \"sair\":\n",
        "        break\n",
        "    print(\"Você digitou:\", resposta) # Esse loop é infinito, mas usamos break para sair quando o usuário digita \"sair\""
      ],
      "metadata": {
        "id": "gy3exNzeuwTB"
      },
      "id": "gy3exNzeuwTB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**✅ Comparação rápida com for:**\n",
        "- O for é usado quando sabemos quantas vezes queremos repetir (percorrer lista, range, etc.).\n",
        "- O while é usado quando queremos repetir até que uma condição seja satisfeita (não sabemos o número exato de repetições).\n"
      ],
      "metadata": {
        "id": "iy7OTGA7vFyM"
      },
      "id": "iy7OTGA7vFyM"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**📝 Exercício: Jogo de Adivinhação**\n",
        "Crie um programa em Python que:\n",
        "- Sorteie um número secreto entre 1 e 10.\n",
        "- Peça para o usuário tentar adivinhar o número.\n",
        "- Use um loop while para permitir várias tentativas.\n",
        "- Utilize condicionais (if, elif, else) para dar dicas:\n",
        "- Se o número digitado for menor que o secreto → diga \"O número é maior\".\n",
        "- Se for maior → diga \"O número é menor\".\n",
        "- Se acertar → diga \"Parabéns, você acertou!\" e encerre o jogo.\n"
      ],
      "metadata": {
        "id": "pGNrrsAqvWjS"
      },
      "id": "pGNrrsAqvWjS"
    },
    {
      "cell_type": "code",
      "source": [
        "# Resolução\n",
        "\n",
        "import random\n",
        "\n",
        "# Sorteia um número entre 1 e 10\n",
        "numero_secreto = random.randint(1, 10)\n",
        "\n",
        "tentativa = None\n",
        "\n",
        "while tentativa != numero_secreto:\n",
        "    tentativa = int(input(\"Digite um número entre 1 e 10: \"))\n",
        "\n",
        "    if tentativa < numero_secreto:\n",
        "        print(\"O número é maior.\")\n",
        "    elif tentativa > numero_secreto:\n",
        "        print(\"O número é menor.\")\n",
        "    else:\n",
        "        print(\"Parabéns, você acertou!\")"
      ],
      "metadata": {
        "id": "SI62yqqlvlLe"
      },
      "id": "SI62yqqlvlLe",
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