# -*- coding: utf-8 -*-
"""OpenCV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ziXOR5sVJrHnlgaMzyF0Znrg05dGCe17
"""

import cv2
from google.colab.patches import cv2_imshow

# Carrega a imagem
imagem = cv2.imread('imagem.jpeg')
if imagem is None:
    print("Error: Image could not be loaded!")
    exit()
cv2_imshow(imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Converte a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Carrega o classificador de face
classificador_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if classificador_face.empty():
    print("Error: Haarcascade classifier could not be loaded!")
    exit()

# Detecta faces na imagem
faces = classificador_face.detectMultiScale(imagem_cinza, 1.1, 4)

# Desenha retângulos ao redor das faces detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Exibe a imagem com as detecções
cv2_imshow(imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()