#!/usr/bin/env python
# coding: utf-8

# # Modelo de Previsão Sobre Venda de Carros 
# 
# 
# O processo de criação e avaliação de um modelo de regressão para prever vendas de carros com base em características como ano de fabricação, preço, tipo de veículo, marca e região de venda. O modelo utilizado é um **RandomForestRegressor**, implementado com a biblioteca **scikit-learn**.

# In[ ]:


# Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# In[ ]:


np.random.seed(0) 

# Criar um DataFrame de exemplo com características dos carros e vendas
n_samples = 1000
anos_fabricacao = np.random.randint(2000, 2023, n_samples)  # Anos de fabricação aleatórios
precos = np.random.uniform(10000, 50000, n_samples)  # Preços aleatórios
tipos_veiculo = np.random.choice(['SUV', 'Sedan', 'Hatchback'], n_samples)  # Tipos de veículos aleatórios
marcas = np.random.choice(['Toyota', 'Honda', 'Ford', 'Chevrolet'], n_samples)  # Marcas aleatórias
regioes_venda = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], n_samples)  # Regiões de venda aleatórias
vendas = np.random.randint(50, 500, n_samples)  # Vendas aleatórias


# In[ ]:


# Criar DataFrame com os dados gerados
dados = pd.DataFrame({
    'AnoFabricacao': anos_fabricacao,
    'Preco': precos,
    'TipoVeiculo': tipos_veiculo,
    'Marca': marcas,
    'RegiaoVenda': regioes_venda,
    'Vendas': vendas
})

print(dados.head())
print(dados.info())

# Salvar os dados gerados em um arquivo CSV
dados.to_csv('dados_carros.csv', index=False)


# In[ ]:


# Carregar os dados do arquivo CSV
dados = pd.read_csv('dados_carros.csv')

# Separar características (X) e alvo (y)
X = dados.drop('Vendas', axis=1)
y = dados['Vendas']

# Transformar variáveis categóricas em variáveis dummy
X = pd.get_dummies(X)

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


# Inicializar o modelo RandomForestRegressor
modelo = RandomForestRegressor(random_state=42)

# Treinar o modelo com os dados de treino
modelo.fit(X_train, y_train)


# In[ ]:


# Fazer previsões com os dados de teste
y_pred = modelo.predict(X_test)

# Calcular o Mean Squared Error (MSE) para avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Exemplo de previsão com novos dados (usando a primeira linha dos dados de teste)
exemplo_novo = X_test.iloc[0].values.reshape(1, -1)
previsao = modelo.predict(exemplo_novo)
print(f'Previsão de vendas para o exemplo novo: {previsao}')


# In[ ]:


plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)  # Pontos do gráfico
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', linewidth=2)  # Linha diagonal
plt.title('Vendas Reais vs Vendas Previstas')  # Título do gráfico
plt.xlabel('Vendas Reais')  # Rótulo do eixo x
plt.ylabel('Vendas Previstas')  # Rótulo do eixo y
plt.grid(True)  # Mostrar grade
plt.show()

