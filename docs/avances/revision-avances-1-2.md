# Revisión de los avances 1 y 2

**Corte documental:** 15 de noviembre de 2026. Se revisaron los README y documentos del repositorio, el Avance 1 con sus actas, el informe del Avance 2, la miniTarea, el ZIP Gill V1 y las nueve imágenes aportadas, de las cuales siete son contenidos únicos. Esta revisión ordena antecedentes y recupera definiciones previas; no inicia la implementación del Avance 3.

El trabajo anterior es mayor que lo que reflejaban los README: hay problema definido, equipo, actas, alternativas, un montaje físico y resultados de antenas. El cierre documental aún es parcial: el enlace está reportado cualitativamente y faltan archivos para reproducirlo. No corresponde describir el proyecto como si nunca hubiera sido probado, ni presentar como validadas funciones que solo están propuestas.

## Qué tenemos

| Tema | Evidencia disponible | Estado |
|---|---|---|
| Problema y usuarios | E1, Introducción y Materiales y métodos | Alertas y monitoreo en cerros de la Región Metropolitana; excursionistas y operadores de puntos fijos. Caracterización preliminar, sin entrevistas acreditadas |
| Equipo | E1 y portada de A2 | Benjamín Muñoz, Benjamín Quijada, Exequiel Najle y Javiera Cárdenas |
| Actas | Anexo A de E1 | 28 de agosto y 4 de septiembre de 2026, con participantes, acuerdos y tareas |
| Alternativas | Tabla 1 de E1 y aclaración del equipo del 15 de noviembre | Placas comerciales, PCB integrado y PCB base modular; análisis de antena compartida, varios radios/controladores y BMS |
| Requisitos iniciales | Tabla 2 de E1 | Metas de entrega, trazabilidad, modularidad, energía, telemetría, interacción y compatibilidad recuperadas en problema y alcance |
| Arquitectura y equipos | A2, pp. físicas 3–6 | RAK19007/RAK4631/RAK1906 reportados como utilizados; montaje fotografiado con dos LILYGO; Heltec disponibles |
| Comunicación | A2, pp. físicas 2, 7, 9 y 13 | Enlace LoRa puro reportado funcional; capturas de TX/RX ambiental y SOS/ACK. Sin código ni logs originales aportados |
| Antenas | A2, pp. físicas 9–11 y dos capturas sueltas | SWR 1,301 a 436,100 MHz y 1,475 a 915,000 MHz; R = 47,02 Ω en la segunda |
| Integración y fallas | A2, p. física 12 | Sustitución del SunSaver-20, batería hinchada retirada y LILYGO averiada; verificación eléctrica final pendiente |
| Encapsulado | A2, p. física 8; paquete Gill V1 | Caja de prueba existente y diseño conceptual del escudo ambiental; fuente OpenSCAD y cinco STL |
| Costos | BOM.xlsx | Solo tres componentes RAK precargados; cantidades, moneda, precios y proveedores vacíos |
| Preparación del Avance 3 | Requisitos, checklist y protocolos del repositorio | Estructura disponible; no acredita ejecución de T01–T08 ni entrega final |

Las páginas del PDF se citan por su posición física: tiene 14 páginas, aunque el pie mantiene “de 13”. No se ha alterado el informe original.

## Definiciones anteriores incorporadas

Se recuperaron el problema, usuarios, objetivos, integrantes, actas, criterios iniciales, separación entre LoRa puro y Meshtastic, inventario histórico, fallas y lecturas de antena. Se incorporaron las fotos, el Word de E1, la miniTarea y el CAD suministrado. Los estados de firmware, hardware, pruebas y diseño enlazan esa evidencia.

El análisis de antena compartida quedó únicamente en estudio: se descartó por el riesgo de pérdida de paquetes durante la conmutación, según aclaración del equipo. No hay un circuito construido ni una pérdida medida que cuantificar. Las variantes de PCB con varios transmisores/controladores, gestión de energía y BMS se postergaron por complejidad, tiempo y dificultad de fabricar y verificar una placa a tiempo. El PCB modular sigue siendo el antecedente conceptual de E1; no se afirma que haya sido fabricado.

## Qué falta para cerrar el pasado

| ID | Pendiente | Evidencia faltante | Acción de cierre |
|---|---|---|---|
| C01 | Pautas originales de E1 y A2 | No están entre los aportes; no es posible certificar cumplimiento académico completo | Incorporar las guías y cotejar sus requisitos |
| C02 | Reproducción del ensayo LoRa | Firmware, versiones, configuración exacta y logs originales | Por indicación del equipo, esta revisión usa solo el informe. Incorporar archivos si se recuperan; no reconstruirlos como originales |
| C03 | Inventario y BOM históricos | Cantidades totales, revisiones, estado operativo, modelos de energía y costos | Completar desde inventario físico y comprobantes; distinguir usados, disponibles, retirados y propuestos |
| C04 | Esquema de alimentación y conexiones | Las fotos y el PoC no acreditan circuito ni ajustes del controlador final | Levantar el montaje real con modelos, tensiones, polaridad, ajustes y protecciones |
| C05 | Trazabilidad de antenas | Modelo exacto Laird, dimensiones del dipolo, calibración detallada, adaptadores y exportaciones | Adjuntar lo conservado; marcar lo no registrado. SWR a 436,100 MHz no acredita el valor a 433 MHz |
| C06 | Registro completo de fallas | Fechas de ensayo, mediciones antes/después y comprobación de la sustitución | Recuperar evidencias sin inventar causas ni dar la reparación por validada |
| C07 | Entrevistas, observaciones, terreno y energía | E1 las propone y A2 deja cobertura y autonomía para después | El equipo incorporará datos posteriormente. Mantener sin acreditar, sin asumir que nunca se hicieron |
| C08 | Actas posteriores y evolución detallada | Solo hay dos actas originales; los descartes adicionales se explicaron el 15 de noviembre | Conservar nota retrospectiva; añadir fechas/responsables solo si se recuperan |
| C09 | Fabricación y ajuste del Gill | El paquete es conceptual y la bandeja no se fija a la base | Posibles registros de impresión por aportar; no acreditar fabricación ni ajuste |

## Inconsistencias detectadas

1. Los README indicaban que faltaba A2 y que no había pruebas o fallas registradas, aunque el PDF ya estaba presente. Se corrigió ese estado y se añadieron enlaces a las fuentes.
2. A2 dice “Resultado correcto” para recepción, latencia y calidad de señal en la tabla 1, pero describe la prueba como cualitativa y deja la cuantificación para después. Se conserva como enlace funcional reportado, sin tasa de entrega, latencia ni alcance demostrados.
3. A2 dice que no consigna valores ambientales en la descripción del sensor, pero la p. 7 contiene valores en capturas de terminal. Se registra su existencia; no se convierten en una serie de datos reales ni en validación del sensor sin procedencia original.
4. El PoC propone Meshtastic, alimentación solar, SOS e indicadores. A2 acredita el ensayo con LoRa puro y deja Meshtastic para después. Los valores del dibujo no se trasladan como especificaciones verificadas del montaje.
5. A2 escribe el tercer integrante de dos formas distintas. Se usa **Exequiel Najle**, como en la portada y E1, por indicación del equipo. No se modificó el PDF.
6. El CAD V1 es OpenSCAD y no un archivo Fusion 360; tampoco representa todos los componentes del nodo. Los modelos Ruuvi y el STEP candidato LILYGO ya existentes son referencias separadas.

## Lo que corresponde al Avance 3

La integración Meshtastic, evaluación de retransmisión, desempeño cuantitativo, consumo y autonomía, validación del ciclo de datos, persistencia, dashboard, gemelo completo, planos, renders y demo siguen como trabajo por ejecutar o acreditar. Los protocolos T01–T08 no se marcan como realizados con antecedentes del Avance 2.

La pauta original del Avance 3 también falta; la fecha, ponderaciones y formato ya transcritos deben cotejarse antes del cierre final.

## Fuentes

- [E1 con actas](E1_Grupo_CerroSeguro_Con_Actas.docx), tablas 1–2 y Anexo A.
- [Informe A2](<Informe Avance 2 - Cerro Seguro (2).pdf>), 25 de octubre de 2026.
- [miniTarea](miniTarea.docx), sin fecha explícita.
- [Inventario de aportes](inventario-aportes.csv), originales y hashes.
- Aclaraciones del equipo del 15 de noviembre: nombre de portada; antena compartida descartada por posible pérdida de paquetes; análisis sin esquemático; uso exclusivo del informe para firmware; datos de usuarios, terreno, energía e impresión por aportar.
