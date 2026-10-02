///Libreria para tomar muestras.

#include <Arduino.h>

bool inicializarMuestras();

void tomarMuestra(int muestra[], int cantidadMuestras, int tiempoEntreMuestras, bool imprimirMuestra = false);

void SerialMuestra(const int muestra[], int cantidadMuestras, bool formatoCSV) ;
