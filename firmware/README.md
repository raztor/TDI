# Firmware

El RAK4631 utiliza Meshtastic con un módulo SOS propio y la telemetría ambiental del RAK1906/BME680. La estación de banco utiliza un Heltec WiFi LoRa 32 V3.2 de 915 MHz con firmware oficial y enlace USB al computador; también admite una LILYGO compatible. Ambos nodos envían y reciben mensajes con rol CLIENT_MUTE.

## Implementación

| Componente | Código o configuración | Función |
|---|---|---|
| Módulo SOS RAK | [meshtastic/](meshtastic/README.md) | Antirrebote, pulsación sostenida de dos segundos, evento único, reintentos y confirmación |
| Sensor RAK1906 | Telemetría ambiental de Meshtastic | Adquisición de temperatura y variables ambientales |
| Perfil RAK | [rak-meshchile.yaml](config/rak-meshchile.yaml) | ANZ, LongFast, slot 20, CLIENT_MUTE y telemetría |
| Perfil estación, Heltec o LILYGO | [lilygo-meshchile.yaml](config/lilygo-meshchile.yaml) | Meshtastic oficial, CLIENT_MUTE y enlace USB |
| Estación | [station/](../station/README.md) | Recepción por USB, SQLite y ACK posterior al commit |

La placa receptora transporta los mensajes a través de Meshtastic. El estado del SOS cambia a REGISTERED únicamente con la respuesta propia de la estación después de guardar la alerta; el ACK nativo de radio no cierra el evento. Para las pruebas de banco, la estación solicita lecturas ambientales cada 120 segundos mediante `--telemetry-poll-seconds 120`.

## Botón y alimentación

Pulsador normalmente abierto entre AIN1 de J11 pin 1 y GND de la propia RAK19007. AIN1 corresponde a P0.31/GPIO 31 del RAK4631 y se utiliza como entrada digital con pull-up interna. El módulo probado utiliza S a AIN1, G a GND y V libre; su modelo exacto está por identificar. No requiere expansión, LED ni buzzer. El ensayo de banco comprobó el SOS físico y el estado REGISTERED.

El GPIO y los parámetros de envío se definen al preparar el firmware. La dirección de la estación debe ser el NodeID real de la placa receptora. Sin dirección, el módulo SOS permanece deshabilitado.

## Compilación y carga

La [guía del módulo](meshtastic/README.md) fija la versión de Meshtastic, framework, compilador y comandos de preparación. El sensor, el botón y el recorrido completo deben verificarse con hardware antes de presentar resultados funcionales.

La compilación produce archivos UF2 y HEX para RAK4631 con bootloader Arduino. La revisión exacta de la LILYGO debe confirmarse antes de instalar su firmware oficial. No cargar un binario destinado a otra placa o bootloader.

El [ensayo de banco RAK/Heltec](../testing/banco-rak-heltec.md) registra la instalación, la lectura del BME680 y la confirmación del protocolo por radio. La prueba del pulsador físico permanece pendiente.

## Antecedente del Avance 2

El [informe A2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>) documenta ensayos con LoRa puro y capturas de telemetría y SOS/ACK. El código original de esos ensayos está pendiente de versionar. La implementación actual utiliza el transporte Meshtastic y un protocolo de confirmación de registro descrito en la guía del módulo.

## Verificación

- [Prueba de integración con dispositivos](../testing/sos-meshtastic.md).
- [Registro de validación de software](../testing/firmware-software.md).
- Pruebas de estado del botón en `tests/sos_state_test.cpp` y receptor en `../station/tests/`.
