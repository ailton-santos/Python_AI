{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7hIGP3dgyrif"
      },
      "source": [
        "# Notebook 02 — Utilizando APIs de Inteligência Artificial\n",
        "\n",
        "Neste notebook veremos como um programa pode se comunicar com modelos de IA através de APIs."
      ],
      "id": "7hIGP3dgyrif"
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo 1: Utilizando API da Open AI:**"
      ],
      "metadata": {
        "id": "KQaGZj9a0dEY"
      },
      "id": "KQaGZj9a0dEY"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JTuXxUIKyrii"
      },
      "outputs": [],
      "source": [
        "# !pip install instala bibliotecas necessárias no ambiente do Colab\n",
        "\n",
        "!pip install openai"
      ],
      "id": "JTuXxUIKyrii"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J_MEcs7xyrij"
      },
      "outputs": [],
      "source": [
        "# Importamos a classe OpenAI da biblioteca instalada\n",
        "\n",
        "from openai import OpenAI"
      ],
      "id": "J_MEcs7xyrij"
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos um cliente que será responsável por enviar requisições para a API\n",
        "# 1. Configuração da API Key\n",
        "# Dica pedagógica: Ensine seus alunos a usarem variáveis de ambiente\n",
        "# para não exporem a chave publicamente!\n",
        "\n",
        "from google.colab import userdata\n",
        "\n",
        "# Recuperando a chave de forma segura\n",
        "CHAVE_API_OPENAI = userdata.get('OPENAI_API_KEY')\n",
        "\n",
        "client = OpenAI(api_key=CHAVE_API_OPENAI)"
      ],
      "metadata": {
        "id": "M7ylEGmpzVI8"
      },
      "id": "M7ylEGmpzVI8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Criamos uma requisição para o modelo\n",
        "\n",
        "response = client.responses.create(\n",
        "    model=\"gpt-4.1-mini\",\n",
        "    input=\"Explique o que é inteligência artificial.\")    # Nome do modelo utilizado e o texto enviado ao modelo (prompt)"
      ],
      "metadata": {
        "id": "pUr7tirBzc-T"
      },
      "id": "pUr7tirBzc-T",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Exibimos o texto gerado pelo modelo\n",
        "\n",
        "print(response.output[0].content[0].text)"
      ],
      "metadata": {
        "id": "Ggx3xQ5ozgG_"
      },
      "id": "Ggx3xQ5ozgG_",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**Exemplo 2: Utilizando API Google AI**"
      ],
      "metadata": {
        "id": "u86vBRJ_0yTi"
      },
      "id": "u86vBRJ_0yTi"
    },
    {
      "cell_type": "code",
      "source": [
        "# Instalar a biblioteca oficial\n",
        "\n",
        "!pip install -q -U google-generativeai"
      ],
      "metadata": {
        "id": "lgq8TZ2W1-hz"
      },
      "id": "lgq8TZ2W1-hz",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Importar biblitecas googlegenerativeai e os\n",
        "\n",
        "import google.generativeai as genai\n",
        "import os"
      ],
      "metadata": {
        "id": "t4vSGOvZ2EAU"
      },
      "id": "t4vSGOvZ2EAU",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "No Colab, a maneira mais moderna e segura de gerenciar chaves de API não é nem por um arquivo .env tradicional, mas sim através do recurso nativo \"Secrets\" (ícone de chave no menu lateral).\n",
        "\n",
        "Aqui está o passo a passo para você mostrar a eles:"
      ],
      "metadata": {
        "id": "dnhsEmyJG1ay"
      },
      "id": "dnhsEmyJG1ay"
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Guardando a chave no \"Cofre\" do Colab\n",
        "No menu à esquerda do Colab, clique no ícone de chave (Secrets).\n",
        "\n",
        "```\n",
        "Clique em \"Add new secret\".\n",
        "\n",
        "No campo Name, digite: GOOGLE_API_KEY.\n",
        "\n",
        "No campo Value, cole a sua chave gerada no Google AI Studio.\n",
        "```\n",
        "\n",
        "Importante: Ative a chave seletora \"Notebook access\" para que o seu código consiga ler esse valor."
      ],
      "metadata": {
        "id": "gLYrfFQBG3MU"
      },
      "id": "gLYrfFQBG3MU"
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Acessando a chave via código\n",
        "Agora, em vez de escrever a chave diretamente no código, você usa a biblioteca google.colab. Veja como o código fica profissional:"
      ],
      "metadata": {
        "id": "P1_40x1YHC5a"
      },
      "id": "P1_40x1YHC5a"
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Configuração da API Key\n",
        "# Dica pedagógica: Ensine seus alunos a usarem variáveis de ambiente\n",
        "# para não exporem a chave publicamente!\n",
        "\n",
        "from google.colab import userdata\n",
        "\n",
        "CHAVE_API = userdata.get('GOOGLE_API_KEY')\n",
        "genai.configure(api_key=CHAVE_API)"
      ],
      "metadata": {
        "id": "vgDovBtf2NvQ"
      },
      "id": "vgDovBtf2NvQ",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Inicialização do Modelo\n",
        "# O 'gemini-1.5-flash' é ótimo para exemplos rápidos e baixo custo\n",
        "\n",
        "model = genai.GenerativeModel('gemini-2.5-flash-lite')"
      ],
      "metadata": {
        "id": "wGfvgbVk2Qyc"
      },
      "id": "wGfvgbVk2Qyc",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 3. Gerando o conteúdo\n",
        "\n",
        "response = model.generate_content(\"Olá! Estamos testando variáveis de ambiente.\")\n",
        "print(response.text)"
      ],
      "metadata": {
        "id": "aLQSxbqO2u0O"
      },
      "id": "aLQSxbqO2u0O",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n6WCHIisyrik"
      },
      "source": [
        "##**📝 Atividade Prática: Criando seu Primeiro Chatbot Inteligente**\n",
        "Objetivo: Modificar o código base para criar um chatbot que converse com o usuário até que ele decida sair, utilizando o modelo de baixo custo Gemini 2.5 Flash-Lite."
      ],
      "id": "n6WCHIisyrik"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**1. Instruções para os Alunos (Célula de Texto)**\n",
        "\n",
        "\"Nesta atividade, vamos usar um laço de repetição while para manter a conversa ativa. O chatbot deve:\n",
        "\n",
        "- Cumprimentar o usuário.\n",
        "\n",
        "- Ler a pergunta do teclado usando input().\n",
        "\n",
        "- Enviar a pergunta para a API do Gemini.\n",
        "\n",
        "- Exibir a resposta de forma clara.\n",
        "\n",
        "- Encerrar o programa se o usuário digitar 'sair'.\""
      ],
      "metadata": {
        "id": "WZlWLdzvMjBS"
      },
      "id": "WZlWLdzvMjBS"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**2. O Código da Atividade (Célula de Código)**"
      ],
      "metadata": {
        "id": "DK-Yl5nVMoRb"
      },
      "id": "DK-Yl5nVMoRb"
    },
    {
      "cell_type": "code",
      "source": [
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "\n",
        "# Recuperando a chave de forma segura\n",
        "CHAVE_API = userdata.get('GOOGLE_API_KEY')\n",
        "genai.configure(api_key=CHAVE_API)\n",
        "\n",
        "# Inicializando o modelo mais econômico\n",
        "model = genai.GenerativeModel('gemini-2.5-flash-lite')\n",
        "\n",
        "def iniciar_chatbot():\n",
        "    print(\"🤖 Olá! Sou seu assistente de IA econômico. (Digite 'sair' para encerrar)\")\n",
        "    print(\"-\" * 50)\n",
        "\n",
        "    while True:\n",
        "        # Entrada do usuário\n",
        "        pergunta = input(\"Você: \")\n",
        "\n",
        "        # Condição de parada\n",
        "        if pergunta.lower() in ['sair', 'exit', 'quit']:\n",
        "            print(\"Chatbot: Tchau! Até a próxima aula. 👋\")\n",
        "            break\n",
        "\n",
        "        try:\n",
        "            # Enviando para a API\n",
        "            response = model.generate_content(pergunta)\n",
        "\n",
        "            # Exibindo a resposta\n",
        "            print(f\"\\nIA: {response.text}\")\n",
        "            print(\"-\" * 50)\n",
        "\n",
        "        except Exception as e:\n",
        "            print(f\"Ops! Ocorreu um erro: {e}\")\n",
        "\n",
        "# Rodar o chat\n",
        "iniciar_chatbot()"
      ],
      "metadata": {
        "id": "CINGVTYqMiIX"
      },
      "id": "CINGVTYqMiIX",
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