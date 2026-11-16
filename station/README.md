# Estación de monitoreo por USB

La estación utiliza un Heltec WiFi LoRa 32 V3.2 de 915 MHz con firmware Meshtastic oficial y conexión USB al computador. También admite una LILYGO compatible. El servicio recibe mensajes de los RAK configurados, guarda telemetría y alertas en SQLite y confirma cada SOS después de completar la transacción. La placa conserva la responsabilidad del transporte de radio; no requiere firmware propio.

## Instalación y ejecución

En macOS, [iniciar.sh](../iniciar.sh) permite ejecutar recepción y dashboard juntos, con detección automática del puerto:

```bash
./iniciar.sh
```

Utiliza el nodo RAK `!1630f9c9` y sondeo de 120 s. El histórico se mantiene en `station-data/cerroseguro.sqlite3`; Ctrl+C detiene ambos procesos. Ver [opciones y detección USB](../dashboard/README.md#un-solo-comando-en-macos). La ejecución manual del receptor se conserva a continuación.

Requisitos: Python 3.10 o posterior, placa receptora de 915 MHz con firmware oficial compatible, cable USB de datos y NodeID del RAK. El puerto serie debe quedar disponible para este servicio; cerrar otras aplicaciones que lo estén utilizando.

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r station/requirements.txt
.venv/bin/python station/main.py --port /dev/cu.usbserial-XXXX --rak-node '!12345678'
```

En Windows, usar `.venv\Scripts\python` y el puerto correspondiente, por ejemplo `COM4`. El identificador mostrado es ilustrativo: reemplazarlo por el RAK real. La estación obtiene su propio NodeID de la placa conectada. Se pueden agregar varios argumentos `--rak-node`, uno por cada emisor autorizado.

Opciones: `--channel 0` y `--database station-data/cerroseguro.sqlite3`. El canal debe coincidir con `--channel` del firmware del RAK. La base se crea en la ruta indicada y persiste entre reinicios.

Para las pruebas de banco se utiliza `--telemetry-poll-seconds 120`. La estación solicita una lectura ambiental al conectar y cada 120 segundos mediante mensajes dirigidos a los RAK autorizados. Las respuestas se guardan por el mismo circuito de recepción; una solicitud no garantiza respuesta ni crea una medición. El sondeo no bloquea el procesamiento de SOS y ACK. El valor predeterminado `0` desactiva estas solicitudes.

La publicación ambiental automática y el sondeo son independientes. Meshtastic 2.7.26 aplica un mínimo de 1800 segundos a la publicación automática en el canal público predeterminado para este rol; configurar 120 en ese campo no produce publicaciones cada dos minutos. La solicitud desde el computador permite usar esa cadencia durante la prueba sin modificar el límite del firmware.

Antes del ensayo, ambos dispositivos deben conocer la identidad y clave pública del otro. Meshtastic puede obtenerlas mediante anuncios de nodo o importación de contactos por USB. Un mensaje directo rechazado con `PKI_SEND_FAIL_PUBLIC_KEY` no llegó a radio. El servicio sincroniza el reloj de la placa receptora al conectar; el reloj del RAK se sincroniza durante su configuración.

## Recepción y confirmación

1. Verificar origen, destino, canal y formato del SOS.
2. Guardar la alerta con clave única `(nodo, evento)` y la confirmación pendiente en una transacción SQLite.
3. Enviar la confirmación por USB y Meshtastic al nodo de origen.
4. Registrar que la confirmación fue encolada para radio. Este estado no demuestra que el RAK la haya recibido.

Un duplicado incrementa su contador de recepción y vuelve a generar la confirmación, sin crear otra alerta. Si el USB falla, la salida permanece pendiente y se reintenta con espera creciente. Los ACK pendientes sobreviven al reinicio del servicio. Si el almacenamiento falla, no se confirma el registro del SOS.

Solo se almacenan los nodos indicados por `--rak-node`. Los mensajes de otros participantes de MeshChile quedan fuera del registro del proyecto. Una alerta debe tener como destino la placa receptora; la telemetría puede llegar dirigida a ella o difundida al canal.

## Datos persistidos

| Tabla | Contenido |
|---|---|
| `alerts` | Nodo, identificador de evento, primera y última recepción UTC, número de recepciones |
| `ack_outbox` | Confirmaciones pendientes, canal, intentos, último error y hora de encolado |
| `measurements` | Nodo, ID de paquete, hora de recepción UTC, hora de captura si existe, métricas ambientales, RSSI y SNR |

Las métricas conservan los valores del paquete de telemetría. Antes de presentar presión o resistencia de gas en un dashboard, verificar las unidades de la implementación de sensor utilizada. La variable principal de esta etapa es temperatura. La ausencia de hora del sensor se guarda como `NULL`; la hora del computador se registra por separado como recepción.

La base usa WAL y sincronización `FULL`. Para trasladarla con el servicio activo, utilizar la API de backup de SQLite; no copiar solo el archivo principal mientras existan transacciones o archivos WAL.

## Integración con el dashboard

El [dashboard local](../dashboard/README.md) consulta esta base y muestra temperatura, humedad, histórico, estadísticas, antigüedad, estado USB y alertas. El servicio de ingestión es independiente del navegador: cerrar el dashboard no detiene la recepción. El heartbeat de `station_status` se actualiza cada cinco segundos. Las revisiones del operador se guardan en `alert_reviews`, separadas de la cola de ACK.

## Pruebas de software

```bash
.venv/bin/python -m unittest discover -s station/tests -v
```

Las pruebas usan paquetes sintéticos y bases temporales: no transmiten por radio ni constituyen mediciones del prototipo. Cubren persistencia antes del ACK, duplicados, reinicios, desconexión USB, errores de escritura, filtrado y decodificación de telemetría.
