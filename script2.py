import cv2
import numpy as np
import serial
import time

try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Aguarda o Arduino iniciar
    if arduino.is_open and arduino.in_waiting > 0:
        print("Dados disponíveis!")
except serial.SerialException as e:
    print("Erro ao acessar a porta serial:", e)

# Cores em HSV
cores_hsv = {
    'vermelho': [(0, 120, 70), (10, 255, 255)],
    'verde_claro': [(40, 50, 200), (85, 150, 255)],
        # Verde escuro: tons densos e profundos
    'verde_escuro': [(40, 100, 20), (85, 255, 100)],

    # Verde médio: típico da natureza
    'verde_medio': [(40, 150, 100), (85, 255, 200)],

    # Verde claro: tons mais suaves e iluminados
    'verde_claro': [(40, 50, 180), (85, 150, 255)],

    # Verde neon: forte brilho e saturação
    'verde_neon': [(45, 200, 200), (85, 255, 255)],

    # Verde oliva / musgo: esverdeado amarelado
    'verde_oliva': [(25, 50, 50), (45, 200, 180)]




}

servo_posicoes = {
    'verde_medio': 0,
    'vermelho': 180
}

ultima_cor = None
tempo_ultima_acao = 0
delay_minimo = 10  # segundos

cap = cv2.VideoCapture(1)
print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Zoom digital
    h, w, _ = frame.shape
    zoom_factor = 0.5
    new_w, new_h = int(w * zoom_factor), int(h * zoom_factor)
    start_x = (w - new_w) // 2
    start_y = (h - new_h) // 2
    frame = frame[start_y:start_y + new_h, start_x:start_x + new_w]
    frame = cv2.resize(frame, (w, h))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cor_detectada = None

    for cor, (lower, upper) in cores_hsv.items():
        mascara = cv2.inRange(hsv, np.array(lower), np.array(upper))
        contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > 2000:
                x, y, w_box, h_box = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (255, 255, 255), 2)
                cv2.putText(frame, cor, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
                cor_detectada = cor
                break

    tempo_atual = time.time()
    if cor_detectada and (tempo_atual - tempo_ultima_acao) >= delay_minimo:
        if arduino and cor_detectada in servo_posicoes:
            angulo = servo_posicoes[cor_detectada]
            arduino.write(f"{angulo}\n".encode())
            print(f"Enviado para Arduino: {angulo} graus por cor {cor_detectada}")
            ultima_cor = cor_detectada
            tempo_ultima_acao = tempo_atual


    # 🔁 Lê mensagens enviadas do Arduino e exibe no terminal
    if arduino and arduino.in_waiting > 0:
        resposta = arduino.readline().decode(errors='ignore').strip()
        if resposta:
            print(f"[Arduino]: {resposta}")

    cv2.imshow("Detecção de Tampas (com Zoom)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
