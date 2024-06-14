# -*- coding: utf-8 -*-
"""Modelo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WnYN4B05BhIVBYpU9vIcYC2ofBTLKz91
"""

import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

tweets=[]
sentimentos =[]

#Tweet Aleatório
palavras_pos=['maravilhoso','incrivel','adoro','recomento','perfeito']
palavras_neg=['ruim','horrivel','decepcionante','nao,recomendo','pessimo']
palavras_neu=['bom','lega','ok','intessante','informativo']

for _ in range(100):
  #Tweet positivo, input palavra para classificação positiva
    tweet_pos = random.choice(palavras_pos) + ' ' + random.choice(palavras_pos)
    tweets.append(tweet_pos)
    sentimentos.append(2)

    tweet_neg = random.choice(palavras_neg) + ' ' + random.choice(palavras_neg)
    tweets.append(tweet_neg)
    sentimentos.append(1)

    tweet_neu = random.choice(palavras_neu) + ' ' + random.choice(palavras_neu)
    tweets.append(tweet_neu)
    sentimentos.append(0)

#DF

dados_tweet=pd.DataFrame({'tweet':tweets,
                         'sentimento':sentimentos})

dados_tweet.to_csv('dados_tweets.csv',index=False)

dados_tweet=pd.read_csv('dados_tweets.csv')

dados_tweet.head()

#Separação Tweets e rótulos

tweets=dados_tweet['tweet']
rotulos=dados_tweet['sentimento']

#cONVERSÃO tweets em vetores
vectorizer=TfidfVectorizer()
tweets_vetorizados=vectorizer.fit_transform(tweets)

# treino x e y
X_treino,X_teste,y_treino,y_teste=train_test_split(tweets_vetorizados,rotulos,test_size=0.2,random_state=42)

# Equalização(treino)Naives Bayes
modelo=MultinomialNB()
modelo.fit(X_treino,y_treino)

#Avaliação desempenho do modelo (Acuracia)
acuracia=modelo.score(X_teste,y_teste)
print('Acuracia do modelo é:',acuracia)

# Classificação dos novos twweets (predição)
tweet_novo ='amei o novo produto da marca! #maravilhoso'
vetor_novo=vectorizer.transform([tweet_novo])
sentimento_predito=modelo.predict(vetor_novo)
print('Osentimento do novo tweet é,: sentimento_predito[0]')