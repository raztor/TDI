# Ensayo de banco RAK4631 y Heltec V3.2

**Fecha local:** 15 de noviembre de 2026, America/Santiago.

## Equipos y configuración

| Componente | Configuración verificada |
|---|---|
| Emisor | RAK4631, NodeID `!1630f9c9`, base RAK19007 |
| Firmware RAK | Meshtastic `2.7.26.54e0d8d`, entorno `cerroseguro-rak4631` |
| Bootloader RAK | UF2 0.4.3, SoftDevice S140 6.1.1 |
| Sensor | RAK1906/BME680, montado en ranura trasera; respuesta ambiental comprobada |
| Estación | Heltec WiFi LoRa 32 V3.2, NodeID `!849c7328` |
| Firmware estación | Meshtastic oficial `2.7.26.54e0d8d`, entorno `heltec-v3` |
| Radio | ANZ, LONG_FAST, slot 20, frecuencia observada 919,875 MHz |
| Canal | Primario 0, LongFast, clave pública predeterminada |
| Rol | CLIENT_MUTE en ambos equipos; MQTT desactivado |
| Pulsador | Módulo S/G/V: S a AIN1/GPIO 31, G a GND, V libre; probado tras la primera fase sin pulsador |

El RAK se actualizó desde Meshtastic `2.7.15.567b8ea`. El UF2 instalado incorpora `!849c7328` como destino SOS y ocupa 105.268 bytes de RAM y 760.560 bytes de flash. SHA-256: `07badb37bebc827b392aacf737e64bbf382b55c02b4ab0b78b93960974dbe653`.

## Preparación del enlace

El Heltec requirió un reinicio para recuperar la API serie durante el montaje. Antes de las pruebas, se sincronizaron los relojes y se asociaron por USB los contactos con las claves públicas de ambos equipos. Sin esa asociación, el envío directo del RAK fue rechazado con `PKI_SEND_FAIL_PUBLIC_KEY`; ese rechazo ocurre antes de la transmisión.

El sensor respondió localmente por USB con 30,21 °C y 40,52 % de humedad. La publicación automática quedó en 1800 segundos: esta versión aplica ese mínimo en el canal público predeterminado para el rol utilizado. El sondeo de banco se configura por separado, desde el computador, con `--telemetry-poll-seconds 120`.

## Primera prueba de protocolo por radio, sin pulsador

Se inyectó desde USB al RAK el mensaje `CS1|SOS|122f185751c74cacb2a87251`, dirigido al Heltec. El receptor procesó el paquete recibido por radio usando el servicio de almacenamiento y confirmación del proyecto.

| Verificación | Resultado |
|---|---|
| Recepción en Heltec | 22:44:56,672, hora local |
| Persistencia | Alerta guardada en SQLite, base de banco |
| Confirmación | ACK encolado después de guardar, 22:44:56,788 |
| Retorno de radio | El RAK recibió `CS1\|ACK\|122f185751c74cacb2a87251\|REGISTRADO` |
| Origen/destino/canal del ACK | Heltec → RAK, canal 0 |

Esta prueba valida transporte, persistencia y retorno del ACK. El mensaje se generó desde el computador: no valida el GPIO, la pulsación sostenida ni la transición REGISTERED del módulo SOS, que requiere un evento pendiente originado por el botón.

## Telemetría recibida por radio

A las 22:45:07,933 se guardó una respuesta del RAK a una solicitud ambiental enviada por el Heltec. Temperatura: 29,79 °C; humedad relativa: 41,13 %. RSSI reportado: −2 dBm; SNR: 7,25 dB. La base de ensayo es `station-data/banco.sqlite3`.

El servicio continuo utiliza otra base, `station-data/cerroseguro.sqlite3`, para separar el ensayo de protocolo de la recepción posterior. Su primera lectura se guardó a las 22:45:30,088, con temperatura 29,76 °C y hora de captura Unix `1794793528`.

La segunda solicitud se emitió a las 22:47:27,718, 120,185 segundos después de la primera. La respuesta se guardó a las 22:47:29,923 con 29,99 °C, 40,92 % de humedad y hora de captura Unix `1794793648`. El intervalo entre capturas fue de 120 segundos; entre recepciones, 119,835 segundos. Esto verifica dos ciclos del sondeo, sin acreditar todavía una ejecución prolongada ni recepción garantizada de cada solicitud.

## Alcance y pendientes

- Lectura del BME680 por USB y telemetría por radio comprobadas.
- Protocolo de mensaje, persistencia y ACK por radio comprobado; la primera fase no utiliza pulsador y la fase siguiente sí.
- Sondeo de estación configurado a 120 segundos; el intervalo de publicación automática del RAK permanece en 1800 segundos.
- Pendientes: reintentos activados físicamente, latencia de campaña, autonomía y pruebas de alcance.
- El ensayo corresponde a un enlace de banco; los resultados no acreditan cobertura en terreno ni un recorrido mediante repetidores de terceros.

## Pulsador y confirmación en el RAK

El módulo de botón se conectó con S a AIN1/J11 pin 1 y G a GND; V permanece sin conectar. El equipo confirmó que los eventos se generaron al pulsar el botón. En la secuencia de comprobación se indicó un pulso breve, cinco segundos de espera y una pulsación de tres segundos; el equipo informó que realizó la prueba. El monitor registró un solo evento adicional, terminado en `00000002`, y el estado REGISTERED. La duración física exacta de cada pulsación no se midió instrumentalmente.

| Evento | WAITING observado | REGISTERED observado | Diferencia observada |
|---|---|---|---|
| `e11eadd41d07cb0000000002` | 22:52:39,541 | 22:52:42,496 | 2,955 s |
| `e11eadd41d07cb0000000003` | 23:07:17,107 | 23:07:19,690 | 2,583 s |

La primera alerta física, terminada en `00000001`, quedó guardada a las 22:52:07,594 y su ACK fue leído a las 22:52:09,794; el monitor todavía no había capturado su transición WAITING. En total se registraron tres eventos físicos de banco. Para las dos secuencias completas, media observada 2,769 s y máximo 2,955 s. Estas diferencias usan marcas del monitor USB del mismo computador: incluyen su captura y no representan tiempo en aire medido con instrumentación.

Evidencias: [monitor RAK](evidencias/rak-sos-banco.log), [eventos de estación](evidencias/estacion-eventos.log), [serie ambiental](datos/banco-2026-11-15.csv) y [alertas persistidas](datos/sos-banco-2026-11-15.csv). El dashboard muestra [vista general](evidencias/dashboard-vista-general.jpg), [registro SOS](evidencias/dashboard-alertas.jpg) y [adaptación móvil](evidencias/dashboard-movil.jpg).
