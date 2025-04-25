from pybricks.parameters import Stop, Direction
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

from config import (
    ev3, motor_d, motor_a, sensor_toque,
    queue, COR_PARA_ANGULO, COR_PARA_SOM
)

def sort():
    """
    Função responsável por ordenar e processar as cores detectadas.
    Executa movimentos específicos para cada cor na fila.
    """
    global queue
    
    # Reproduz o som "System Ready" até que esteja concluído
    ev3.speaker.play_file(SoundFile.SYSTEM_READY)
    
    # Mostra informação "LEGO / EV3" no monitor
    ev3.screen.print("LEGO / EV3")
    
    # Espera 1 segundo antes de iniciar
    wait(1000)
    
    # Iniciar motor no sentido horário
    motor_d.run(Direction.CLOCKWISE)
    
    # Espera até que o botão seja pressionado
    while not sensor_toque.pressed():
        wait(10)  # Pequena pausa para não sobrecarregar o processador
    
    # Define o motor para flutuar ao parar
    motor_d.stop(Stop.COAST)
    
    # Para o motor
    motor_d.stop()
    
    # Configura o motor para manter a posição ao parar
    motor_d.run_target(speed=100, target_angle=0, then=Stop.HOLD)
    
    # Processa cada cor na fila
    for cor in queue:
        if cor in COR_PARA_ANGULO:
            # Toca o som correspondente à cor
            ev3.speaker.play_file(COR_PARA_SOM[cor])
            # Executa a rotação correspondente
            motor_d.run_angle(speed=100, rotation_angle=COR_PARA_ANGULO[cor])
            wait(500)  # Pequena pausa entre cores
    
    # Motor A - Movimentos adicionais
    # 90 graus no sentido horário
    motor_a.run_angle(speed=100, rotation_angle=90)
    
    # 90 graus no sentido anti-horário
    motor_a.run_angle(speed=-100, rotation_angle=90) 