import socket
import time
import threading

IP_ESP32 = "10.188.1.150"  # Reemplaza con la IP impresa en el monitor serial
PUERTO = 8080

def escuchar_esp32(sock):
    """ Hilo para recibir datos continuos desde la ESP32 """
    while True:
        try:
            respuesta = sock.recv(1024).decode('utf-8')
            if respuesta:
                print(f"\n[Dato recibido de ESP32]: {respuesta.strip()}")
        except Exception as e:
            print(f"\nConexión perdida: {e}")
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"Conectando a {IP_ESP32}:{PUERTO}...")
        sock.connect((IP_ESP32, PUERTO))
        print("¡Conectado exitosamente!")

        # Hilo en segundo plano para recibir datos en tiempo real
        hilo_recepcion = threading.Thread(target=escuchar_esp32, args=(sock,), daemon=True)
        hilo_recepcion.start()

        # Bucle principal para enviar comandos
        while True:
            comando = input("Escribe un comando para enviar al ESP32 (o 'salir'): ")
            if comando.lower() == 'salir':
                break
            sock.sendall((comando + '\n').encode('utf-8'))
            time.sleep(0.1)

    except Exception as e:
        print(f"Error en la conexión: {e}")
    finally:
        sock.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()