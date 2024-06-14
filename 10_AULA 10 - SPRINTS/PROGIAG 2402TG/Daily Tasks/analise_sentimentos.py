# -*- coding: utf-8 -*-
"""Analise-Sentimentos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uo_EXiwTRPAIfJ3aXv4dKqRkZacPPrgr
"""

import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

tweets = []
sentimentos = []

#Tweet Aleatório

palavrasPositivas = ['maravilhoso', 'incrivel', 'adoro', 'recomendo', 'perfeito']
palavrasNegativas = ['ruim', 'horrivel', 'decepcionante', 'nao recomendo', 'pessimo']
palavrasNeutras = ['bom', 'legal', 'ok', 'interessante', 'informativo']

for i in range(100):
  #Tweet Positivo - Input palavra para classificação positiva
  tweetPositivo = random.choice(palavrasPositivas)+' '+random.choice(palavrasPositivas)
  tweets.append(tweetPositivo)
  sentimentos.append(2)

  #Tweet Neutro - Input palavra para classificação netra
  tweetNeutro = random.choice(palavrasNeutras)+' '+random.choice(palavrasNeutras)
  tweets.append(tweetNeutro)
  sentimentos.append(1)

  #Tweet Negativo - Input palavra para classificação negativa
  tweetNegativo = random.choice(palavrasNegativas)+' '+random.choice(palavrasNegativas)
  tweets.append(tweetNegativo)
  sentimentos.append(0)

#DF

dadosTweet = pd.DataFrame({
    'tweet': tweets,
    'sentimento': sentimentos
})

dadosTweet.to_csv('dados_tweets.csv', index=False)

dadosTweet = pd.read_csv('dados_tweets.csv')

dadosTweet.head()

#Separação Tweets e Rótulos

tweets = dadosTweet['tweet']
rotulos = dadosTweet['sentimento']

#Conversão tweets em vetores

vectorizer = TfidfVectorizer()
tweetsVetorizados = vectorizer.fit_transform(tweets)

#Treino X e Y

x_treino,x_teste,y_treino,y_teste = train_test_split(tweetsVetorizados, rotulos, test_size=0.2, random_state=42)

#Equalização (Treino) Naives Bayes

modelo = MultinomialNB()
modelo.fit(x_treino,y_treino)

#Avaliação Desempenho do Modelo (Acurácia)

acuracia = modelo.score(x_teste,y_teste)

print ('Acurácia do modelo é: ', acuracia)

#Classificação dos novos tweets (Predição)

tweetNovo = 'Recomendo o novo produto da marca #maravilhoso'

vetorNovo = vectorizer.transform([tweetNovo])

sentimentoPredito = modelo.predict(vetorNovo)

print ('O sentimento do novo tweet é: ', sentimentoPredito[0])