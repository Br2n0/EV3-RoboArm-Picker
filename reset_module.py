from pybricks.parameters import Stop, Direction
from pybricks.tools import wait

from config import (
    ev3, motor_d, motor_a, sensor_toque,
    queue, scanning
)

def reset():
    """
    Função responsável por resetar o estado do robô.
    Reinicia motores, limpa a fila e prepara para nova operação.
    """
    global queue, scanning
    
    try:
        # Configura velocidade do motor A para 8%
        motor_a.run(speed=8)
        
        # Executa no sentido horário por 2 segundos
        wait(2000)
        
        # Define velocidade para 30%
        motor_a.run(speed=30)
        
        # Gira 180 graus no sentido anti-horário
        motor_a.run_angle(speed=-100, rotation_angle=180)
        
        # Define velocidade do motor D para 30%
        motor_d.run(speed=30)
        
        # Inicia motor D no sentido anti-horário
        motor_d.run(Direction.COUNTERCLOCKWISE)
        
        # Espera até que o botão seja pressionado
        while not sensor_toque.pressed():
            wait(10)
        
        # Define o motor para flutuar ao parar
        motor_d.stop(Stop.COAST)
        
        # Para o motor D
        motor_d.stop()
        
        # Espera 1 segundo
        wait(1000)
        
        # Reinicia o gyro (ângulo controlado)
        motor_a.reset_angle(0)
        motor_d.reset_angle(0)
        
        # Limpa o monitor
        ev3.screen.clear()
        
        # Remove tudo da fila
        queue.clear()
        
        # Para o escaneamento
        scanning = False
        
        # Feedback sonoro de reset concluído
        ev3.speaker.beep()
        
    except Exception as e:
        ev3.screen.print(f"Erro no reset: {str(e)}")
        ev3.speaker.beep(frequency=200, duration=1000) 