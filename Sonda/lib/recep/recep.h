#ifndef RECEP_H
#define RECEP_H

#include <Arduino.h>
#include <WiFi.h>

class Recep
{
private:
    WiFiClient* _cliente;

public:
    Recep();
    void asociarCliente(WiFiClient &cliente);
    bool recibir(String &mensaje);
};

#endif