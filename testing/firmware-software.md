# Validación de software del firmware y la estación

**Fecha:** 15 de noviembre de 2026. **Plataforma de destino:** RAK4631/nRF52840. **Base:** Meshtastic `v2.7.26.54e0d8d`.

## Alcance

El módulo SOS se compila junto con Meshtastic para RAK4631. La lógica del botón y la confirmación se verifica en un ejecutable C++ independiente. El receptor USB se prueba con SQLite temporal y paquetes sintéticos. Estas pruebas no generan tráfico de radio.

## Pruebas aprobadas

| Componente | Verificación | Resultado |
|---|---|---|
| Estado SOS | Rebotes y pulsos breves; dos segundos de pulsación estable; interrupción de la pulsación | Aprobado |
| Estado SOS | Un evento por pulsación; liberación obligatoria; botón mantenido al arrancar | Aprobado |
| Reintentos | Espera, límite de intentos y estado UNCONFIRMED; temporizador al desbordar `millis()` | Aprobado |
| Confirmación | Evento, origen, destino, canal y longitud del mensaje; rechazo de ACK tardío o de otro evento | Aprobado |
| Estación | Escritura visible desde otra conexión SQLite antes de encolar el ACK | Aprobado |
| Estación | Duplicados con un solo registro de alerta y una nueva confirmación | Aprobado |
| Estación | Cola pendiente recuperada tras reinicio; error USB con espera y reintento | Aprobado |
| Estación | Sin ACK cuando falla la escritura; rechazo de nodos, destinos y canales ajenos | Aprobado |
| Telemetría | Decodificación protobuf, deduplicación por nodo/paquete, rechazo de valores no finitos y mensajes malformados | Aprobado |
| Tiempo | Hora de recepción UTC separada de hora de captura; ausencia de reloj del sensor como NULL | Aprobado |
| Configuración | Perfiles YAML válidos con el protobuf de Meshtastic Python 2.7.11; ANZ, slot 20, transmisión y CLIENT_MUTE | Aprobado |

La suite Python contiene 11 pruebas. El ejecutable C++ se compila con `-Wall -Wextra -Werror`. Los comandos se mantienen en [firmware](../firmware/meshtastic/README.md) y [estación](../station/README.md).

## Compilación de firmware

Entorno PlatformIO: `cerroseguro-rak4631`. PlatformIO 6.1.18, plataforma Nordic 10.11.0 y toolchain 1.90301.200702. Framework Meshtastic/Adafruit fijado al commit `9ddcbc9568b12f102f9e88bd4d1b88ea789213a4`.

Resultado: compilación completa aprobada, con salidas UF2 y HEX. Uso de RAM: 105.268 de 248.832 bytes (42,3 %). Uso de flash: 760.320 de 815.104 bytes (93,3 %). Las ampliaciones deben comprobar nuevamente el margen disponible.

La compilación de comprobación utiliza NodeID de estación sin asignar, por lo que el módulo SOS queda deshabilitado al arrancar. Antes de cargar, es necesario preparar y compilar con la dirección real de la LILYGO. Los archivos UF2/HEX de comprobación no son una configuración operativa del prototipo.

## Aceptación pendiente

- Instalación del adaptador RAK13002 y pulsador IO6–GND.
- Identificación de la revisión exacta de la LILYGO y su NodeID.
- Carga y verificación de los perfiles de MeshChile en ambas placas.
- Detección del BME680 y comparación de lecturas y unidades.
- SOS y ACK de persistencia mediante radio, USB y SQLite con dispositivos reales.
- Pruebas de recorrido por la malla, pérdidas, latencia, consumo y autonomía.
- Interfaz web del dashboard e histórico consultable desde ella.

Los casos de aceptación física se describen en [prueba SOS/Meshtastic](sos-meshtastic.md). Los protocolos T01–T08 permanecen pendientes de ejecución completa.
