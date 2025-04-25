from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

from config import (
    ev3, sensor_cor,
    queue, scanning, MAX_QUEUE_SIZE,
    COR_PARA_ANGULO
)

def scan():
    """
    Função responsável por escanear e detectar cores.
    Armazena as cores detectadas na fila global.
    """
    global queue, scanning
    scanning = True
    
    # Enquanto o comprimento da fila for menor que o máximo
    while len(queue) < MAX_QUEUE_SIZE and scanning:
        try:
            # Mostra informações no display
            ev3.screen.clear()
            ev3.screen.print("Information / Right")
            
            # Escreve a função com o comprimento atual da fila
            ev3.screen.print(f"# {len(queue)}", font=('Arial', 12))
            
            # Inicializa a detecção de cor como falso
            cor_detectada = False
            
            # Repete até que uma cor seja detectada
            while not cor_detectada and scanning:
                # Define a cor atual
                cor_atual = sensor_cor.color()
                
                # Verifica se alguma das cores específicas foi detectada
                if cor_atual in COR_PARA_ANGULO:
                    # Toca um som por 0.1 segundos
                    ev3.speaker.beep(frequency=84, duration=100)
                    
                    # Adiciona a cor à fila
                    queue.append(cor_atual)
                    
                    # Espera até que não detecte mais cor (sensor afastado)
                    while sensor_cor.color() != Color.NONE and scanning:
                        wait(10)
                    
                    # Toca outro som por 0.1 segundos
                    ev3.speaker.beep(frequency=36, duration=100)
                    
                    # Mostra informação no display
                    ev3.screen.print("Information / Backward")
                    
                    # Espera 2 segundos
                    wait(2000)
                    
                    # Marca que uma cor foi detectada
                    cor_detectada = True
                
                wait(10)  # Pequena pausa para não sobrecarregar o CPU
            
        except Exception as e:
            ev3.screen.print(f"Erro no scan: {str(e)}")
            ev3.speaker.beep(frequency=200, duration=1000)
            wait(2000)
        
        # Para o escaneamento quando a condição for verdadeira
        if len(queue) >= MAX_QUEUE_SIZE:
            scanning = False
            ev3.speaker.play_file(SoundFile.READY) 