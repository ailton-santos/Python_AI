# -*- coding: utf-8 -*-
"""sklearn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mqHldc2_VEBfckHXfcUpkghxWPje--2W
"""

import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC

"""*Identificar um porco ou cachorro*

*Características*

- Pelo (Curto ou Longo?)
- Latir (Faz "au-au"?)
- Rabo (Rabo curto ou longo?)

*Sempre comparar algo (cachorro)*

0 - Tem pelo curto
1 - Tem pelo longo

-------------------

0 - Não faz "au-au"
1 - Faz "au-au"

-------------------

0 - Rabo curto
1 - Rabo longo

-------------------

0 - Orelha Pequenas e Arredondadas
1 - Orelha Pontudas e Eretas

-------------------

0 - Focinho Curto e Rechonchudo
1 - Focinho alongado e pontiagudo
"""

porco1 = [0, 1, 0, 0, 0] #Tem pelo Curto / Não faz "au-au" / Rabo Curto
porco2 = [0, 1, 1, 0, 1] #Tem pelo Curto / Faz "au-au" / Rabo Longo
porco3 = [1, 1, 0, 1, 0] #Tem pelo Longo / Faz "au-au" / Rabo Longo

cachorro1 = [0, 1, 1, 1, 0] #Tem pelo Longo / Faz "au-au" / Rabo Longo
cachorro2 = [1, 0, 1, 1, 1] #Tem pelo Longo / Não faz "au-au" / Rabo Longo
cachorro3 = [1, 1, 1, 0, 1]

treinoX = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treinoY = [1, 1, 1, 0, 0, 0] # 0 - Cachorro || 1 - Porco

modelo = LinearSVC()

modelo.fit (treinoX, treinoY)

animalMisterioso = [1, 0, 0, 1, 1]

descoberta = modelo.predict([animalMisterioso])

if descoberta == 1:
  print ("Animal misterioso é porco!")
elif descoberta == 0:
  print ("Animal misterioso é cachorro!")
else:
  ("Animal desconhecido")