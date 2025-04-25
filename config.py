#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Color

# Inicializa o brick EV3
ev3 = EV3Brick()

# Inicializa os motores
motor_d = Motor(Port.D)  # Motor conectado à porta D
motor_a = Motor(Port.A)  # Motor conectado à porta A

# Inicializa os sensores
sensor_cor = ColorSensor(Port.S3)  # Sensor de cor conectado à porta 3
sensor_toque = TouchSensor(Port.S1)  # Sensor de toque conectado à porta 1

# Variáveis globais
queue = []  # Lista global para armazenar as cores detectadas
scanning = False  # Controle do estado de escaneamento
MAX_QUEUE_SIZE = 6  # Tamanho máximo da fila de cores

# Mapeamento de cores para ângulos de rotação
COR_PARA_ANGULO = {
    Color.BLUE: 10,
    Color.GREEN: 180,
    Color.YELLOW: 360,
    Color.RED: 530
}

# Mapeamento de cores para arquivos de som
COR_PARA_SOM = {
    Color.BLUE: "Colors/Blue",
    Color.GREEN: "Colors/Green",
    Color.YELLOW: "Colors/Yellow",
    Color.RED: "Colors/Red"
}

# Definição das cores
BLUE = 2
GREEN = 3
YELLOW = 4
RED = 5 