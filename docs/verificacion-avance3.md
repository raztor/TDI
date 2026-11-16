# Verificación del Avance 3

**Revisión:** 16 de noviembre de 2026. Referencia: [pauta TEI201](pautas/avance-03-estudiantes.pdf), numeración impresa.

## Resultado actual

El sistema implementa captura ambiental y SOS en RAK4631, transporte Meshtastic, estación Heltec V3.2 por USB, SQLite y dashboard. El equipo confirmó **20/20 mensajes recibidos en menos de 60 s**, sin pérdidas, alimentación correcta, autonomía suficiente y montaje satisfactorio. La fabricación propia utiliza **460 g aproximados de PLA: 160 g del interior y unos 300 g entre aletas y tapa**.

El [cierre funcional](../testing/cierre-funcional-avance3.md) registra el origen y alcance de esos resultados. Las fechas, lugar, participantes y condiciones de los ensayos se completan en las actas; las fotografías finales siguen pendientes.

## Software · 30 %, pp. 2–4

| Criterio | Resultado | Cierre documental restante |
|---|---|---|
| Captura y frecuencia | Sensor reconocido y sondeo solicitado cada 120 s; publicación automática separada de 1800 s | Precisar duración y condiciones de la campaña |
| Persistencia | SQLite conserva histórico y SOS tras reiniciar | Mantener exportaciones y revisión entregada identificables |
| Dashboard | Gráficas, histórico, filtros, CSV, estadísticas, antigüedad, estado USB y revisión de SOS | Incorporar capturas finales para la presentación |
| Calidad | Código modular, instalación documentada y 22 pruebas de estación/dashboard aprobadas | Comprobar instalación desde clonación limpia de la revisión final |

ACK encolado, REGISTERED en el RAK y revisión del operador son estados distintos. Ninguno acredita por sí solo la atención de una emergencia.

## Hardware · 30 %, pp. 4–6

| Entregable | Estado actual | Pendiente |
|---|---|---|
| Esquema | Dos hojas A3 y SVG; terminales y salida cotejados por el equipo | Incorporar fotografías finales y datos de ensayo a las actas |
| Energía | Generación diurna repone consumo nocturno con excedente; consumo y autonomía aceptados | Registrar duración, condiciones y lecturas existentes; no se cuantificó reserva del 30 % |
| BOM | 31 partidas con importes y fuentes; material impreso contado una sola vez | Precios son referencias de reposición, no gastos pagados ni costo importado completo |
| Montaje | Encaje y montaje correctos según el equipo | Fotos de al menos tres ángulos e interior; demostración de reparación |

Panel real: 12 V / 25 W. BMS entre batería y controlador GC para Li-ion 3S, DC-DC USB de 5 V hacia RAK19007. Se conserva la distinción entre modelos físicos y referencias comerciales de precio o CAD.

## Diseño 3D · 20 %, pp. 6–7

Gill V7 dispone de ensamble F3D, STEP, STL y [doce hojas de planos](../diseño-3d/planos/README.md). El equipo confirmó tolerancias suficientes y encaje satisfactorio después de calibrar la impresora. Se actualiza el material fabricado a PLA; el CAD mantiene su geometría.

Quedan la revisión final de renders, la documentación de la parametrización nativa y el cotejo documental de volúmenes comerciales aproximados. No se declaran ensayos de agua, resistencia o comportamiento térmico que no fueron informados.

## Testing · 10 %, pp. 7–8

- Comunicación: 20 enviados y 20 recibidos, 100 % de recepción y 0 % de pérdidas observadas; todos bajo 60 s. Cumple los objetivos de recepción y tiempo en las condiciones ensayadas.
- Energía: suficiencia funcional y recuperación diurna confirmadas. No se informaron mA, Wh, horas exactas ni reserva porcentual.
- Ajuste: montaje y encaje aceptados; impresión propia en PLA y 460 g aproximados reportados.
- Banco documentado: sensor, persistencia y SOS/ACK; dos diferencias WAITING–REGISTERED de 2,955 s y 2,583 s. No se asignan a la campaña de veinte mensajes.
- Falla real: rechazo por contacto público y cadencia diagnosticados, corregidos y comprobados; [registro](../testing/registro-fallas.md).

Faltan las condiciones y fechas de la campaña, latencias individuales si existen, comparación del sensor con referencia, ensayo de reemplazo y validación con usuarios. El resultado 20/20 no se atribuye a múltiples puntos o a toda una ruta sin ese registro.

## Repositorio y presentación · 5 % cada uno

Código, esquema, BOM, CAD, planos, reporte editable y documentación de uso están disponibles. Quedan la revisión final integrada, instalación desde clonación limpia, acceso del evaluador y comprobación de los entregables finales.

La presentación del 23 de noviembre requiere diapositivas, participación de todos, demo real, apertura del encapsulado, gemelo abierto y explicación de resultados. Duración: 8–10 minutos y 3 de preguntas. Completar tres ensayos el 22 de noviembre y registrar responsables.

## Cierre

La implementación y la aceptación funcional de montaje, comunicación y energía están registradas. El cierre de entrega requiere fotografías, actas y condiciones de ensayo, presentación y revisión final del repositorio. El [checklist](checklist-entrega.md) distingue esos pendientes de las funciones ya comprobadas.
