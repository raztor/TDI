# Arquitectura del sistema

## Elementos conocidos

| Elemento | Función del componente | Decisión de implementación pendiente |
|---|---|---|
| RAK19007 | Base WisBlock: alimentación e interconexión | Montaje, revisión y alimentación efectiva |
| RAK4631 | Núcleo nRF52840 con transceptor SX1262 | Variante de banda, firmware y modo de comunicación |
| RAK1906 / BME680 | Sensado ambiental | Variables usadas, período de captura y procesamiento |

Las capacidades de la hoja de datos no implican que todas estén implementadas. El BME680 no mide CO₂ directamente; cualquier índice derivado requiere especificar algoritmo y condiciones.

## Recorrido de una medición

1. Sensor: variable, unidad, lectura y validación de rango, pendientes.
2. Firmware: muestreo, marca temporal, identificador y gestión de errores, pendientes.
3. Transporte: radio/red, formato de mensajes y recuperación de cortes, pendientes.
4. Persistencia: servicio o archivos, esquema e histórico, pendientes.
5. Procesamiento: indicadores, ventanas y umbrales, pendientes.
6. Dashboard: acceso, actualización y estados de datos, pendientes.
7. Usuario: interpretación y decisión vinculadas al Avance 1, pendientes.

Incorporar un diagrama que identifique nodos, enlaces, dirección del flujo y puntos de almacenamiento cuando se confirme el recorrido real.

## Configuración técnica

| Parámetro | Valor | Justificación |
|---|---|---|
| Intervalo de muestreo | Pendiente | Pendiente |
| Intervalo de transmisión | Pendiente | Pendiente |
| Banda, variante de módulo y antena | Pendiente | Compatibilidad y configuración regional por verificar |
| Protocolo y formato del mensaje | Pendiente | Pendiente |
| Origen del reloj y zona horaria | Pendiente | Pendiente |
| Detección de muestra duplicada | Pendiente | Pendiente |
| Política ante pérdida de conexión | Pendiente | Pendiente |
| Fuente de energía y autonomía | Pendiente de diseño y medición | Pendiente |

## Repositorio de datos

- Tecnología y versión: pendiente.
- Ubicación o endpoint sin secretos: pendiente.
- Esquema, campos, tipos y unidades: pendiente.
- Identificación del nodo y de cada muestra: pendiente.
- Retención, consulta y exportación del histórico: pendiente.
- Integridad ante reinicios, reintentos y duplicados: pendiente.
- Permisos y configuración local necesaria: pendiente.

## Límites y recuperación

Documentar qué datos se pierden o retienen durante una falla, cómo se informa al usuario y cuándo una medición deja de considerarse actual. Verificar con las pruebas T02, T03 y T05 del [protocolo](../testing/protocolo-pruebas.md).
