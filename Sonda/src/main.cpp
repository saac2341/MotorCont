#include <Arduino.h>
#include <WiFi.h>
#include "comunic.h"
#include "recep.h"
#include "sonda.h"

const char* ssid = "INFINITUM859C_2.4";
const char* password = "aVvf872uhC"; // Mantén tu contraseña exacta

WiFiServer servidor(8080);
WiFiClient cliente;

Comunic comunicacion;
Recep recepcion;

// Variable de control de modo ('H' = Humano, 'P' = Planta)
char modoActual = 'P'; // Inicia por defecto en modo planta

// Parámetros de filtrado digital EMA para el modo Humano
const float ALPHA = 0.1;
float v0_filtered = 0.0;
float v1_filtered = 0.0;

unsigned long ultimoEnvio = 0;

void setup()
{
    Serial.begin(115200);
    delay(1000);

    // Inicializamos el ADS1115 mediante la sonda
    if (inicializarMuestras()) {
        Serial.println("[INFO] Sonda / ADS1115 inicializada correctamente.");
    } else {
        Serial.println("[AVISO] No se encontró el ADS1115 (requerirá el sensor físico).");
    }

    WiFi.begin(ssid, password);
    Serial.print("Conectando a Wi-Fi");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWi-Fi Conectado!");
    Serial.print("IP de la ESP32: ");
    Serial.println(WiFi.localIP());

    servidor.begin();
}

void loop()
{
    // Aceptar nuevo cliente (Python) si se conecta a la red
    if (!cliente || !cliente.connected())
    {
        cliente = servidor.accept();
        if (cliente)
        {
            Serial.println("¡Nuevo cliente (Python) conectado!");
            comunicacion.asociarCliente(cliente);
            recepcion.asociarCliente(cliente);
        }
    }

    // --- RECEPCIÓN DE COMANDOS DESDE PYTHON (Selector de Modo) ---
    String mensajeRecibido = "";
    if (recepcion.recibir(mensajeRecibido))
    {
        mensajeRecibido.trim(); // Limpiamos espacios o saltos de línea
        if (mensajeRecibido == "H" || mensajeRecibido == "P")
        {
            modoActual = mensajeRecibido[0];
            Serial.print("[MODO CAMBIADO] Nuevo perfil activo: ");
            Serial.println(modoActual == 'H' ? "HUMANO (GSR/Hemisferios)" : "PLANTA (Sensores/Bioseñales)");
        }
        else
        {
            Serial.print("Comando recibido: ");
            Serial.println(mensajeRecibido);
        }
    }

    // --- ADQUISICIÓN Y ENVÍO DE DATOS SEGÚN EL MODO (~30 Hz para graficación fluida) ---
    if (millis() - ultimoEnvio >= 33) 
    {
        ultimoEnvio = millis();

        int canalA = 0, canalB = 0, diferencia = 0;
        
        // Obtenemos las lecturas del ADS1115 a través de nuestra sonda
        tomarMuestrasCanales(canalA, canalB, diferencia);

        String paqueteDatos = "";

        if (modoActual == 'H') 
        {
            // Perfil Humano: Incluye voltajes y filtros EMA inspirados en tu reporte de prácticas
            float voltage0 = (canalA * 4.096) / 32767.0; 
            float voltage1 = (canalB * 4.096) / 32767.0;
            float voltage2 = (diferencia * 4.096) / 32767.0;

            v0_filtered = (ALPHA * voltage0) + ((1.0 - ALPHA) * v0_filtered);
            v1_filtered = (ALPHA * voltage1) + ((1.0 - ALPHA) * v1_filtered);

            // Trama extendida para humano (6 columnas)
            paqueteDatos = String(canalA) + "," + String(canalB) + "," + String(diferencia) + "," +
                           String(voltage2, 4) + "," + String(v0_filtered, 4) + "," + String(v1_filtered, 4);
        } 
        else 
        {
            // Perfil Planta: Trama estándar (3 columnas)
            paqueteDatos = String(canalA) + "," + String(canalB) + "," + String(diferencia);
        }

        // Si Python está conectado, enviamos el paquete de manera inalámbrica
        if (cliente && cliente.connected()) 
        {
            cliente.println(paqueteDatos);
        }
    }
}