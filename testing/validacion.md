# Validación frente al problema del Avance 1

## Problema y decisión

- Problema y población: [E1 con actas](../docs/avances/E1_Grupo_CerroSeguro_Con_Actas.docx), comunicación de incidentes y monitoreo en cerros de la Región Metropolitana para excursionistas y operadores de puntos fijos.
- Escenario de banco comprobado: pulsador y BME680 del RAK4631, estación Heltec V3.2 por USB, SQLite y dashboard local. La ruta de terreno sigue pendiente.
- Pregunta: qué configuración modular de radio, energía, antena y sensores permite transportar mensajes y telemetría de forma útil y mantenible. Ver también [miniTarea](../docs/avances/miniTarea.docx).
- Decisión: identificar origen y estado de entrega de la alerta y consultar condiciones locales. La recepción no equivale a activar un rescate.
- Criterios preliminares de E1: al menos 9/10 mensajes por punto, entrega objetivo menor a 60 s y reserva energética objetivo del 30 %, entre otros; [detalle y límites](../docs/problema-y-alcance.md). No hay resultados suficientes para comprobarlos.

## Relación entre medición e información

| Necesidad | Variable medida y unidad | Indicador/umbral | Evidencia real | Interpretación | Decisión apoyada | Limitación |
|---|---|---|---|---|---|---|
| Comunicar una alerta | Envíos, recepciones y estados de confirmación | Meta E1: 9/10 por punto y entrega menor a 60 s | A2: capturas SOS/ACK y relato cualitativo | Flujo reportado, desempeño no cuantificado | Saber si se recibió el mensaje | Sin campaña por punto ni receptor operativo definido |
| Consultar condiciones locales | Temperatura °C, humedad % y presión hPa mostradas en A2 | Umbrales y utilidad por definir con usuarios | Capturas ambientales, sin serie original | No permite validar precisión ni tendencias | Interpretar condiciones del punto medido | No representa toda una ruta ni sustituye pronóstico |

## Conclusión

El Avance 3 comprobó en banco el transporte de telemetría real, su histórico y visualización, y la confirmación de SOS hasta REGISTERED en el RAK. El operador dispone de antigüedad del dato, tendencia ambiental y un registro SOS revisable. El [ensayo](banco-rak-heltec.md) documenta dos diferencias observadas de confirmación de 2,955 s y 2,583 s; los [indicadores](../docs/indicadores.md) explican las decisiones y sus límites.

Esto vincula la implementación con comunicación de incidentes y monitoreo local de E1. No acredita aún la meta 9/10 por punto, entrega en montaña menor de 60 s, reserva energética del 30 % ni utilidad demostrada con usuarios. Tampoco valida precisión del sensor mediante comparación con una referencia.

El enlace cualitativo de A2 y las mediciones de antena respaldan el desarrollo técnico. La validación de las metas iniciales requiere campañas de mensajes y energía, junto con entrevistas y observaciones de uso. Sus registros están pendientes de documentación.

Los resultados se limitan a las condiciones de los ensayos documentados. La cobertura en montaña, la autonomía y la fiabilidad operativa requieren validación específica. El prototipo no constituye un servicio de rescate.
