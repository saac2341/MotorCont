#ifndef SONDA_H
#define SONDA_H

#include <Arduino.h>

bool inicializarMuestras();
void tomarMuestrasCanales(int &valA, int &valB, int &valDiferencia);
void tomarMuestra(int muestra[], int cantidadMuestras, int tiempoEntreMuestras, bool imprimirMuestra);
void SerialMuestra(const int muestra[], int cantidadMuestras, bool formatoCSV);

#endif