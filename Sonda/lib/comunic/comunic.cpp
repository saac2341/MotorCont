    ///Declarar la logica de la funciones que se están declarando en el punto h. 

#include "comunic.h"

Comunic::Comunic()
{
    _cliente = nullptr;
}

void Comunic::asociarCliente(WiFiClient &cliente)
{
    _cliente = &cliente;
}

void Comunic::enviarDato(float dato)
{
    if (_cliente != nullptr && _cliente->connected())
    {
        _cliente->println(dato);
    }
}