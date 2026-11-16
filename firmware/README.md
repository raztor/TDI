# Firmware

El RAK4631 utiliza Meshtastic con un módulo SOS propio y la telemetría ambiental del RAK1906/BME680. La LILYGO de 915 MHz utiliza firmware oficial y actúa como interfaz USB de la estación del computador. Ambos nodos envían y reciben mensajes con rol CLIENT_MUTE.

## Implementación

| Componente | Código o configuración | Función |
|---|---|---|
| Módulo SOS RAK | [meshtastic/](meshtastic/README.md) | Antirrebote, pulsación sostenida de dos segundos, evento único, reintentos y confirmación |
| Sensor RAK1906 | Telemetría ambiental de Meshtastic | Adquisición de temperatura y variables ambientales |
| Perfil RAK | [rak-meshchile.yaml](config/rak-meshchile.yaml) | ANZ, LongFast, slot 20, CLIENT_MUTE y telemetría |
| Perfil LILYGO | [lilygo-meshchile.yaml](config/lilygo-meshchile.yaml) | Meshtastic oficial, CLIENT_MUTE y enlace USB |
| Estación | [station/](../station/README.md) | Recepción por USB, SQLite y ACK posterior al commit |

La LILYGO confirma el transporte de los mensajes a través de Meshtastic. El estado del SOS cambia a REGISTERED únicamente con la respuesta propia de la estación después de guardar la alerta; el ACK nativo de radio no cierra el evento.

## Botón y alimentación

Pulsador normalmente abierto entre AIN1 de J11 pin 1 y GND de la propia RAK19007. AIN1 corresponde a P0.31/GPIO 31 del RAK4631 y se utiliza como entrada digital con pull-up interna. No requiere módulo de expansión ni LED o buzzer. La instalación física del pulsador está pendiente.

El GPIO y los parámetros de envío se definen al preparar el firmware. La dirección de la estación debe ser el NodeID real de la LILYGO. Sin dirección, el módulo SOS permanece deshabilitado.

## Compilación y carga

La [guía del módulo](meshtastic/README.md) fija la versión de Meshtastic, framework, compilador y comandos de preparación. El sensor, el botón y el recorrido completo deben verificarse con hardware antes de presentar resultados funcionales.

La compilación produce archivos UF2 y HEX para RAK4631 con bootloader Arduino. La revisión exacta de la LILYGO debe confirmarse antes de instalar su firmware oficial. No cargar un binario destinado a otra placa o bootloader.

## Antecedente del Avance 2

El [informe A2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>) documenta ensayos con LoRa puro y capturas de telemetría y SOS/ACK. El código original de esos ensayos está pendiente de versionar. La implementación actual utiliza el transporte Meshtastic y un protocolo de confirmación de registro descrito en la guía del módulo.

## Verificación

- [Prueba de integración con dispositivos](../testing/sos-meshtastic.md).
- [Registro de validación de software](../testing/firmware-software.md).
- Pruebas de estado del botón en `tests/sos_state_test.cpp` y receptor en `../station/tests/`.
