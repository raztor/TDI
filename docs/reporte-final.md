# Cerro Seguro · Reporte del Avance 3

**Curso:** TEI201, Taller de Diseño en Ingeniería. **Entrega:** 23 de noviembre de 2026. **Revisión:** 16 de noviembre de 2026.

## 1. Resumen

Cerro Seguro integra un nodo fijo de telemetría ambiental y SOS con una estación de monitoreo conectada a computador. RAK4631 procesa el sensor RAK1906/BME680 y el pulsador; Meshtastic transporta mensajes hacia Heltec V3.2; la estación guarda datos y eventos en SQLite y el dashboard permite consultar histórico, tendencias y alertas.

El equipo confirmó una campaña de **20/20 mensajes recibidos en menos de 60 s**, sin pérdidas observadas. También confirmó alimentación correcta, autonomía suficiente, recuperación diurna del consumo nocturno y montaje satisfactorio. La fabricación propia se realizó en PLA, con **160 g aproximados utilizados en el interior**. La tapa y las aletas exteriores no se fabricaron por indisponibilidad de ASA. Se incorporan renders del diseño y del interior, fotografías del interior y veinte lecturas de distancia/SNR hasta 17,4 km; sus límites se detallan en las pruebas.

## 2. Equipo

Benjamín Muñoz, Benjamín Quijada, Exequiel Najle y Javiera Cárdenas. Las contribuciones históricas se conservan en E1 y el [README](../README.md). Las responsabilidades de integración, ensayos y presentación del Avance 3 deben completarse con los datos de las actas.

## 3. Problema y objetivos

El proyecto aborda comunicación de incidentes y monitoreo local en cerros de la Región Metropolitana, con una plataforma modular y mantenible. La información permite consultar condiciones del punto medido, reconocer datos antiguos y revisar el registro de un SOS. Un ACK de registro no equivale a atención de rescate. [Problema, usuarios y alcance](problema-y-alcance.md).

Las metas de recepción de al menos 9/10 mensajes y entrega menor a 60 s se cumplen en la campaña de veinte envíos reportada. La suficiencia energética se comprobó funcionalmente; no se ha informado una medición de la reserva porcentual objetivo del 30 %. No se generalizan resultados a rutas o condiciones no registradas.

## 4. Arquitectura y ciclo de datos

Captura BME680/pulsador → RAK4631 → Meshtastic → Heltec USB → servicio de estación → SQLite → dashboard → revisión del operador. La estación solicita telemetría cada 120 s; la publicación automática del firmware mantiene su intervalo separado de 1800 s. El navegador actualiza la pantalla cada cinco segundos sin ocupar el puerto USB. [Arquitectura](arquitectura.md) e [indicadores](indicadores.md).

## 5. Software

El [firmware SOS](../firmware/meshtastic/README.md) utiliza AIN1/P0.31 con pull-up interno, rebote de 40 ms y pulsación mantenida de dos segundos. Envía la alerta y reconoce el ACK dirigido de la estación. No requiere RAK13002 ni LED/buzzer externos.

La [estación](../station/README.md) separa recepción, protocolo, almacenamiento y sondeo. El [dashboard](../dashboard/README.md) presenta temperatura/humedad, histórico, estadísticas, antigüedad, estado USB, CSV y revisión/reapertura persistente de alertas. Se aprobaron 22 pruebas automatizadas de estación/dashboard, sintaxis JavaScript y comprobación visual de escritorio y móvil.

## 6. Hardware y costo

RAK19007 + RAK4631 de 915 MHz + RAK1906, pulsador S/G con V libre, panel de 12 V/25 W, controlador GC para Li-ion 3S, BMS externo, batería 3S, DC-DC USB de 5 V y estación Heltec V3.2 por USB. El equipo cotejó terminales con el [esquema](../hardware/esquematicos/README.md) y confirmó la salida y el funcionamiento energético.

La [BOM](../hardware/BOM.xlsx) consolida 31 partidas con referencias de precio. Totales separados: **USD 204,78** y **CLP 102.397**, sin conversión, flete ni tributos de importación. La impresión aporta únicamente **CLP 2.080** de PLA utilizado. [Criterios y fuentes de costo](../hardware/cotizaciones.md).

La energía generada durante el día repone el consumo de la noche y deja excedente. No se interpreta como una carga superior al 100 % de la batería. Las tres fotografías del interior están indexadas en [hardware/fotos](../hardware/fotos/README.md); no representan una carcasa exterior cerrada.

## 7. Diseño 3D y fabricación

[Gill V7](../diseño-3d/fusion/gill-v7-75mm/README.md): base Ø200, aletas Ø236, tapa Ø256 y margen nominal sobre el interior de 75 mm. Incluye ensamble completo e interior, once tipos de pieza, STEP/STL y [doce hojas de planos A3](../diseño-3d/planos/README.md).

El equipo imprimió en PLA y confirmó encaje satisfactorio con la impresora recién calibrada. El consumo aproximado fue 160 g del interior; tapa y aletas exteriores no fabricadas. Se acepta el ajuste funcional del interior. No se fabricó la envolvente exterior por falta de ASA y se descartó imprimirla en PLA para exposición solar. No se atribuyen desviaciones dimensionales numéricas sin medirlas. Los volúmenes comerciales aproximados permanecen identificados como referencias.

## 8. Pruebas y resultados

| Ensayo | Resultado | Alcance |
|---|---|---|
| Comunicación reportada | 20 enviados/20 recibidos, 100 % recepción, 0 % pérdidas; todos bajo 60 s | Fecha, lugar, distancias y tiempos individuales por incorporar al acta |
| Distancia/SNR | 20 lecturas de 0,2–17,4 km; SNR de −9,0 a 13,2 dB | No incluye tiempos ni pérdidas por punto; no identifica saltos de red |
| Banco documentado | Telemetría, persistencia, dashboard y SOS/ACK; diferencias WAITING–REGISTERED 2,955 s y 2,583 s | Son registros separados de la campaña de veinte mensajes |
| Energía | Consumo y autonomía suficientes; generación diurna repone descarga nocturna | Sin valores mA/Wh, duración exacta ni reserva porcentual informados |
| Fabricación | Interior: encaje satisfactorio y 160 g aproximados de PLA | Exterior no fabricado; fotografías del interior indexadas |

[Cierre funcional](../testing/cierre-funcional-avance3.md), [resultados](../testing/resultados.md) y [protocolo](../testing/protocolo-pruebas.md). La falla de mensajes directos por contactos públicos se corrigió y verificó; el [registro](../testing/registro-fallas.md) conserva esa evidencia y separa los incidentes históricos de A2.

## 9. Validación del problema

La recepción y el tiempo reportados cumplen las metas iniciales en el escenario probado. El histórico, la antigüedad y la revisión de SOS convierten la captura en información consultable. La cobertura general en montaña, la precisión meteorológica y la utilidad con usuarios necesitan registros específicos. [Validación frente a E1](../testing/validacion.md).

## 10. Limitaciones y mejoras

Completar las condiciones y fechas de las pruebas para delimitar sus conclusiones. La envolvente exterior no fabricada limita la protección frente a intemperie. No se declaran ensayos de agua, radiación o resistencia. No consta comparación del sensor con un instrumento de referencia ni demostración documentada de reparación. Conservar latencias individuales y lecturas energéticas si existen para calcular métricas adicionales. La calibración de la impresora y el buen encaje no prueban por sí solos resistencia a agua, radiación solar ni comportamiento térmico del sensor.

## 11. Conclusiones

El prototipo completa captura, radio, persistencia y visualización, con SOS y confirmación de registro. El equipo aceptó la comunicación 20/20 bajo 60 s, la suficiencia energética y el montaje. La documentación técnica incorpora circuito, costos y planos; la revisión documental incorpora fotos interiores, renders y datos de distancia/SNR, y conserva explícitos los límites de las evidencias y de la fabricación exterior.

## 12. Referencias y anexos

- [Fuentes del proyecto](../FUENTES.md).
- [Requisitos y evidencias](requisitos.md).
- [Checklist de entrega](checklist-entrega.md).
- [Actas y decisiones](avances/actas-y-decisiones.md).

El reporte se conserva editable, con enlaces a las fotografías interiores, renders, datos originales y actas. Los metadatos no informados permanecen identificados como tales.

## Anexo visual del diseño y del interior

- [Render exterior del diseño completo](../diseño-3d/renders/gill-v7-75mm/gill_v7_exterior_diseno.png): tapa y aletas digitales, no fabricadas.
- [Render del interior sin tapa ni aletas](../diseño-3d/renders/gill-v7-75mm/gill_v7_interior_render.png): geometría STEP de los soportes; electrónica comercial de referencia. No sustituye la fotografía del montaje.
- [Pruebas de distancia, tabla y gráfica](../testing/pruebas-distancia.md): 20 lecturas, incluida la recepción registrada a 17,4 km.
