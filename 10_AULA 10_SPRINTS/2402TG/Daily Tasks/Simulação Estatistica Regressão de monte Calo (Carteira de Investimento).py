#!/usr/bin/env python
# coding: utf-8

# In[5]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1)
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 100000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150)
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.show()


# In[6]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1)
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 100000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150)
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=['blue', 'green', 'red', 'purple'])
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.show()



# In[7]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1)
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 100000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150)
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=['blue', 'green', 'red', 'purple'])
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True)
plt.show()

# Determinando o melhor investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]

# Exibindo o melhor investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')


# In[8]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 1000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')


# In[9]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 1000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
indice_pior_acao = retornos.mean().idxmin()
pior_acao = lista_acoes[indice_pior_acao]

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')
print(f'A ação que teve o pior desempenho foi {pior_acao}.')


# In[10]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 1000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
pior_acao = retornos.mean().idxmin()

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')
print(f'A ação que teve o pior desempenho foi {pior_acao}.')


# In[11]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 1000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
retornos_finais = (retornos + 1).cumprod().iloc[-1] * capital_inicial
pior_acao = retornos_finais.idxmin()

# Calculando as perdas de cada ação
perdas_acoes = capital_inicial - retornos_finais

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')

print("Perdas individuais por ação:")
for acao, perda in perdas_acoes.items():
    print(f'Ação: {acao}, Perda: R$ {perda:,.2f}')

print(f'A ação que teve o pior desempenho foi {pior_acao}.')

# Plotando gráfico de barras das perdas individuais por ação
plt.figure(figsize=(12, 6))
plt.bar(perdas_acoes.index, perdas_acoes.values, color=['blue', 'green', 'red', 'purple', 'orange'], edgecolor='black')
plt.ylabel('Perda (R$)')
plt.xlabel('Ação')
plt.title('Perdas Individuais por Ação')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()


# In[12]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Calculando retornos e matriz de covariância
retornos = precos.pct_change().dropna()
media_retornos = retornos.mean()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))

# Premissas para simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 3
capital_inicial = 1000

# Adicionando retorno médio
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, len(lista_acoes)))

# Cholesky decomposition
L = LA.cholesky(matriz_covariancia)

# Gerando simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)

for s in range(numero_simulacoes):
    Rpdf = np.random.normal(size=[dias_projetados, len(lista_acoes)])
    retornos_sinteticos = matriz_retorno_medio + np.dot(Rpdf, L.T)
    retornos_carteira[:, s] = np.cumprod(np.dot(retornos_sinteticos, pesos_carteira) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os resultados da simulação Monte Carlo
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Estatísticas dos resultados
montante_99 = np.percentile(montante_final, 1)
montante_95 = np.percentile(montante_final, 5)
montante_mediano = np.percentile(montante_final, 50)
cenarios_com_lucro = (len(montante_final[montante_final > 1000]) / len(montante_final)) * 100

# Exibindo resultados
print(f'''Ao investir R$ 1000,00 na carteira {lista_acoes},
podemos esperar esses resultados para os próximos 3 anos,
utilizando o método de Monte Carlo com 10 mil simulações:

Com 50% de probabilidade, o montante será maior que R$ {montante_mediano:,.2f}.
Com 95% de probabilidade, o montante será maior que R$ {montante_95:,.2f}.
Com 99% de probabilidade, o montante será maior que R$ {montante_99:,.2f}.
Em {cenarios_com_lucro:.2f}% dos cenários, foi possível obter lucro nos próximos 3 anos.
''')

# Plotando distribuição dos montantes finais
plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Cálculo dos retornos para outros tipos de investimento
retorno_poupanca = 0.04  # Exemplo de retorno anual de 4% para poupança
retorno_renda_fixa = 0.06  # Exemplo de retorno anual de 6% para renda fixa
retorno_tesouro_direto = 0.05  # Exemplo de retorno anual de 5% para Tesouro Direto

# Calculando montante final para esses investimentos após 3 anos
montante_poupanca = capital_inicial * (1 + retorno_poupanca) ** 3
montante_renda_fixa = capital_inicial * (1 + retorno_renda_fixa) ** 3
montante_tesouro_direto = capital_inicial * (1 + retorno_tesouro_direto) ** 3

# Média dos montantes finais da simulação de Monte Carlo
montante_simulacao_mediana = np.median(montante_final)

# Ajustando os valores finais para lucro/perda
montante_simulacao_mediana = capital_inicial + (montante_simulacao_mediana - capital_inicial)
montante_poupanca = capital_inicial + (montante_poupanca - capital_inicial)
montante_renda_fixa = capital_inicial + (montante_renda_fixa - capital_inicial)
montante_tesouro_direto = capital_inicial + (montante_tesouro_direto - capital_inicial)

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 3 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
retornos_finais = (retornos + 1).cumprod().iloc[-1] * capital_inicial
pior_acao = retornos_finais.idxmin()

# Calculando as perdas de cada ação
perdas_acoes = capital_inicial - retornos_finais

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')

print("Perdas individuais por ação:")
for acao, perda in perdas_acoes.items():
    print(f'Ação: {acao}, Perda: R$ {perda:,.2f}')

print(f'A ação que teve o pior desempenho foi {pior_acao}.')

# Plotando gráfico de barras das perdas individuais por ação
plt.figure(figsize=(12, 6))
plt.bar(perdas_acoes.index, perdas_acoes.values, color=['blue', 'green', 'red', 'purple', 'orange'], edgecolor='black')
plt.ylabel('Perda (R$)')
plt.xlabel('Ação')
plt.title('Perdas Individuais por Ação')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()


# In[14]:


# Introdução
# Simulação de Monte Carlo para Projeção de Retornos de Carteira de Ações
# Objetivo: Utilizar simulação de Monte Carlo para projetar retornos de uma carteira de ações.
# Ferramentas: Python, bibliotecas NumPy, Matplotlib, Pandas DataReader, yFinance.

# Importação de Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from numpy import linalg as LA
import yfinance as yf
import matplotlib.ticker as ticker

# Coleta de Dados do Yahoo Finance
lista_acoes = ['BTLG11', 'MXRF11', 'RBRF11', 'RECR11', 'TGAR11', 'VGIP11', 'VISC11']
lista_acoes = [acao + '.SA' for acao in lista_acoes]
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=365 * 5)
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']

# Impressão dos Preços
print(precos)

# Cálculo de Retornos e Covariância
retornos = precos.pct_change().dropna()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))
numero_acoes = len(lista_acoes)

# Retornos Sintéticos - Simulação de Monte Carlo
numero_simulacoes = 10000
dias_projetados = 252 * 5  # 5 anos de dias úteis
capital_inicial = 1000
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, numero_acoes))
L = LA.cholesky(matriz_covariancia)

# Gerando Simulações
retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)
for s in range(numero_simulacoes):
    rpdf = np.random.normal(size=(dias_projetados, numero_acoes))
    retornos_sinteticos = matriz_retorno_medio + np.inner(rpdf, L)
    retornos_carteira[:, s] = np.cumprod(np.inner(pesos_carteira, retornos_sinteticos) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]

# Plotando os Resultados
plt.figure(figsize=(12, 6))
plt.plot(retornos_carteira, linewidth=1, alpha=0.1, color='blue')
plt.ylabel('Dinheiro (R$)')
plt.xlabel('Dias')
plt.title('Simulação Monte Carlo do Retorno da Carteira')
plt.grid(True)
plt.tight_layout()
plt.show()

# Distribuição dos Montantes Finais
montante_99 = str(np.percentile(montante_final, 1))
montante_95 = str(np.percentile(montante_final, 5))
montante_mediano = str(np.percentile(montante_final, 50))
cenarios_com_lucros = str((len(montante_final[montante_final > 1000]) / len(montante_final)) * 100) + '%'
print(f'ao investir R$ 1000,00 na carteira {lista_acoes}, podemos esperar esses resultados nos próximos 3 anos, utilizando o método de Monte Carlo, com 10 mil simulações:\n'
      f'    Com 50% de probabilidade, o montante será maior que R$ {montante_mediano}.\n'
      f'    Com 95% de probabilidade, o montante será maior que R$ {montante_95}.\n'
      f'    Com 99% de probabilidade, o montante será maior que R$ {montante_99}.\n'
      f'    Em {cenarios_com_lucros} dos cenários, foi possível obter lucro nos próximos 3 anos.')

# Histogramas dos Montantes Finais
config = dict(histtype='stepfilled', alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(montante_final, **config)
formatter = ticker.FuncFormatter(lambda x, pos: f'R${x:,.0f}')
ax.xaxis.set_major_formatter(formatter)
plt.title('Distribuição dos Montantes Finais com a Simulação MC')
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Ajustando os valores finais para lucro/perda
montante_simulacao_mediana = capital_inicial + (np.median(montante_final) - capital_inicial)
montante_poupanca = capital_inicial * (1 + 0.04) ** 5
montante_renda_fixa = capital_inicial * (1 + 0.06) ** 5
montante_tesouro_direto = capital_inicial * (1 + 0.05) ** 5

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)

# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 5 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
retornos_finais = (retornos + 1).cumprod().iloc[-1] * capital_inicial
pior_acao = retornos_finais.idxmin()

# Calculando as perdas de cada ação
perdas_acoes = capital_inicial - retornos_finais

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')

print("Perdas individuais por ação:")
for acao, perda in perdas_acoes.items():
    print(f'Ação: {acao}, Perda: R$ {perda:,.2f}')

print(f'A ação que teve o pior desempenho foi {pior_acao}.')

# Plotando gráfico de barras das perdas individuais por ação
plt.figure(figsize=(12, 6))
plt.bar(perdas_acoes.index, perdas_acoes.values, color=['blue', 'green', 'red', 'purple', 'orange'], edgecolor='black')
plt.ylabel('Perda (R$)')
plt.xlabel('Ação')
plt.title('Perdas Individuais por Ação')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()


# # Simulação Estatística Regressão de Monte Carlo (Carteira de Investimento)
# 
# A simulação estatística de Monte Carlo é uma técnica amplamente utilizada para modelar e analisar sistemas complexos e incertos. Na área de investimentos, essa abordagem é empregada para projetar os retornos potenciais de uma carteira de ações ao longo de um período futuro, permitindo uma avaliação mais precisa dos riscos e das oportunidades associadas.
# 
# Neste estudo, aplicamos a simulação de Monte Carlo para avaliar o desempenho de uma carteira de ações composta pelas empresas WEGE3 (WEG S.A.), PCAR3 (Grupo Pão de Açúcar), IRBR3 (IRB Brasil Resseguros), PETR4 (Petrobras) e VALE3 (Vale S.A.). O objetivo é fornecer recomendações de investimento para os próximos três anos

# In[ ]:


import datetime as dt
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Definindo lista de ações
lista_acoes = ['WEGE3', 'PCAR3', 'IRBR3', 'PETR4', 'VALE3']
lista_acoes = [acao + '.SA' for acao in lista_acoes]

# Definindo datas para o período de dados
data_final = dt.datetime.now()
data_inicial = data_final - dt.timedelta(days=300)

# Usando yfinance para obter os preços ajustados de fechamento das ações
precos = yf.download(lista_acoes, start=data_inicial, end=data_final)['Adj Close']


# In[ ]:


# Cálculo de Retornos e Covariância

retornos = precos.pct_change().dropna()
matriz_covariancia = retornos.cov()
pesos_carteira = np.full(len(lista_acoes), 1 / len(lista_acoes))
numero_acoes = len(lista_acoes)


# In[ ]:


# Retornos Sintéticos - Simulação de Monte Carlo

numero_simulacoes = 10000
dias_projetados = 252 * 3  # 3 anos de dias úteis
capital_inicial = 1000
retorno_medio = retornos.mean(axis=0).to_numpy()
matriz_retorno_medio = retorno_medio * np.ones(shape=(dias_projetados, numero_acoes))
L = LA.cholesky(matriz_covariancia)


# In[ ]:


# Gerando Simulações

retornos_carteira = np.zeros([dias_projetados, numero_simulacoes])
montante_final = np.zeros(numero_simulacoes)
for s in range(numero_simulacoes):
    rpdf = np.random.normal(size=(dias_projetados, numero_acoes))
    retornos_sinteticos = matriz_retorno_medio + np.inner(rpdf, L)
    retornos_carteira[:, s] = np.cumprod(np.inner(pesos_carteira, retornos_sinteticos) + 1) * capital_inicial
    montante_final[s] = retornos_carteira[-1, s]


# In[ ]:


# Plotando distribuição dos montantes finais

plt.figure(figsize=(12, 6))
config = dict(histtype="stepfilled", alpha=0.8, density=False, bins=150)
plt.hist(montante_final, **config)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.title("Distribuição dos Montantes Finais com Simulação de Monte Carlo")
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


# In[ ]:


# Histogramas dos Montantes Finais
config = dict(histtype='stepfilled', alpha=0.8, density=False, bins=150, color='skyblue', edgecolor='black')
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(montante_final, **config)
formatter = ticker.FuncFormatter(lambda x, pos: f'R${x:,.0f}')
ax.xaxis.set_major_formatter(formatter)
plt.title('Distribuição dos Montantes Finais com a Simulação MC')
plt.xlabel('Montante Final (R$)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()


# In[ ]:


# Ajustando os valores finais para lucro/perda
montante_simulacao_mediana = capital_inicial + (np.median(montante_final) - capital_inicial)
montante_poupanca = capital_inicial * (1 + 0.04) ** 5
montante_renda_fixa = capital_inicial * (1 + 0.06) ** 5
montante_tesouro_direto = capital_inicial * (1 + 0.05) ** 5

# Criando um DataFrame para facilitar a visualização
data = {
    'Investimento': ['Carteira de Ações', 'Poupança', 'Renda Fixa', 'Tesouro Direto'],
    'Montante Final': [montante_simulacao_mediana, montante_poupanca, montante_renda_fixa, montante_tesouro_direto]
}
df_resultados = pd.DataFrame(data)


# In[ ]:


# Plotando gráfico de barras comparativo
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red', 'purple']
plt.bar(df_resultados['Investimento'], df_resultados['Montante Final'], color=cores, edgecolor='black')
plt.ylabel('Montante Final (R$)')
plt.xlabel('Tipo de Investimento')
plt.title('Comparação de Investimentos Após 5 Anos')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()


# In[ ]:


# Determinando o melhor e pior investimento
melhor_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmax()]
pior_investimento = df_resultados.loc[df_resultados['Montante Final'].idxmin()]
perda_pior_investimento = capital_inicial - pior_investimento['Montante Final']

# Identificando a ação que teve o pior desempenho
retornos_finais = (retornos + 1).cumprod().iloc[-1] * capital_inicial
pior_acao = retornos_finais.idxmin()

# Calculando as perdas de cada ação
perdas_acoes = capital_inicial - retornos_finais


# In[ ]:


# Calculando as perdas de cada ação
perdas_acoes = capital_inicial - retornos_finais

# Exibindo o melhor e pior investimento
print(f'O melhor investimento no momento é {melhor_investimento["Investimento"]} com um montante final esperado de R$ {melhor_investimento["Montante Final"]:,.2f}.')
print(f'O pior investimento no momento é {pior_investimento["Investimento"]} com um montante final esperado de R$ {pior_investimento["Montante Final"]:,.2f}, resultando em uma perda de R$ {perda_pior_investimento:,.2f}.')

print("Perdas individuais por ação:")
for acao, perda in perdas_acoes.items():
    print(f'Ação: {acao}, Perda: R$ {perda:,.2f}')

print(f'A ação que teve o pior desempenho foi {pior_acao}.')


# In[ ]:


# Plotando gráfico de barras das perdas individuais por ação
plt.figure(figsize=(12, 6))
plt.bar(perdas_acoes.index, perdas_acoes.values, color=['blue', 'green', 'red', 'purple', 'orange'], edgecolor='black')
plt.ylabel('Perda (R$)')
plt.xlabel('Ação')
plt.title('Perdas Individuais por Ação')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
plt.grid(True, linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.show()

