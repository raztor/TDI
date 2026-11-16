# Estado de los avances 1 y 2

**Actualización:**16 de noviembre de2026. Se conserva el alcance histórico de A2 y se distingue de las comprobaciones posteriores de A3.

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
| Integración y fallas | A2, página 12 del archivo | Sustitución del SunSaver-20, batería hinchada retirada y LILYGO averiada; montaje actual aceptado funcionalmente, causas históricas sin determinar |
| Encapsulado | A2, página 8 del archivo; Gill V1 | Caja de prueba y escudo ambiental conceptual en OpenSCAD con cinco STL |
| Costos | BOM.xlsx | A3: 31 partidas con importe y fuentes; PLA 460 g contabilizado una vez |

## Evolución del diseño

E1 seleccionó un PCB base modular como dirección conceptual. Las variantes con varios transmisores y controladores, gestión de energía y BMS se postergaron por complejidad, tiempo de integración y plazo de fabricación. El prototipo de pruebas se desarrolló con placas comerciales.

La antena compartida mediante conmutación RF se descartó durante el análisis por el riesgo de pérdida de paquetes. La alternativa no pasó a esquemático ni a fabricación. El [registro de decisiones](actas-y-decisiones.md) detalla las opciones y sus motivos de descarte.

## Pendientes de cierre

| ID | Pendiente | Acción |
|---|---|---|
| C01 | Guías de evaluación | Versionar las guías de E1 y A2 y cotejar los entregables |
| C02 | Reproducción del ensayo LoRa | Versionar firmware, dependencias, parámetros de radio y logs. Referencia actual: informe A2 |
| C03 | Inventario y BOM | BOM actual completada con 31 partidas; conservar distinción entre modelos físicos y referencias de precio |
| C04 | Alimentación y conexiones | Esquema publicado; terminales, salida y suficiencia energética aceptados por el equipo; lecturas y condiciones para el acta |
| C05 | Caracterización de antenas | Documentar modelo Laird, dimensiones del dipolo, calibración, coaxiales, adaptadores y archivos de barrido |
| C06 | Verificación de fallas y correcciones | Registrar fechas, mediciones antes y después de la sustitución del controlador y estado de los equipos dañados |
| C07 | Usuarios, terreno y energía | Documentar entrevistas, observaciones, pruebas de cobertura y mediciones de consumo y autonomía |
| C08 | Actas posteriores | Completar fechas, participantes, acuerdos y tareas de las decisiones de integración |
| C09 | Fabricación y ajuste del Gill | Impresión PLA 460 g y encaje aceptados; fotos, fecha de fabricación y responsables para el acta |

## Límites de los resultados

El enlace de A2 fue una comprobación cualitativa. La tasa de entrega, latencia, RSSI, SNR y alcance requieren mediciones con configuración y condiciones registradas.

Las capturas ambientales muestran temperatura, humedad y presión, pero no constituyen una serie de adquisición con la que evaluar continuidad o precisión. La validación del sensor requiere datos y una referencia de contraste.

Las lecturas NanoVNA caracterizan la adaptación en sus marcadores: 436,100 MHz para el dipolo y 915,000 MHz para la Laird. Faltan la lectura exacta en la frecuencia operativa de cada radio y las pruebas de cobertura.

El PoC y el diagrama de E1 representan la arquitectura prevista. La red Meshtastic, el registro persistente y el dashboard ya están integrados en A3. Gill V7 dispone de ensamble completo y doce hojas de planos; el equipo aceptó el encaje del montaje impreso en PLA. El [cierre funcional](../../testing/cierre-funcional-avance3.md) incorpora20/20 mensajes bajo 60 s y autonomía suficiente. Fotografías, fechas, condiciones y responsables se completan en las actas.

## Continuidad hacia el Avance 3

A3 implementa mensajería y ACK sobre Meshtastic, persistencia, dashboard y gemelo Gill V7. La fabricación, el encaje, la comunicación20/20 bajo 60 s y la suficiencia energética fueron reportados por el equipo. No se implementa repetidor propio. Quedan fotografías finales, metadatos de ensayo y actas, demostración de reparación, presentación y cierre del repositorio. La [verificación de la pauta](../verificacion-avance3.md) detalla esos estados.

## Referencias

- [E1 con actas](E1_Grupo_CerroSeguro_Con_Actas.docx), tablas 1–2 y Anexo A.
- [Informe A2](<Informe Avance 2 - Cerro Seguro (2).pdf>), 25 de octubre de 2026.
- [miniTarea](miniTarea.docx).
- [Actas y decisiones de diseño](actas-y-decisiones.md).
