# Datos de prueba

Esta carpeta reúne las series de medición y exportaciones del almacenamiento persistente. **Las series ambientales y los logs de mensajes están pendientes de versionar.** Las lecturas de antena están en [antenas del Avance 2](../antenas-avance2.md) y las capturas de terminal, en el informe A2.

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
