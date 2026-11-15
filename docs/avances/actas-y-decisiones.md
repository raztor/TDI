# Actas y evolución de las decisiones

## Actas originales del Avance 1

Fuente: Anexo A del [documento E1](E1_Grupo_CerroSeguro_Con_Actas.docx). Este índice resume las reuniones sin reemplazar los originales.

| Fecha | Participantes | Acuerdos | Tareas registradas |
|---|---|---|---|
| 28 de agosto de 2026 | Benjamín Muñoz, Benjamín Quijada, Exequiel Najle y Javiera Cárdenas | Cerros de la Región Metropolitana; alertas y telemetría LoRa modular. Entrevistas y cobertura pendientes | Muñoz: fuentes y antecedentes. Quijada: arquitectura y diseño conceptual. Najle: redacción inicial. Cárdenas: instructivo y observaciones |
| 4 de septiembre de 2026 | Los mismos cuatro integrantes | PCB base modular con radios, gestión energética, sensores y botón. Selección de componentes y validación como trabajo posterior | Muñoz: fuentes. Quijada: diseño y criterios técnicos. Najle: resultados, discusión y conclusión. Cárdenas: revisión de contenido y formato |

Ambas actas indican coordinación mediante mensajes y documento compartido. No hay otras actas originales entre los archivos aportados.

## Nota retrospectiva del 15 de noviembre de 2026

Esta nota recoge el relato del equipo durante la revisión de antecedentes. La fecha corresponde al registro de la explicación, no a las fechas de los análisis. No se conocen participantes, fechas exactas ni votaciones de esas decisiones adicionales.

Durante el desarrollo analizamos una placa común para integrar microcontroladores, transmisores LoRa y gestión de energía, con conexiones modulares y BMS, buscando un montaje listo para conectar y utilizar. Evaluamos variantes con uno o varios transmisores y controladores, así como compartir una sola antena mediante conmutación RF (switching).

La antena compartida quedó solo en análisis y se descartó por la posible pérdida de paquetes durante la conmutación. Esa preocupación fue un criterio de descarte; no se realizó un ensayo de pérdida de paquetes con un conmutador construido. No se produjo un esquemático ni PCB de esa alternativa.

Las opciones de integración completa y de varios transmisores/controladores con BMS añadían decisiones de compatibilidad, alimentación y coordinación que debían resolverse antes de fabricar. Su complejidad, el tiempo disponible y la dificultad de fabricar y verificar el PCB dentro del plazo llevaron a postergarlas para este prototipo. Se continuó con módulos y placas comerciales para avanzar en las pruebas físicas. Esto explica la transición desde la dirección conceptual elegida en E1 hasta el montaje mostrado en A2.

| Alternativa | Fuente | Decisión o evolución | Límite |
|---|---|---|---|
| Placas comerciales interconectadas | E1, tabla 1; fotos y ensayo A2 | Utilizadas para el prototipo de pruebas | No equivale a una integración final estandarizada |
| PCB completamente integrado | E1, tabla 1; relato del equipo | Postergado por complejidad, tiempo y fabricación | Sin diseño fabricable aportado |
| PCB base modular | E1, tabla 1 y acta del 4 de septiembre | Dirección inicial; implementación postergada para este prototipo | Sin esquemático, Gerbers ni placa fabricada aportados |
| Una antena compartida mediante switching RF | Aclaración del 15 de noviembre | Descartada por posible pérdida de paquetes | Solo análisis; sin resultado experimental |
| Varios transmisores y controladores, energía y BMS en una placa plug and play | Relato del 15 de noviembre | Postergado por integración y plazo de fabricación | Cantidad, topología y componentes sin cerrar |

## Antenas y pruebas realizadas

El [informe A2](<Informe Avance 2 - Cerro Seguro (2).pdf>) documenta un dipolo artesanal de aluminio para 433 MHz y una antena Laird usada en 915 MHz. Se revisó su adaptación con NanoVNA, además de las pruebas cualitativas de comunicación con LoRa puro. Se conservaron las capturas y marcadores en [caracterización de antenas](../../testing/antenas-avance2.md).

El informe declara calibración previa, sin procedimiento ni archivos del instrumento. Las lecturas son SWR 1,301 a 436,100 MHz y SWR 1,475 a 915,000 MHz; la segunda muestra R = 47,02 Ω. Estos resultados no prueban ganancia, cobertura entre cerros ni desempeño del enlace. El valor a 436,100 MHz no se presenta como medición exacta a 433 MHz.

## Iteraciones de integración

A2, fechado el 25 de octubre de 2026, registra el reemplazo del controlador Morningstar SunSaver-20 por el controlador blanco/azul tras desconexiones prematuras con la batería LiPo 3S. También registra una batería hinchada retirada de servicio y una placa LILYGO averiada. La causa de esos dos daños quedó sin determinar. El [registro de fallas](../../testing/registro-fallas.md) separa la sustitución realizada y la verificación pendiente.

Para completar actas posteriores faltan fechas de sesiones, participantes, acuerdos y tareas reales. No se asignan reuniones ni responsables nuevos para llenar esos espacios.
