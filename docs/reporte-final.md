# Cerro Seguro · Reporte del Avance 3

**Curso:** TEI201, Taller de Diseño en Ingeniería. **Entrega:** 23 de noviembre de 2026. **Revisión:** 16 de noviembre de 2026.

## 1. Resumen

Cerro Seguro integra un nodo fijo de telemetría ambiental y SOS con una estación de monitoreo conectada a computador. RAK4631 procesa el sensor RAK1906/BME680 y el pulsador; Meshtastic transporta mensajes hacia Heltec V3.2; la estación guarda datos y eventos en SQLite y el dashboard permite consultar histórico, tendencias y alertas.

El equipo confirmó una campaña de **20/20 mensajes recibidos en menos de 60 s**, sin pérdidas observadas. También confirmó alimentación correcta, autonomía suficiente, recuperación diurna del consumo nocturno y montaje satisfactorio. La fabricación propia se realizó en PLA, con **460 g aproximados utilizados**. Quedan fotografías finales, datos de contexto para las actas, demostración de reparación, comparación del sensor con referencia y validación de uso.

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

La [BOM](../hardware/BOM.xlsx) consolida 31 partidas con referencias de precio. Totales separados: **USD 204,78** y **CLP 106.297**, sin conversión, flete ni tributos de importación. La impresión aporta únicamente **CLP 5.980** de PLA utilizado. [Criterios y fuentes de costo](../hardware/cotizaciones.md).

La energía generada durante el día repone el consumo de la noche y deja excedente. No se interpreta como una carga superior al 100 % de la batería. Las fotos finales desde tres ángulos e interior y la demostración de reemplazo se incorporarán al cierre.

## 7. Diseño 3D y fabricación

[Gill V7](../diseño-3d/fusion/gill-v7-75mm/README.md): base Ø200, aletas Ø236, tapa Ø256 y margen nominal sobre el interior de 75 mm. Incluye ensamble completo e interior, once tipos de pieza, STEP/STL y [doce hojas de planos A3](../diseño-3d/planos/README.md).

El equipo imprimió en PLA y confirmó encaje satisfactorio con la impresora recién calibrada. El consumo aproximado fue 160 g del interior y unos 300 g entre aletas y tapa. Se aceptan las tolerancias funcionales del montaje; no se atribuyen errores dimensionales numéricos sin medirlos. Los volúmenes comerciales aproximados permanecen identificados como referencias.

## 8. Pruebas y resultados

| Ensayo | Resultado | Alcance |
|---|---|---|
| Comunicación reportada | 20 enviados/20 recibidos, 100 % recepción, 0 % pérdidas; todos bajo 60 s | Fecha, lugar, distancias y tiempos individuales por incorporar al acta |
| Banco documentado | Telemetría, persistencia, dashboard y SOS/ACK; diferencias WAITING–REGISTERED 2,955 s y 2,583 s | Son registros separados de la campaña de veinte mensajes |
| Energía | Consumo y autonomía suficientes; generación diurna repone descarga nocturna | Sin valores mA/Wh, duración exacta ni reserva porcentual informados |
| Fabricación | Encaje satisfactorio, montaje correcto y 460 g aproximados de PLA | Fotografías y fecha de fabricación por incorporar |

[Cierre funcional](../testing/cierre-funcional-avance3.md), [resultados](../testing/resultados.md) y [protocolo](../testing/protocolo-pruebas.md). La falla de mensajes directos por contactos públicos se corrigió y verificó; el [registro](../testing/registro-fallas.md) conserva esa evidencia y separa los incidentes históricos de A2.

## 9. Validación del problema

La recepción y el tiempo reportados cumplen las metas iniciales en el escenario probado. El histórico, la antigüedad y la revisión de SOS convierten la captura en información consultable. La cobertura general en montaña, la precisión meteorológica y la utilidad con usuarios necesitan registros específicos. [Validación frente a E1](../testing/validacion.md).

## 10. Limitaciones y mejoras

Completar las condiciones y fechas de las pruebas para delimitar sus conclusiones. Incorporar fotografías, comparación del sensor con un instrumento de referencia y demostración de reparación. Conservar latencias individuales y lecturas energéticas si existen para calcular métricas adicionales. La calibración de la impresora y el buen encaje no prueban por sí solos resistencia a agua, radiación solar ni comportamiento térmico del sensor.

## 11. Conclusiones

El prototipo completa captura, radio, persistencia y visualización, con SOS y confirmación de registro. El equipo aceptó la comunicación 20/20 bajo 60 s, la suficiencia energética y el montaje. La documentación técnica incorpora circuito, costos y planos; la entrega debe cerrarse con evidencias visuales, actas contextualizadas, presentación y revisión del repositorio.

## 12. Referencias y anexos

- [Fuentes del proyecto](../FUENTES.md).
- [Requisitos y evidencias](requisitos.md).
- [Checklist de entrega](checklist-entrega.md).
- [Actas y decisiones](avances/actas-y-decisiones.md).

El reporte se conserva editable. La exportación final para presentación incorporará las fotografías y actas pendientes.
