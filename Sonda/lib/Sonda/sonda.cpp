#include "sonda.h"
#include <Wire.h>
#include <Adafruit_ADS1X15.h>

// Objeto global para el ADS1115
static Adafruit_ADS1X15 ads;

bool inicializarMuestras() {
    // Configuración automática de pines I2C según la tarjeta compilada
    #if defined(BOARD_XIAO_ESP32C6)
        Wire.begin(6, 7); // Pines SDA y SCL para XIAO C6
    #else
        Wire.begin(21, 22); // Pines SDA y SCL estándar para ESP32 DevKit
    #endif

    Wire.setClock(400000); // Modo I2C rápido (400 kHz)

    if (!ads.begin(0x48, &Wire)) {
        Serial.println("[ERROR] No se encontró el ADC ADS1115.");
        return false;
    }
    
    ads.setGain(GAIN_ONE); // Rango de +/- 4.096V
    return true;
}

// Función adaptada para capturar los canales individuales y la diferencia simultáneamente
void tomarMuestrasCanales(int &valA, int &valB, int &valDiferencia) {
    // Leemos el canal 0 de forma individual (Canal A)
    int16_t canalA = ads.readADC_SingleEnded(0);
    // Leemos el canal 1 de forma individual (Canal B)
    int16_t canalB = ads.readADC_SingleEnded(1);
    // Realizamos la lectura diferencial (o la resta matemática A - B)
    int16_t diferencia = ads.readADC_Differential_0_1();

    valA = (int)canalA;
    valB = (int)canalB;
    valDiferencia = (int)diferencia;
}

// Conservamos tu función original por si la usas en otra parte del proyecto
void tomarMuestra(int muestra[], int cantidadMuestras, int tiempoEntreMuestras, bool imprimirMuestra) {
    for (int i = 0; i < cantidadMuestras; i++) {
        int16_t valor_adc = ads.readADC_Differential_0_1();
        muestra[i] = (int)valor_adc;

        if (imprimirMuestra) {
            Serial.println(muestra[i]);
        }

        delay(tiempoEntreMuestras);
    }
}

void SerialMuestra(const int muestra[], int cantidadMuestras, bool formatoCSV) {
    for (int i = 0; i < cantidadMuestras; i++) {
        Serial.print(muestra[i]);
        if (formatoCSV && i < cantidadMuestras - 1) {
            Serial.print(",");
        }
    }
    Serial.println();
}