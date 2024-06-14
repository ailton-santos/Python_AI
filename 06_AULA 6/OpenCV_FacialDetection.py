import cv2

# Carregar o classificador Haar para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Função para capturar e processar a imagem da webcam
def capture_and_detect_faces():
    # Captura de vídeo da webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Captura frame por frame
        ret, frame = cap.read()

        if not ret:
            print("Não foi possível capturar a imagem da webcam")
            break

        # Conversão para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecção de rostos
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Desenhar retângulo ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Exibir o frame com os rostos detectados
        cv2.imshow('Detecção de Rostos', frame)

        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libere a captura quando tudo estiver terminado
    cap.release()
    cv2.destroyAllWindows()

# Executar a função
capture_and_detect_faces()
