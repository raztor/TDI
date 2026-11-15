# Problema y alcance

## Contexto

**Cerro Seguro** es un proyecto de seguridad y comunicaciones en montaña, con un prototipo de repetidor y telemetría ambiental.

El [Avance 1 con actas](avances/E1_Grupo_CerroSeguro_Con_Actas.docx) define una plataforma modular LoRa para alertas y telemetría en cerros de la Región Metropolitana. El [Avance 2](<avances/Informe Avance 2 - Cerro Seguro (2).pdf>) reporta pruebas con RAK19007, RAK4631 y RAK1906/BME680, y documenta un montaje de prueba con dos LILYGO para bandas distintas.

## Problema del Avance 1

| Campo | Definición |
|---|---|
| Documento o evidencia original | [E1 con actas](avances/E1_Grupo_CerroSeguro_Con_Actas.docx), Introducción, Materiales y métodos y tabla 2 |
| Usuario o grupo afectado | Excursionistas que necesitan comunicar incidentes; administradores, guardaparques y operadores que reciben información y mantienen nodos. Caracterización preliminar |
| Situación, lugar y necesidad | Cerros de la Región Metropolitana: comunicar ubicación y situación ante extravío, lesión o retraso, y disponer de telemetría de puntos fijos. E1 menciona Manquehue, Sierra de Ramón y Cajón del Maipo como contexto, no como rutas ya medidas |
| Evidencia de la necesidad | Revisión documental de fuentes institucionales y técnicas recogida en E1. Registros de entrevistas, observaciones y cobertura por ruta pendientes de documentación |
| Limitaciones de las soluciones actuales | E1 compara dependencia de cobertura celular, compatibilidad e interlocutor en radio portátil, equipo/servicio satelital y mapas sin transmisión. Identifica una brecha de integración modular y mantenimiento |
| Decisión que se busca facilitar | Comunicar y recibir una alerta con estado de entrega, identificar el punto de origen y consultar condiciones locales. Destinatario operativo y protocolo de respuesta pendientes |

## Alcance del prototipo

- Funciones reportadas en A2: enlace físico con LoRa puro; capturas de TX/RX ambiental y secuencia SOS/ACK. Comprobación cualitativa, con firmware y logs pendientes de versionar.
- Variables mostradas en terminal: temperatura, humedad relativa y presión. Su procedencia y continuidad no se pueden verificar con una captura; no hay serie original ni validación del sensor.
- Flujo conceptual: alerta o telemetría → radio → recepción/retransmisión → receptor y registro → interpretación. La retransmisión Meshtastic es un objetivo posterior, no un resultado de A2.
- Lugar y condiciones del ensayo: fotografías de banco e instalación exterior en A2; coordenadas, distancias, configuración y duración no consignadas.
- Diseño propio de PCB: dirección conceptual de E1, postergada para este prototipo. [Evolución y descartes](avances/actas-y-decisiones.md).
- Fuera del alcance demostrado: cobertura entre cerros, enlace Santiago–Valparaíso, red mesh, autonomía, resistencia exterior, persistencia y dashboard. La expansión interregional es una hipótesis de E1.

## Criterios de éxito

La tabla 2 de E1 establece las metas preliminares del proyecto. Sus condiciones y criterios deben confirmarse para la siguiente campaña; su cumplimiento no está demostrado en A2.

| Objetivo | Métrica | Criterio | Justificación | Prueba |
|---|---|---|---|---|
| Entrega de mensajes | Mensajes únicos recibidos/enviados y tiempo de entrega | Al menos 9 de 10 por punto; objetivo menor a 60 s | Meta inicial de E1; no garantiza confiabilidad de emergencia | Registro por punto, mediana, máximo y pérdidas; medición pendiente |
| Retransmisión y trazabilidad | Duplicados, reintentos, saltos y registros | Registrar el 100 % de mensajes recibidos y controlar reenvíos | E1, función central del nodo | Ensayos de pérdida, reenvío y reinicio; pendientes |
| Modularidad | Interfaces y configuración | Sensor y botón por puertos documentados, sin modificar placa base | E1, objetivo de PCB | Revisión y conexión; diseño postergado |
| Autonomía | Consumo y energía útil | Completar el ensayo con reserva objetivo del 30 % | E1; duración y método de reserva por definir | Consumo por estado, frío y ausencia de sol; medición pendiente |
| Telemetría | Unidades, tiempo y errores | Reportar unidad, hora válida o su ausencia y error de lectura | E1 | Comparación con referencia y desconexión; pendientes |
| Alerta comprensible | Estados y activaciones accidentales | Distinguir recibido, pendiente y fallido; objetivo inicial cero activaciones falsas | E1 | Guion de uso; capturas SOS/ACK en A2 no completan la validación |
| Compatibilidad y operación | Configuración, lugar y receptor | Parámetros compatibles, sitio autorizado y responsable de recepción | E1 | Ensayo con nodos, revisión técnica y permisos; pendientes de respaldo |

El plan de E1 propone entrevistar a 8–12 excursionistas y 3–5 rescatistas o guardaparques, y observar dos jornadas en un acceso autorizado. Las entrevistas y jornadas de observación están pendientes de documentación.

El prototipo no debe presentarse como garantía de cobertura, rescate o seguridad personal sin evidencia que sustente esas afirmaciones.
