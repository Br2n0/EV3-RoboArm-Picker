# EV3-RoboArm-Picker

## Descrição do Projeto
Este é um projeto base para desenvolvimento de um sistema automatizado de picking utilizando o LEGO MINDSTORMS EV3. O objetivo final é implementar um braço robótico capaz de identificar e manipular objetos em uma esteira transportadora, simulando operações de picking em ambientes industriais.

### Versão Atual (Base)
A versão atual serve como fundação para o sistema completo, implementando:
- Sistema base de controle dos motores
- Estrutura modular do código
- Tratamento de erros e feedback
- Interface básica de operação

### Desenvolvimento Futuro
O projeto será expandido para incluir:
- Implementação do braço robótico
- Sistema de identificação de objetos na esteira
- Algoritmos de picking e placing
- Integração com sistema de esteira
- Otimização de movimentos e tempo de ciclo

### Aplicações Previstas
- Simulação de operações de picking em armazéns
- Demonstração de automação industrial
- Prototipagem de sistemas de manipulação
- Estudo de processos logísticos automatizados

## Estrutura do Projeto
```
.
├── config.py           # Configurações globais e inicializações
├── sort_module.py      # Módulo de ordenação das cores
├── reset_module.py     # Módulo de reset do sistema
├── scan_module.py      # Módulo de escaneamento de cores
├── main.py            # Arquivo principal do programa
└── README.md          # Este arquivo
```

## Funcionalidades
- **Reset**: Prepara o robô para uma nova operação
- **Scan**: Detecta e armazena até 6 cores diferentes
- **Sort**: Ordena os objetos baseado nas cores detectadas
- **Feedback**: Visual (display) e sonoro durante operação

## Requisitos de Hardware
- LEGO MINDSTORMS EV3 Brick
- 2 Motores Grandes (Portas A e D)
- 1 Sensor de Cor (Porta 3)
- 1 Sensor de Toque (Porta 1)

## Configuração das Portas
- Motor A: Motor para movimentação do braço
- Motor D: Motor para rotação da base
- Sensor de Cor: Porta S3
- Sensor de Toque: Porta S1

## Como Configurar o Ambiente

### 1. Preparação do EV3 Brick
1. Faça o download da imagem mais recente do EV3 MicroPython:
   - Visite: https://education.lego.com/pt-br/downloads/mindstorms-ev3/software
   - Baixe o arquivo de imagem do EV3 MicroPython

2. Prepare o cartão SD:
   - Formate um cartão SD (mínimo 4GB)
   - Grave a imagem do EV3 MicroPython no cartão
   - Insira o cartão no EV3 Brick

### 2. Configuração do Visual Studio Code
1. Instale o VS Code: https://code.visualstudio.com/
2. Instale as extensões:
   - LEGO MINDSTORMS EV3 MicroPython
   - Python

### 3. Conectando ao EV3
1. Ligue o EV3 Brick
2. Conecte o EV3 ao computador via:
   - USB (mais recomendado para desenvolvimento)
   - Bluetooth
   - Wi-Fi (se disponível)

### 4. Configurando o Projeto
1. Abra o VS Code
2. Vá em File > Open Folder e selecione a pasta do projeto
3. Verifique se o EV3 está conectado:
   - Deve aparecer um ícone do EV3 na barra inferior
   - Clique no ícone para verificar a conexão

## Como Executar
1. Certifique-se que todos os sensores e motores estão conectados corretamente
2. Abra o VS Code e conecte ao EV3
3. Carregue todos os arquivos do projeto para o EV3
4. Execute o arquivo `main.py`

## Sequência de Operação
1. **Inicialização**:
   - O programa inicia com um beep
   - Display mostra "Iniciando..."

2. **Reset**:
   - Robô se move para posição inicial
   - Limpa dados anteriores
   - Display mostra "Resetando..."

3. **Scan**:
   - Aguarda detecção de cores
   - Emite sons para cada cor detectada
   - Display mostra progresso

4. **Sort**:
   - Processa cores detectadas
   - Move objetos para posições específicas
   - Emite sons correspondentes

5. **Finalização**:
   - Som de conclusão
   - Display mostra "Programa concluído!"

## Tratamento de Erros
- O programa possui tratamento para diversos tipos de erros
- Feedback visual e sonoro em caso de problemas
- Opção de interrupção manual segura

## Manutenção
Para modificar o comportamento do robô, você pode ajustar:
- Ângulos de rotação em `config.py`
- Velocidades dos motores nos módulos específicos
- Sequência de operações em `main.py`

## Suporte
Em caso de problemas:
1. Verifique as conexões dos sensores e motores
2. Confirme se o EV3 está com a versão correta do MicroPython
3. Verifique as mensagens de erro no display do EV3 