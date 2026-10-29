#include "recep.h"

Recep::Recep()
{
    _cliente = nullptr;
}

void Recep::asociarCliente(WiFiClient &cliente)
{
    _cliente = &cliente;
}

bool Recep::recibir(String &mensaje)
{
    if (_cliente != nullptr && _cliente->connected())
    {
        if (_cliente->available() > 0)
        {
            mensaje = _cliente->readStringUntil('\n');
            mensaje.trim();
            return true;
        }
    }
    return false;
}