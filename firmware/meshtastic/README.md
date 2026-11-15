# Firmware SOS para RAK4631

Adaptación de Meshtastic para RAK4631 con nRF52840, base RAK19007 y sensor RAK1906/BME680. Mantiene la mensajería Meshtastic y la telemetría ambiental del firmware oficial. El módulo `CerroSeguroModule` añade el botón SOS y la confirmación de registro de la estación.

## Hardware

| Elemento | Conexión |
|---|---|
| RAK1906 | Ranura de sensor compatible de la RAK19007; bus I²C WisBlock |
| Pulsador SOS | Normalmente abierto, entre AIN1 de J11 pin 1 y GND; `INPUT_PULLUP`, activo en LOW |
| AIN1 | nRF52840 P0.31, número Arduino GPIO 31; utilizado como entrada digital |
| GND accesible | J10 pin 2 o J12 pin 2 de la propia RAK19007 |
| LED y buzzer de aplicación | No utilizados |

La conexión utiliza los pads de 2,54 mm de la RAK19007, sin módulo de expansión. Se pueden soldar dos cables o instalar pines de cabecera. AIN1 se usa como entrada digital con pull-up interna; el botón solo lo conecta a GND. No conectar el pulsador a VBAT ni a una alimentación externa. El pulsador está pendiente de instalación.

El RAK1906 utiliza I²C y no ocupa AIN1. La medida interna de batería del RAK4631 utiliza AIN0/P0.05, separado de AIN1/P0.31. El módulo Dropzone, que también podría usar AIN1, permanece excluido de la compilación. No utilizar RESET, IO1 ni IO2 como sustitutos del pin seleccionado.

Referencias: [cabeceras de la RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/), [conexiones del RAK1906](https://docs.rakwireless.com/product-categories/wisblock/rak1906/datasheet/), [mapeo y medida de batería en Meshtastic](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/variants/nrf52840/rak4631/variant.h).

## Procedimiento del botón

El módulo muestrea la entrada cada 10 ms, filtra rebotes durante 40 ms y exige 2000 ms de pulsación estable. Un pulso breve o una liberación interrumpen la cuenta. Cada pulsación genera un solo evento; es necesario soltar el botón para volver a activarlo. Un botón mantenido al encender no genera SOS hasta ser liberado y pulsado nuevamente.

Estados: `WAITING`, `REGISTERED` y `UNCONFIRMED`, visibles en logs del RAK. La respuesta de la estación también es un mensaje de texto Meshtastic consultable desde su aplicación. La espera no bloquea la ejecución del firmware ni añade señales LED o sonoras propias.

Mientras un SOS está pendiente se ignoran nuevas pulsaciones. El módulo realiza como máximo tres intentos, separados por 60 segundos sin confirmación. Los valores son configurables y deben evaluarse con la latencia y carga reales de la malla.

## Protocolo

Puerto: `TEXT_MESSAGE_APP`. Todos los SOS se dirigen al NodeID de la estación, sin difusión de alertas al canal completo.

```text
CS1|SOS|0123456789abcdef00000001
CS1|ACK|0123456789abcdef00000001|REGISTRADO
```

El evento tiene 24 caracteres hexadecimales: nonce de arranque de 64 bits y secuencia de 32 bits. Cada reintento mantiene el evento y utiliza un ID de paquete Meshtastic nuevo. El RAK solo acepta una respuesta con origen, destino, canal e identificador coincidentes con el SOS pendiente.

`REGISTRADO` significa que la estación confirmó la escritura en SQLite. No significa atención humana ni respuesta de rescate. Los ACK nativos de radio no cambian el estado del SOS. Para evitar dos mecanismos de retransmisión simultáneos, los mensajes de este protocolo usan `want_ack=false`; la confiabilidad se gestiona con reintentos limitados del evento y la cola persistente de la estación.

El evento pendiente se mantiene en RAM del RAK. Un reinicio del emisor interrumpe su espera; la estación conserva los eventos ya recibidos. La recuperación de SOS pendientes después de reiniciar el RAK queda fuera de esta versión.

## Base de compilación

- Meshtastic `v2.7.26.54e0d8d`, commit `54e0d8d0ab2ff56b3a9ce967e53f79e49af560fb`.
- Framework nRF52 Meshtastic/Adafruit, commit `9ddcbc9568b12f102f9e88bd4d1b88ea789213a4`.
- PlatformIO `6.1.18`; plataforma Nordic `10.11.0`; toolchain `1.90301.200702`.
- Entorno: `cerroseguro-rak4631`, basado en `rak4631`.

La integración copia los archivos del módulo a `src/modules/`, añade su instancia a `Modules.cpp` y crea el entorno PlatformIO del proyecto. El script comprueba el commit base y puede ejecutarse de nuevo sin duplicar el módulo. Las dependencias de sensores y radio proceden del manifiesto de esa versión de Meshtastic.

## Preparar y compilar

Desde la raíz de Cerro Seguro, con Git y Python disponibles:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r firmware/requirements-build.txt -r station/requirements.txt
git clone --branch v2.7.26.54e0d8d --depth 1 --recurse-submodules --shallow-submodules https://github.com/meshtastic/firmware.git ../meshtastic-cerroseguro
.venv/bin/python firmware/meshtastic/prepare.py ../meshtastic-cerroseguro --station-node '!12345678'
.venv/bin/pio run --project-dir ../meshtastic-cerroseguro -e cerroseguro-rak4631
```

Reemplazar `!12345678` por el NodeID real de la LILYGO, obtenido mediante `meshtastic --port PUERTO_LILYGO --info`. Si se omite `--station-node`, se puede comprobar la compilación, pero el SOS permanece deshabilitado. La dirección de la estación queda definida en la compilación; cambiarla requiere volver a preparar, compilar y cargar.

Opciones del script: `--sos-pin 31`, `--channel 0`, `--ack-timeout-ms 60000`, `--max-attempts 3`. Cambiar el pin exige verificar su disponibilidad en el montaje.

Los archivos de salida se generan en `.pio/build/cerroseguro-rak4631/` del checkout de Meshtastic. Para carga se requiere bootloader Arduino del RAK4631; RAK4631-R/RUI3 necesita el procedimiento oficial de conversión de bootloader.

## Configuración de red y sensor

Ambas placas deben ser las variantes de 915 MHz. El perfil de MeshChile usa región `ANZ` (AU/NZ), preset `LONG_FAST`, slot 20 y canal primario LongFast con clave pública `AQ==` (`psk default` en la CLI). La guía indica 919,875 MHz y mantener el ajuste de frecuencia sin modificarlo manualmente.

```bash
.venv/bin/meshtastic --port PUERTO_RAK --configure firmware/config/rak-meshchile.yaml
.venv/bin/meshtastic --port PUERTO_RAK --ch-index 0 --ch-set name LongFast --ch-set psk default
.venv/bin/meshtastic --port PUERTO_LILYGO --configure firmware/config/lilygo-meshchile.yaml
.venv/bin/meshtastic --port PUERTO_LILYGO --ch-index 0 --ch-set name LongFast --ch-set psk default
```

Los perfiles seleccionan `CLIENT_MUTE`, sin retransmisión de mensajes ajenos, y mantienen recepción activa. Los nodos existentes de la red pueden transportar los mensajes dirigidos a la estación. Se configura telemetría ambiental cada 900 segundos; la cadencia de medición y envío debe contrastarse con el consumo y las necesidades del proyecto. La integración de esta versión funciona por RF y USB; MQTT no interviene en el registro ni en el ACK.

En la LILYGO se instala la distribución oficial correspondiente a su modelo exacto, que debe confirmarse antes de flashear. La etiqueta de banda no identifica por sí sola la revisión de placa.

Referencias: [MeshChile](https://meshchile.cl/node-configuration), [telemetría](https://meshtastic.org/docs/configuration/module/telemetry/), [API de módulos](https://meshtastic.org/docs/development/device/module-api/), [bootloader RAK](https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/core-module/).

## Comprobación local y en hardware

```bash
c++ -std=c++17 -Wall -Wextra -Werror -I firmware/meshtastic firmware/tests/sos_state_test.cpp -o /tmp/cerroseguro-sos-test
/tmp/cerroseguro-sos-test
.venv/bin/python -m unittest discover -s station/tests -v
```

La aceptación con dispositivos requiere instalar el pulsador, cargar firmware con la dirección real de la estación, comprobar el sensor y ejecutar la [prueba de integración](../../testing/sos-meshtastic.md). La compilación y las pruebas de software no acreditan el funcionamiento de radio ni la escritura desde dispositivos físicos.
