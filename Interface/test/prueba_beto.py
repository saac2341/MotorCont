import socket
import select
import sys
import termios
import tty

# Sustituye con la IP que aparezca en el Monitor Serial del ESP32
IP_ESP32 = "10.188.1.37"
PUERTO = 8080


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    terminal_fd = sys.stdin.fileno()
    configuracion_terminal = termios.tcgetattr(terminal_fd)
    comando = ""

    try:
        print(f"Conectando a {IP_ESP32}:{PUERTO}...")
        sock.connect((IP_ESP32, PUERTO))
        print("¡Conectado exitosamente con la ESP32!")
        print("Escribe un comando y pulsa Enter. Usa Ctrl+C para salir.")

        # Permite leer las teclas inmediatamente, sin esperar Enter.
        tty.setcbreak(terminal_fd)

        prompt = "> "
        sys.stdout.write(prompt)
        sys.stdout.flush()

        while True:
            disponibles, _, _ = select.select(
                [sock, sys.stdin], [], [], 0.1
            )

            # Lectura de datos periódicos de la ESP32.
            if sock in disponibles:
                respuesta = sock.recv(1024)

                if not respuesta:
                    print("\nLa ESP32 cerró la conexión.")
                    break

                datos = respuesta.decode("utf-8", errors="replace").strip()

                # Limpia la línea actual y la redibuja después del mensaje.
                sys.stdout.write(
                    f"\r\033[K[Dato recibido de ESP32]: {datos}\n"
                    f"{prompt}{comando}"
                )
                sys.stdout.flush()

            # Lectura de comandos del teclado.
            if sys.stdin in disponibles:
                tecla = sys.stdin.read(1)

                if tecla in ("\x03", "\x04"):  # Ctrl+C o Ctrl+D
                    break

                if tecla in ("\n", "\r"):
                    if comando.strip():
                        sock.sendall((comando + "\n").encode("utf-8"))
                    comando = ""

                    sys.stdout.write(f"\r\033[K{prompt}")
                    sys.stdout.flush()

                elif tecla in ("\x7f", "\b"):
                    if comando:
                        comando = comando[:-1]
                        sys.stdout.write("\b \b")
                        sys.stdout.flush()

                elif tecla.isprintable():
                    comando += tecla
                    sys.stdout.write(tecla)
                    sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
    except Exception as error:
        print(f"\nError de conexión: {error}")
    finally:
        termios.tcsetattr(
            terminal_fd,
            termios.TCSADRAIN,
            configuracion_terminal
        )
        sock.close()
        print("\nConexión finalizada.")


if __name__ == "__main__":
    main()