# Evidencias

Las capturas NanoVNA documentan la caracterización de las antenas. Las fotos históricas están en [hardware/fotos](../../hardware/fotos/README.md). El [ensayo del Avance 3](../banco-rak-heltec.md) incorpora datos reales, logs de pulsador y estación, y las capturas del dashboard siguientes.

| Archivo | Evidencia del 15 de noviembre de 2026 |
|---|---|
| [Dashboard general](dashboard-vista-general.jpg) | Temperatura, humedad, gráfico histórico, estadísticas y conexión USB con datos reales |
| [Alertas](dashboard-alertas.jpg) | Eventos físicos persistidos, ACK encolado y revisión humana independiente |
| [Vista móvil](dashboard-movil.jpg) | Diseño adaptable con gráfica y unidades legibles |
| [Monitor RAK](rak-sos-banco.log) | WAITING, TX, REGISTERED y recepción del ACK del emisor |
| [Eventos de estación](estacion-eventos.log) | Extracto de solicitudes ambientales, escritura de SOS y encolado de ACK |

Cada archivo debe poder vincularse con una prueba y una revisión del sistema.

| Archivo | Prueba | Fecha | Qué demuestra | Origen o revisión |
|---|---|---|---|---|
| [Dipolo](nanovna-dipolo-436-100-mhz.jpeg) | A2-R03 | Fecha de ensayo no registrada | M1 436,100 MHz; SWR 1,301 | A2, figura 7 |
| [Laird](nanovna-laird-915-mhz.jpeg) | A2-R04 | Fecha de ensayo no registrada | M1 915,000 MHz; SWR 1,475; R 47,02 Ω | A2, figura 9 |

Lecturas y límites en [antenas del Avance 2](../antenas-avance2.md). Los protocolos T01–T08 requieren sus propios registros de ejecución.

Las capturas deben mostrar unidades, intervalo temporal y valores legibles. Conservar logs y datos originales cuando una imagen no permita comprobar el resultado. No subir claves, tokens ni otros secretos visibles en capturas.

## Pruebas a distancia

- [Tabla original de veinte pruebas](pruebas-distancia-snr.png): imagen aportada por el equipo; fecha de ensayo no informada.
- [Gráfica SNR/distancia PNG](distancia-snr-grafica.png) y [SVG editable](distancia-snr-grafica.svg): generadas a partir del [CSV](../datos/distancia-snr.csv), sin suavizar ni eliminar filas.
- [Informe e interpretación](../pruebas-distancia.md): alcance de 0,2–17,4 km observado; sin inferir cobertura garantizada, pérdidas por punto o latencias individuales.
