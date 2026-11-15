# Validación frente al problema del Avance 1

## Problema y decisión

- Problema y población: [E1 con actas](../docs/avances/E1_Grupo_CerroSeguro_Con_Actas.docx), comunicación de incidentes y monitoreo en cerros de la Región Metropolitana para excursionistas y operadores de puntos fijos.
- Escenario: persona que requiere comunicar una alerta desde un punto fijo y operador que recibe mensajes y telemetría; receptor y ruta de prueba por confirmar.
- Pregunta: qué configuración modular de radio, energía, antena y sensores permite transportar mensajes y telemetría de forma útil y mantenible. Ver también [miniTarea](../docs/avances/miniTarea.docx).
- Decisión: identificar origen y estado de entrega de la alerta y consultar condiciones locales. La recepción no equivale a activar un rescate.
- Criterios preliminares de E1: al menos 9/10 mensajes por punto, entrega objetivo menor a 60 s y reserva energética objetivo del 30 %, entre otros; [detalle y límites](../docs/problema-y-alcance.md). No hay resultados suficientes para comprobarlos.

## Relación entre medición e información

| Necesidad | Variable medida y unidad | Indicador/umbral | Evidencia real | Interpretación | Decisión apoyada | Limitación |
|---|---|---|---|---|---|---|
| Comunicar una alerta | Envíos, recepciones y estados de confirmación | Meta E1: 9/10 por punto y entrega menor a 60 s | A2: capturas SOS/ACK y relato cualitativo | Flujo reportado, desempeño no cuantificado | Saber si se recibió el mensaje | Sin campaña por punto ni receptor operativo definido |
| Consultar condiciones locales | Temperatura °C, humedad % y presión hPa mostradas en A2 | Umbrales y utilidad por definir con usuarios | Capturas ambientales, sin serie original | No permite validar precisión ni tendencias | Interpretar condiciones del punto medido | No representa toda una ruta ni sustituye pronóstico |

## Conclusión

El enlace cualitativo de A2 y las mediciones de antena son antecedentes técnicos. No cierran los criterios iniciales ni demuestran utilidad con usuarios. Los registros de entrevistas, observaciones, terreno y energía se incorporarán posteriormente según indicó el equipo. Distinguir funcionamiento técnico de utilidad: recibir una lectura no basta para demostrar que resuelve el problema.

Para un sistema orientado a seguridad y comunicaciones en montaña, no afirmar cobertura garantizada, capacidad de rescate, autonomía ni fiabilidad fuera de las condiciones medidas. Señalar el alcance de las pruebas y los datos que todavía faltan.
