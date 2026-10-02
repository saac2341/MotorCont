#ifndef PINES_H
#define PINES_H

// =============================================================================
// CONFIGURACIÓN PARA ESP32 DEV MODULE
// =============================================================================
#if defined(BOARD_ESP32_DEV) || defined(ARDUINO_ESP32_DEV)

    /// Definición de pines I2C (ADS1115)
    #define PIN_ADS1115_SDA  21
    #define PIN_ADS1115_SCL  22

    /// Definición de pines de salida
    #define PIN_LED          2

// =============================================================================
// CONFIGURACIÓN PARA SEEED XIAO ESP32-C6
// =============================================================================
#elif defined(BOARD_XIAO_ESP32C6) || defined(ARDUINO_SEEED_XIAO_ESP32C6)

    /// Definición de pines I2C (ADS1115) - Pines por defecto del XIAO C6
    #define PIN_ADS1115_SDA  22  // Pin D4 (SDA)
    #define PIN_ADS1115_SCL  23  // Pin D5 (SCL)

    /// Definición de pines de salida
    #define PIN_LED          15  // LED integrado o salida de uso general

// =============================================================================
// ERROR EN CASO DE NO DETECTAR PLACA
// =============================================================================
#else
    #error "Placa no soportada o macro de entorno no definida en platformio.ini"
#endif

#endif // PINES_H