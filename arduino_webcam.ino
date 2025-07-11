#include <Servo.h>

Servo servo;

int posNeutra = 90;
int posAlvo = 90;

unsigned long tempoUltimoMovimento = 0;
bool emMovimento = false;

void setup() {
  Serial.begin(9600);
  servo.attach(9);
  servo.write(posNeutra);
  Serial.println("Sistema pronto. Aguardando comandos do Python.");
}

void loop() {
  if (Serial.available() > 0 && !emMovimento) {
    int comando = Serial.parseInt();
    if (comando == 0) { // azul
      posAlvo = posNeutra - 20;  // vira 20 graus à esquerda
      if (posAlvo < 0) posAlvo = 0;
      servo.write(posAlvo);
      Serial.println("Detectado AZUL -> movendo 20° para esquerda.");
      tempoUltimoMovimento = millis();
      emMovimento = true;
    } 
    else if (comando == 180) { // vermelho
      posAlvo = posNeutra + 20; // vira 20 graus à direita
      if (posAlvo > 180) posAlvo = 180;
      servo.write(posAlvo);
      Serial.println("Detectado VERMELHO -> movendo 20° para direita.");
      tempoUltimoMovimento = millis();
      emMovimento = true;
    }
  }

  // Após 5 segundos, volta para posição neutra
  if (emMovimento && millis() - tempoUltimoMovimento >= 5000) {
    servo.write(posNeutra);
    Serial.println("Voltando para posição neutra (90°).");
    emMovimento = false;
  }
}
