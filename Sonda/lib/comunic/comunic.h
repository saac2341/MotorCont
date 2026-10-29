/// Parar la función, abierta,boleana, recibirara la comunican 

#ifndef COMUNIC_H
#define COMUNIC_H

#include <Arduino.h>
#include <WiFi.h>

class Comunic
{
private:
    WiFiClient* _cliente;

public:
    Comunic();
    void asociarCliente(WiFiClient &cliente);
    void enviarDato(float dato);
};

#endif