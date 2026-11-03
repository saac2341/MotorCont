# MotorCont Interface

Interfaz gráfica desarrollada en Python para la captura, visualización, procesamiento y exportación de señales provenientes de dispositivos ESP32.

El proyecto utiliza PySide6 para la interfaz gráfica y permite trabajar con datos obtenidos mediante conexión Wi-Fi o puerto serial.

## Funcionalidades actuales

### Panel principal

- Navegación entre los diferentes módulos de la aplicación.
- Configuración de dirección IP y puerto de conexión.
- Conexión TCP con un dispositivo ESP32.
- Indicadores visuales del estado de conexión.
- Puertos disponibles: `80`, `8080`, `5000` y `3333`.

### Visualización de señales

El módulo de señales permite:

- Iniciar y detener la captura de datos.
- Visualizar una gráfica temporal.
- Mostrar el ángulo actual mediante un goniómetro.
- Mostrar indicadores de actividad cerebral.
- Normalizar los valores mostrados en la gráfica.

Actualmente, la captura del módulo principal utiliza datos de prueba generados mediante funciones senoidales. Esta sección está preparada para ser conectada posteriormente a datos reales de sensores.

### Comunicación con ESP32

El módulo ESP32 permite:

- Detectar puertos seriales disponibles.
- Seleccionar el puerto de comunicación.
- Configurar la velocidad de transmisión.
- Conectar y desconectar el dispositivo.
- Leer datos recibidos desde el ESP32.
- Mostrar los datos recibidos en la interfaz.

La velocidad configurada inicialmente es de `115200 baudios`.

### Procesamiento y filtrado de señales

El módulo de filtros permite:

- Introducir muestras manualmente.
- Cargar datos separados por líneas, comas o punto y coma.
- Aplicar filtros digitales:
  - Pasa bajas.
  - Pasa altas.
  - Pasa banda.
- Visualizar la señal original y la señal filtrada.
- Configurar la frecuencia de corte.
- Exportar los resultados en formato CSV o JSON.

El procesamiento utiliza `NumPy`, `SciPy` y `PyQtGraph`.

### Integración con Edge Impulse

El módulo Edge Impulse permite:

- Configurar un token de acceso.
- Guardar la configuración localmente.
- Seleccionar archivos `.csv`, `.json`, `.txt` o `.zip`.
- Consultar los archivos seleccionados.
- Abrir la plataforma de Edge Impulse desde la aplicación.
- Preparar archivos para su análisis.

Esta integración se encuentra en desarrollo y algunas operaciones todavía funcionan como preparación previa al análisis.

## Tecnologías utilizadas

- Python
- PySide6
- Qt Designer
- PyQtGraph
- NumPy
- SciPy
- PySerial
- Edge Impulse

## Estructura del proyecto

```text
Interface/
├── main.py                  # Punto de entrada de la aplicación
├── assets/                  # Iconos y recursos gráficos
├── data/                    # Datos de trabajo
├── forms/                   # Interfaces generadas con Qt Designer
│   └── ui/                  # Archivos fuente .ui
├── scrips/                  # Scripts auxiliares
├── src/
│   ├── main_window.py      # Ventana principal
│   ├── network_conexion.py # Comunicación de red
│   ├── signal_filters.py   # Funcionalidad relacionada con filtros
│   └── views/              # Módulos visuales de la aplicación
└── test/                   # Pruebas y prototipos