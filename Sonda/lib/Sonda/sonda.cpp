#include "sonda.h"
#include <pines.h>
#include <Adafruit_ADS1X15.h>
#include <Wire.h>

static Adafruit_ADS1115 ads;

static const float ALPHA = 0.15f; 
static float filteredValue = 0.0f;

bool inicializarMuestras() {
  Wire.begin(PIN_ADS1115_SDA, PIN_ADS1115_SCL);
  Wire.setClock(400000); // Modo I2C rápido (400 kHz)

  if (!ads.begin(0x48, &Wire)) {
    Serial.println("[ERROR] No se encontró el ADC ADS1115.");
    return false;
  }

  // GAIN_ONE: ±4.096V (ideal para módulos alimentados a 3.3V / 5V)
  ads.setGain(GAIN_ONE);

  // 250 SPS: Tasa óptima para equilibrio entre velocidad y bajo ruido
  ads.setDataRate(RATE_ADS1115_250SPS);

  filteredValue = 0.0f;
  return true;
}

void tomarMuestra(int muestra[], int cantidadMuestras, int tiempoEntreMuestras, bool imprimirInmediato) {
  for (int i = 0; i < cantidadMuestras; i++) {
    // 1. Lectura del canal A0 (salida del módulo GSR)
    int16_t rawADC = ads.readADC_SingleEnded(0);

    // 2. Filtro exponencial
    if (filteredValue == 0.0f && rawADC > 0) {
      filteredValue = static_cast<float>(rawADC);
    } else {
      filteredValue = (ALPHA * static_cast<float>(rawADC)) + ((1.0f - ALPHA) * filteredValue);
    }

    // 3. Almacenar valor filtrado en el arreglo
    muestra[i] = static_cast<int>(filteredValue);

    // 4. Imprimir inmediatamente por el puerto serial para la GUI
    if (imprimirInmediato) {
      // Opcional: Si deseas enviar el valor en Voltios en lugar del RAW, usa:
      // float voltios = ads.computeVolts(muestra[i]);
      // Serial.println(voltios, 4);

      Serial.println(muestra[i]); 
    }

    // 5. Retardo de muestreo
    if (tiempoEntreMuestras > 0) {
      delay(tiempoEntreMuestras);
    }
  }
}

void SerialMuestra(const int muestra[], int cantidadMuestras, bool formatoCSV) {
  if (formatoCSV) {
    for (int i = 0; i < cantidadMuestras; i++) {
      Serial.print(muestra[i]);
      if (i < cantidadMuestras - 1) {
        Serial.print(",");
      }
    }
    Serial.println();
  } else {
    for (int i = 0; i < cantidadMuestras; i++) {
      Serial.println(muestra[i]);
    }
  }
}