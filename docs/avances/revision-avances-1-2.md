# Estado de los avances 1 y 2

**Actualización:** 15 de noviembre de 2026.

Cerro Seguro tiene definidos el problema, los usuarios, los objetivos y una arquitectura modular. El Avance 2 documenta un montaje físico, un enlace LoRa puro funcional, mediciones de antenas y fallas de integración. El desempeño del enlace está descrito cualitativamente; faltan los archivos y registros necesarios para reproducir los ensayos y comprobar las metas iniciales.

## Desarrollo y resultados

| Tema | Referencia | Estado |
|---|---|---|
| Problema y usuarios | E1, Introducción y Materiales y métodos | Alertas y monitoreo en cerros de la Región Metropolitana; excursionistas y operadores de puntos fijos. Validación con usuarios pendiente |
| Equipo | E1 y portada de A2 | Benjamín Muñoz, Benjamín Quijada, Exequiel Najle y Javiera Cárdenas |
| Actas | Anexo A de E1 | Reuniones del 28 de agosto y 4 de septiembre de 2026, con acuerdos y tareas |
| Alternativas | E1, tabla 1; registro de decisiones | Placas comerciales, PCB integrado, PCB base modular y antena compartida mediante conmutación RF |
| Requisitos iniciales | E1, tabla 2 | Metas de entrega, trazabilidad, modularidad, energía, telemetría, interacción y compatibilidad |
| Arquitectura y equipos | A2, páginas 3–6 del archivo | Conjunto RAK utilizado; montaje fotografiado con dos LILYGO; Heltec disponibles |
| Comunicación | A2, páginas 2, 7, 9 y 13 del archivo | Enlace LoRa puro funcional, capturas de TX/RX ambiental y SOS/ACK. Código y logs pendientes de versionar |
| Antenas | A2, páginas 9–11 del archivo | SWR 1,301 a 436,100 MHz y 1,475 a 915,000 MHz; R = 47,02 Ω en la segunda |
| Integración y fallas | A2, página 12 del archivo | Sustitución del SunSaver-20, batería hinchada retirada y LILYGO averiada; verificación eléctrica final pendiente |
| Encapsulado | A2, página 8 del archivo; Gill V1 | Caja de prueba y escudo ambiental conceptual en OpenSCAD con cinco STL |
| Costos | BOM.xlsx | Tres componentes RAK registrados; cantidades, moneda, precios y proveedores pendientes |

## Evolución del diseño

E1 seleccionó un PCB base modular como dirección conceptual. Las variantes con varios transmisores y controladores, gestión de energía y BMS se postergaron por complejidad, tiempo de integración y plazo de fabricación. El prototipo de pruebas se desarrolló con placas comerciales.

La antena compartida mediante conmutación RF se descartó durante el análisis por el riesgo de pérdida de paquetes. La alternativa no pasó a esquemático ni a fabricación. El [registro de decisiones](actas-y-decisiones.md) detalla las opciones y sus motivos de descarte.

## Pendientes de cierre

| ID | Pendiente | Acción |
|---|---|---|
| C01 | Guías de evaluación | Versionar las guías de E1 y A2 y cotejar los entregables |
| C02 | Reproducción del ensayo LoRa | Versionar firmware, dependencias, parámetros de radio y logs. Referencia actual: informe A2 |
| C03 | Inventario y BOM | Completar cantidades, revisiones, modelos de energía, costos y estado operativo; distinguir usados, disponibles y retirados |
| C04 | Alimentación y conexiones | Levantar el esquema del montaje con tensiones, polaridad, ajustes del controlador y protecciones |
| C05 | Caracterización de antenas | Documentar modelo Laird, dimensiones del dipolo, calibración, coaxiales, adaptadores y archivos de barrido |
| C06 | Verificación de fallas y correcciones | Registrar fechas, mediciones antes y después de la sustitución del controlador y estado de los equipos dañados |
| C07 | Usuarios, terreno y energía | Documentar entrevistas, observaciones, pruebas de cobertura y mediciones de consumo y autonomía |
| C08 | Actas posteriores | Completar fechas, participantes, acuerdos y tareas de las decisiones de integración |
| C09 | Fabricación y ajuste del Gill | Medir componentes, resolver la fijación de la bandeja y registrar impresión, montaje y ensayos |

## Límites de los resultados

El enlace de A2 fue una comprobación cualitativa. La tasa de entrega, latencia, RSSI, SNR y alcance requieren mediciones con configuración y condiciones registradas.

Las capturas ambientales muestran temperatura, humedad y presión, pero no constituyen una serie de adquisición con la que evaluar continuidad o precisión. La validación del sensor requiere datos y una referencia de contraste.

Las lecturas NanoVNA caracterizan la adaptación en sus marcadores: 436,100 MHz para el dipolo y 915,000 MHz para la Laird. Faltan la lectura exacta en la frecuencia operativa de cada radio y las pruebas de cobertura.

El PoC y el diagrama de E1 representan la arquitectura prevista. La red Meshtastic, el registro persistente y el dashboard siguen pendientes de integración. El Gill V1 es un escudo conceptual; el gemelo completo del nodo, planos y renders siguen pendientes.

## Continuidad hacia el Avance 3

La siguiente etapa comprende integración Meshtastic, retransmisión, desempeño cuantitativo, consumo y autonomía, ciclo de datos con persistencia y dashboard, gemelo completo y demo. Los protocolos T01–T08 están definidos y pendientes de ejecución. La guía del Avance 3 debe cotejarse con la matriz de requisitos.

## Referencias

- [E1 con actas](E1_Grupo_CerroSeguro_Con_Actas.docx), tablas 1–2 y Anexo A.
- [Informe A2](<Informe Avance 2 - Cerro Seguro (2).pdf>), 25 de octubre de 2026.
- [miniTarea](miniTarea.docx).
- [Actas y decisiones de diseño](actas-y-decisiones.md).
