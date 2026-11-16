# Datos de prueba

Esta carpeta reúne las series de medición y exportaciones del almacenamiento persistente. La campaña de banco RAK/Heltec del 15 de noviembre incluye [lecturas ambientales](banco-2026-11-15.csv) y [alertas SOS](sos-banco-2026-11-15.csv). Los [logs](../evidencias/README.md) y el [informe del ensayo](../banco-rak-heltec.md) permiten relacionar los registros con la configuración y sus límites.

El CSV ambiental conserva hora UTC de recepción, época de captura, temperatura °C, humedad % HR, RSSI dBm y SNR dB. El CSV SOS conserva eventos únicos, recepciones y encolado de ACK. Son muestras reales de banco; no son una campaña de cobertura, precisión o autonomía. Los datos activos permanecen en SQLite, fuera del versionado; estos CSV son un corte de evidencia del ensayo.

[mediciones.csv](mediciones.csv) contiene solo encabezados para un registro de formato largo: una variable por fila. Adaptar o documentar el esquema real antes de la campaña y conservar los datos originales sin sobrescribirlos.

| Campo | Significado |
|---|---|
| prueba_id | Identificador de protocolo, por ejemplo T01 |
| dispositivo_id | Identificador estable del nodo |
| timestamp_captura | Fecha y hora ISO 8601 con zona horaria |
| timestamp_recepcion | Fecha y hora ISO 8601 con zona horaria |
| variable | Magnitud medida |
| valor | Valor numérico, punto decimal |
| unidad | Unidad de la magnitud |
| estado | Válida, inválida u otro estado definido en el proyecto |
| referencia | Valor del instrumento de contraste, cuando exista |
| observacion | Evento o condición relevante |

## Trazabilidad

Nombrar las campañas con fecha e identificador de prueba. Adjuntar sensor, configuración, intervalo, condiciones, revisión de firmware y responsable. Documentar huecos, reinicios y cualquier limpieza o transformación.

Separar mediciones originales, datos procesados y valores controlados para pruebas de cálculo. No compartir credenciales, ubicaciones privadas ni información personal innecesaria.
