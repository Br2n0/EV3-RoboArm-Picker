import cv2
import numpy as np
import serial
import time

try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
    print("Conectado ao Arduino na COM3")
except:
    print("Arduino não conectado.")
    arduino = None

cores_hsv = {
    'vermelho': [(0, 120, 70), (10, 255, 255)],
    'azul': [(100, 150, 0), (140, 255, 255)]
}

servo_posicoes = {
    'azul': 0,
    'vermelho': 180
}

ultima_cor = None
cap = cv2.VideoCapture(1)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cor_detectada = None

    for cor, (lower, upper) in cores_hsv.items():
        mascara = cv2.inRange(hsv, np.array(lower), np.array(upper))
        contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,255), 2)
                cv2.putText(frame, cor, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
                cor_detectada = cor
                break  # pega só o primeiro grande encontrado

    # Só envia se mudou
    if cor_detectada and cor_detectada != ultima_cor:
        if arduino and cor_detectada in servo_posicoes:
            angulo = servo_posicoes[cor_detectada]
            arduino.write(f"{angulo}\n".encode())
            print(f"Enviado para Arduino: {angulo} graus por cor {cor_detectada}")
        ultima_cor = cor_detectada

    cv2.imshow("Detecção de Tampas", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
