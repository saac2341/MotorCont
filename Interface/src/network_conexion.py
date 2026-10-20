"""Libreria encarga de la realizar las conexiones 
con la ESP32 a traves de WIFI"""

class NetworkConexion:
    """Clase encargada de la conexión con la ESP32 a través de WIFI."""

    def __init__(self, ip_address: str, port: int):
        self.ip_address = ip_address
        self.port = port
        self.socket = None

    def connect(self):
        """Establece la conexión con la ESP32."""
        # Aquí iría el código para establecer la conexión con la ESP32
        pass

    def disconnect(self):
        """Cierra la conexión con la ESP32."""
        # Aquí iría el código para cerrar la conexión con la ESP32
        pass

    def send_data(self, data):
        """Envía datos a la ESP32."""
        # Aquí iría el código para enviar datos a la ESP32
        pass

    def receive_data(self):
        """Recibe datos de la ESP32."""
        # Aquí iría el código para recibir datos de la ESP32
        pass