#include <Arduino.h>
#include <sonda.h>

const int CANTIDAD_MUESTRAS = 100;
int arregloMuestras[CANTIDAD_MUESTRAS];

void setup() {
  Serial.begin(115200);
  ///Programa para ver muestras de un sensor en tiempo real y almacenarlas en memoria para su posterior análisis.
  delay(8000);
  printf("Iniciando captura de muestras...\n");

  if (!inicializarMuestras()) {
    while (1);
  }
}

void loop() {
  // Captura 100 muestras, almacenándolas en 'arregloMuestras' 
  // y transmitiendo CADA muestra por Serial en tiempo real (cada 10 ms = 100 Hz).
  tomarMuestra(arregloMuestras, CANTIDAD_MUESTRAS, 10, true);

  // En este punto, 'arregloMuestras' ya tiene las 100 lecturas guardadas en memoria 
  // por si quieres hacer algún cálculo local (promedio, detección de picos, etc.)
}