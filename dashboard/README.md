# Dashboard de Cerro Seguro

Aplicación local para interpretar las lecturas reales del RAK4631 y revisar alertas SOS. Consulta la misma base SQLite que el receptor USB, sin abrir el puerto serie. La captura continúa al cerrar el navegador.

## Iniciar desde cero

Requisitos: Python 3.10 o posterior, firmware/configuración de [RAK y receptor](../firmware/meshtastic/README.md) y las dependencias de la estación. Python 3.11 es la versión verificada. El Heltec V3.2 utiliza firmware oficial `heltec-v3`; el RAK utiliza el firmware modificado con el NodeID real de la estación. Ambos deben conocer el contacto público del otro para los mensajes directos.

### Un solo comando en macOS

Conectar el Heltec con un cable USB de datos, alimentar el RAK y cerrar los monitores serie o clientes que ocupen el USB. Desde la raíz del proyecto:

```bash
./iniciar.sh
```

En el primer inicio se crea `.venv` y se instalan las dependencias si faltan; esa instalación requiere internet. El script detecta el puerto compatible, inicia la recepción y espera que SQLite esté preparada antes de iniciar el dashboard. Abre [http://127.0.0.1:8765](http://127.0.0.1:8765) en el navegador. El estado USB del dashboard y el mensaje «Estación conectada» confirman la conexión; disponer de la página no confirma recepción de radio.

Valores predeterminados: RAK `!1630f9c9`, canal 0, sondeo de 120 s, puerto web 8765 y `station-data/cerroseguro.sqlite3`. La ruta relativa de la base se interpreta desde la raíz del proyecto, aunque se invoque el script desde otra carpeta. Se conserva el histórico.

La detección usa la descripción USB Heltec o el adaptador CP210x que incorpora V3/V3.2, sin seleccionar el USB nativo del RAK. Identifica un puerto compatible, no el NodeID de la radio. Si hay varios candidatos, se muestran las opciones y se solicita una selección explícita. No se prueban conexiones en todos los puertos. Referencias: [Heltec V3](https://heltec.org/project/wifi-lora-32-v3/) y [enumeración USB de pySerial](https://pyserial.readthedocs.io/en/latest/tools.html#serial.tools.list_ports.comports).

```bash
# Mostrar los puertos sin abrirlos ni iniciar servicios.
./iniciar.sh --list-ports

# Elegir el puerto si hay varios adaptadores conectados.
./iniciar.sh --port /dev/cu.usbserial-0001

# Otra configuración de ejecución, manteniendo el mismo firmware.
./iniciar.sh --no-browser --dashboard-port 8766

# Consultar todas las opciones.
./iniciar.sh --help
```

`--rak-node '!1630f9c9'` permite indicar otro emisor autorizado y se puede repetir; no reconfigura el destino SOS del firmware. También se admiten `--database` y `--poll-seconds`. El intervalo es compartido por el sondeo y la detección de datos antiguos en el dashboard.

**Ctrl+C** detiene los dos servicios y libera sus recursos. Si uno termina de forma inesperada o falla el arranque del segundo, el script cierra el otro y muestra el error. Un puerto web ocupado se detecta antes de iniciar la estación. La reconexión USB sigue a cargo del servicio de estación; si el sistema asigna otro nombre al puerto después de reconectar el cable, reiniciar el comando para detectarlo de nuevo.

### Ejecución manual en dos terminales

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r station/requirements.txt
```

Primera terminal: iniciar la recepción, sustituyendo el puerto y NodeID por los equipos utilizados.

```bash
.venv/bin/python station/main.py \
  --port /dev/cu.usbserial-0001 \
  --rak-node '!1630f9c9' \
  --channel 0 \
  --telemetry-poll-seconds 120 \
  --database station-data/cerroseguro.sqlite3
```

Cuando indique que la estación está conectada, abrir una segunda terminal en la raíz del repositorio:

```bash
.venv/bin/python dashboard/server.py \
  --database station-data/cerroseguro.sqlite3 \
  --expected-interval 120 \
  --port 8765
```

Abrir **[http://127.0.0.1:8765](http://127.0.0.1:8765)** en el navegador. El servidor solo escucha en este computador. En Windows usar `.venv\Scripts\python` y el puerto `COM` correspondiente.

Para detener cada proceso, utilizar `Ctrl+C` en su terminal. La base conserva sus datos; reiniciar con la misma ruta permite consultar el histórico. El receptor debe ser el único programa que utilice el USB del Heltec. La página y sus gráficas no requieren servicios, fuentes o scripts de terceros.

## Información para decidir

| Vista o indicador | Lectura y acción |
|---|---|
| Temperatura y humedad | Última medición real recibida del nodo, en °C y % HR |
| Gráfica e histórico | Rango de 1 h, 6 h, 24 h, 7 días o fechas personalizadas; reconocer cambios locales |
| Media, mínima, máxima y variación | Estadísticas de temperatura del período seleccionado; no equivalen a un pronóstico |
| Antigüedad del dato | Tras tres intervalos sin una lectura, revisar alimentación y enlace antes de interpretar el valor |
| Estado USB | Heartbeat del receptor cada cinco segundos; tras 15 s sin actualización se muestra sin conexión verificada |
| SOS por revisar | Eventos guardados sin revisión del operador; abrir el registro y seguir el procedimiento del proyecto |
| Intervalo observado | Mediana de las diferencias de recepción del mismo nodo; no es una tasa de pérdida de paquetes |

La pantalla consulta cada cinco segundos; el receptor solicita telemetría cada 120 segundos para el ensayo de banco. Son frecuencias distintas. La publicación automática del RAK permanece en 1800 segundos por el mínimo del canal público de esta versión de Meshtastic. El sondeo no garantiza recepción de cada solicitud.

Las fechas visibles usan `America/Santiago`. Los filtros personalizados indican la hora local del equipo. La persistencia y las exportaciones conservan UTC; la hora de captura se mantiene separada de la hora de recepción. Si el reloj del sensor no está sincronizado y reporta un tiempo anterior a 2020, el dashboard presenta la captura como desconocida.

## SOS y revisión del operador

- **ACK pendiente:** el envío de confirmación está pendiente en la estación.
- **ACK encolado:** la estación guardó la alerta y entregó el ACK al radio para envío. No demuestra que el RAK lo haya recibido.
- **Por revisar / Revisada:** estado humano independiente. «Marcar revisada» guarda la revisión y «Reabrir» permite revertirla.
- **REGISTERED en el RAK:** solo puede comprobarse en el emisor o con evidencia adicional. El dashboard no lo deduce del encolado del ACK.

La revisión no transmite otro SOS ni una orden de rescate. Las alertas de la campaña del 15 de noviembre son pruebas de banco.

## Datos, exportación y API

La fuente es `measurements`, `alerts` y `ack_outbox` de la estación. `station_status` permite observar su estado de conexión y `alert_reviews` conserva la revisión del operador sin modificar los registros del protocolo.

- `GET /api/dashboard?hours=24&node=!1630f9c9`: lecturas, estadísticas, frescura y alertas.
- `GET /api/dashboard?since=2026-11-15T00:00:00Z&until=2026-11-16T00:00:00Z`: rango UTC explícito.
- `GET /api/export.csv`: exportación del rango seleccionado, con hora UTC, temperatura °C, humedad % HR, RSSI dBm y SNR dB.
- `POST /api/alerts/review`: JSON con `node`, `event_id` y `reviewed` booleano.

Las consultas usan conexiones independientes, límites de visualización y parámetros SQL. La vista carga hasta 20.000 lecturas y hasta 500 alertas recientes del nodo; los contadores incluyen todo su registro. El CSV exporta todas las lecturas del rango, hasta 366 días, sin el límite de la vista. La base no borra registros automáticamente. Las escrituras de revisión validan origen, formato e identidad del evento.

## Verificación

```bash
.venv/bin/python -m unittest discover -s station/tests -v
.venv/bin/python -m unittest discover -s dashboard/tests -v
.venv/bin/python -m unittest discover -s tools/tests -v
```

La API se prueba con bases temporales. El [ensayo de banco](../testing/banco-rak-heltec.md) y la [verificación del Avance 3](../docs/verificacion-avance3.md) separan los resultados físicos de las pruebas de software. Las capturas de [vista general](../testing/evidencias/dashboard-vista-general.jpg), [alertas](../testing/evidencias/dashboard-alertas.jpg) y [móvil](../testing/evidencias/dashboard-movil.jpg) usan datos reales.
