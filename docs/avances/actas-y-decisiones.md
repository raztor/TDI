# Actas y decisiones de diseño

## Reuniones del Avance 1

Referencia: Anexo A del [documento E1](E1_Grupo_CerroSeguro_Con_Actas.docx). Modalidad: coordinación mediante mensajes y documento compartido.

| Fecha | Participantes | Acuerdos | Tareas |
|---|---|---|---|
| 28 de agosto de 2026 | Benjamín Muñoz, Benjamín Quijada, Exequiel Najle y Javiera Cárdenas | Delimitar el proyecto a cerros de la Región Metropolitana; alertas y telemetría LoRa modular. Entrevistas y cobertura pendientes | Muñoz: fuentes y antecedentes. Quijada: arquitectura y diseño conceptual. Najle: redacción inicial. Cárdenas: instructivo y observaciones |
| 4 de septiembre de 2026 | Los mismos cuatro integrantes | Seleccionar un PCB base modular con radios, gestión energética, sensores y botón. Continuar con selección de componentes y validación | Muñoz: fuentes. Quijada: diseño y criterios técnicos. Najle: resultados, discusión y conclusión. Cárdenas: revisión de contenido y formato |

## Integración electrónica y alternativas descartadas

El diseño inicial contempló una placa común para integrar microcontroladores, transmisores LoRa, gestión de energía, conexiones modulares y BMS. Se buscaba un montaje plug and play que redujera cableado y facilitara la configuración de cada nodo.

Se evaluaron variantes con uno o varios transmisores y controladores y una sola antena compartida mediante conmutación RF. La antena compartida se descartó por la posible pérdida de paquetes durante la conmutación. La alternativa quedó en análisis, sin esquemático ni PCB; no se realizaron ensayos con un conmutador construido.

Las opciones con varios transmisores/controladores y BMS exigían resolver compatibilidad, alimentación y coordinación antes de fabricar. La complejidad de integración y la dificultad de fabricar y verificar el PCB dentro del plazo llevaron a postergarlas. Se continuó con placas comerciales para realizar las pruebas físicas del Avance 2.

| Alternativa | Motivo de selección o descarte | Estado |
|---|---|---|
| Placas comerciales interconectadas | Disponibilidad para pruebas de banco y cambios rápidos | Utilizadas en el prototipo de A2 |
| PCB completamente integrado | Mayor complejidad y tiempo de desarrollo y fabricación | Postergado; sin diseño fabricable |
| PCB base modular | Permite unificar energía y control y cambiar radios o sensores | Dirección conceptual seleccionada en E1; implementación postergada |
| Antena compartida mediante switching RF | Riesgo de pérdida de paquetes durante la conmutación | Descartada durante el análisis |
| Varios transmisores y controladores con energía y BMS en una placa | Esfuerzo de integración y plazo de fabricación | Postergada; topología y componentes sin cerrar |

Las fechas de análisis de estas alternativas están pendientes de registro en las actas de integración.

## Antenas y pruebas

Se construyó un dipolo artesanal de aluminio para 433 MHz y se utilizó una antena Laird en 915 MHz. Ambas se caracterizaron con NanoVNA, junto con las pruebas cualitativas de comunicación LoRa puro descritas en el [informe A2](<Informe Avance 2 - Cerro Seguro (2).pdf>).

Las lecturas fueron SWR 1,301 a 436,100 MHz para el dipolo y SWR 1,475 a 915,000 MHz para la antena comercial; esta última muestra R = 47,02 Ω. El informe registra calibración previa. El procedimiento, los adaptadores y los archivos de barrido están pendientes de documentación. Los resultados y sus límites se detallan en [caracterización de antenas](../../testing/antenas-avance2.md).

## Iteraciones de alimentación y hardware

Durante la integración se sustituyó el Morningstar SunSaver-20 por el controlador blanco/azul tras observar desconexiones prematuras con la batería LiPo 3S. El equipo aceptó posteriormente el montaje actual, con terminales coincidentes con el esquema, salida correcta y energía suficiente. Los valores de ajustes y umbrales no fueron informados; no se atribuyen al equipo los de una ficha de referencia.

También se retiró una batería LiPo hinchada y se registró una placa LILYGO averiada. No se determinó la causa de esos daños ni una causa común entre ambos. Ver [registro de fallas](../../testing/registro-fallas.md).

## Integración del Avance 3

El [cierre de actas de integración](cierre-actas-integracion.md) reúne los acuerdos y resultados confirmados y los datos de fecha, participantes y responsables que faltan para formalizar cada instancia. La aceptación funcional de alimentación, comunicación y encaje se documenta en el [cierre funcional](../../testing/cierre-funcional-avance3.md).
