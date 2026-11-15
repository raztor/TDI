# Estación de monitoreo por USB

La LILYGO de 915 MHz utiliza firmware Meshtastic oficial y se conecta al computador mediante USB. El servicio recibe mensajes de los RAK configurados, guarda telemetría y alertas en SQLite y confirma cada SOS después de completar la transacción. La LILYGO conserva la responsabilidad del transporte de radio; no requiere firmware propio.

## Instalación y ejecución

Requisitos: Python 3.10 o posterior, LILYGO con firmware oficial compatible, cable USB de datos y NodeID del RAK. El puerto serie debe quedar disponible para este servicio; cerrar otras aplicaciones que lo estén utilizando.

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r station/requirements.txt
.venv/bin/python station/main.py --port /dev/cu.usbserial-XXXX --rak-node '!12345678'
```

En Windows, usar `.venv\Scripts\python` y el puerto correspondiente, por ejemplo `COM4`. El identificador mostrado es ilustrativo: reemplazarlo por el RAK real. La estación obtiene su propio NodeID de la LILYGO. Se pueden agregar varios argumentos `--rak-node`, uno por cada emisor autorizado.

Opciones: `--channel 0` y `--database station-data/cerroseguro.sqlite3`. El canal debe coincidir con `--channel` del firmware del RAK. La base se crea en la ruta indicada y persiste entre reinicios.

## Recepción y confirmación

1. Verificar origen, destino, canal y formato del SOS.
2. Guardar la alerta con clave única `(nodo, evento)` y la confirmación pendiente en una transacción SQLite.
3. Enviar la confirmación por USB y Meshtastic al nodo de origen.
4. Registrar que la confirmación fue encolada para radio. Este estado no demuestra que el RAK la haya recibido.

Un duplicado incrementa su contador de recepción y vuelve a generar la confirmación, sin crear otra alerta. Si el USB falla, la salida permanece pendiente y se reintenta con espera creciente. Los ACK pendientes sobreviven al reinicio del servicio. Si el almacenamiento falla, no se confirma el registro del SOS.

Solo se almacenan los nodos indicados por `--rak-node`. Los mensajes de otros participantes de MeshChile quedan fuera del registro del proyecto. Una alerta debe tener como destino la LILYGO; la telemetría puede llegar dirigida a ella o difundida al canal.

## Datos persistidos

| Tabla | Contenido |
|---|---|
| `alerts` | Nodo, identificador de evento, primera y última recepción UTC, número de recepciones |
| `ack_outbox` | Confirmaciones pendientes, canal, intentos, último error y hora de encolado |
| `measurements` | Nodo, ID de paquete, hora de recepción UTC, hora de captura si existe, métricas ambientales, RSSI y SNR |

Las métricas conservan los valores del paquete de telemetría. Antes de presentar presión o resistencia de gas en un dashboard, verificar las unidades de la implementación de sensor utilizada. La variable principal de esta etapa es temperatura. La ausencia de hora del sensor se guarda como `NULL`; la hora del computador se registra por separado como recepción.

La base usa WAL y sincronización `FULL`. Para trasladarla con el servicio activo, utilizar la API de backup de SQLite; no copiar solo el archivo principal mientras existan transacciones o archivos WAL.

## Integración con el dashboard

El dashboard debe consultar esta base y mostrar última temperatura, histórico, antigüedad del dato, estado USB y alertas registradas. El servicio de ingestión es independiente del navegador: cerrar el dashboard no debe detener la recepción. La interfaz web y su API están pendientes de implementación.

## Pruebas de software

```bash
.venv/bin/python -m unittest discover -s station/tests -v
```

Las pruebas usan paquetes sintéticos y bases temporales: no transmiten por radio ni constituyen mediciones del prototipo. Cubren persistencia antes del ACK, duplicados, reinicios, desconexión USB, errores de escritura, filtrado y decodificación de telemetría.
