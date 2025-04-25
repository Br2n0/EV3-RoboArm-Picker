#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

from config import ev3
from sort_module import sort
from reset_module import reset
from scan_module import scan

def main():
    """
    Função principal que coordena todas as operações do robô.
    Executa a sequência: reset -> scan -> sort
    """
    try:
        # Feedback inicial
        ev3.screen.clear()
        ev3.screen.print("Iniciando...")
        ev3.speaker.beep()
        wait(1000)

        # Reset
        ev3.screen.clear()
        ev3.screen.print("Resetando...")
        reset()
        
        # Scan
        ev3.screen.clear()
        ev3.screen.print("Escaneando cores...")
        scan()
        
        # Sort
        ev3.screen.clear()
        ev3.screen.print("Ordenando cores...")
        sort()
        
        # Finalização bem-sucedida
        ev3.screen.clear()
        ev3.screen.print("Programa concluído!")
        ev3.speaker.play_file(SoundFile.MISSION_ACCOMPLISHED)
        wait(2000)
        
    except KeyboardInterrupt:
        # Tratamento para interrupção manual
        ev3.screen.clear()
        ev3.screen.print("Programa interrompido")
        ev3.speaker.beep(frequency=200, duration=500)
        wait(1000)
        
    except Exception as e:
        # Tratamento de outros erros
        ev3.screen.clear()
        ev3.screen.print("Erro:")
        ev3.screen.print(str(e))
        ev3.speaker.beep(frequency=200, duration=1000)
        wait(2000)
    
    finally:
        # Limpeza final
        ev3.screen.clear()
        ev3.screen.print("Finalizando...")
        wait(1000)
        ev3.screen.clear()

# Executa o programa principal
if __name__ == "__main__":
    main() 