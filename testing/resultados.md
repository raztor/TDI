# Resultados de pruebas

**Estado:** antecedentes de A2, banco del15-11-2026 y [cierre funcional](cierre-funcional-avance3.md):20/20 mensajes recibidos bajo 60 s, energía suficiente y montaje satisfactorio. Fecha y condiciones de las pruebas reportadas se completarán en las actas.

## Resultados de banco del Avance 3

- Captura ambiental recibida por radio y persistida: [serie CSV](datos/banco-2026-11-15.csv), con UTC, temperatura, humedad y métricas de radio.
- Sondeo de 120 s: los dos primeros tiempos de captura difieren en 120 s; las recepciones difieren en 119,835 s.
- Tres alertas del pulsador guardadas. Dos secuencias completas WAITING → TX → REGISTERED observadas: 2,955 s y 2,583 s, media 2,769 s. No se equiparan a latencia de radio instrumental ni a una campaña de pérdidas.
- Histórico y alertas conservados al reiniciar el servicio USB con la misma base. Dashboard con gráficas, filtros, CSV y revisión/reapertura verificados con datos reales.
- Fallas de contacto público y cadencia corregidas; [registro](registro-fallas.md). El cierre posterior incorpora autonomía suficiente y20/20 mensajes bajo 60 s reportados por el equipo. No se informó calibración contra referencia ni distribución por punto.

## Resultados documentados del Avance 2

Fuente: [informe A2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), 25 de octubre de 2026. Esta fecha corresponde al informe; no se conoce la fecha exacta de cada ensayo.

| ID histórico | Resultado disponible | Alcance y faltante |
|---|---|---|
| A2-R01 | Enlace LoRa puro reportado funcional | Comprobación cualitativa. Número total de envíos, configuración completa, RSSI, SNR, latencia y pérdida pendientes de registro |
| A2-R02 | Capturas de TX/RX ambiental y SOS/ACK, p. física 7 | Muestran el flujo presentado; sin código o logs originales no se acredita continuidad, persistencia ni fiabilidad |
| A2-R03 | Dipolo: SWR 1,301 a 436,100 MHz | [Captura y condiciones conocidas](antenas-avance2.md); no es un valor exacto a 433 MHz ni una prueba de alcance |
| A2-R04 | Laird: SWR 1,475 y R = 47,02 Ω a 915,000 MHz | [Captura y condiciones conocidas](antenas-avance2.md); no prueba ganancia ni cobertura |

La comprobación del enlace en A2 es cualitativa. La cuantificación del desempeño requiere logs de envíos y recepciones, configuración registrada y relojes sincronizados. Las capturas ambientales muestran ejemplos del flujo; la serie de adquisición está pendiente de versionar.

## Resumen por prueba

| Prueba | Fecha | Revisión | Muestras/duración | Criterio de aceptación | Resultado medido | Estado | Evidencia |
|---|---|---|---|---|---|---|---|
| Comunicación | Fecha por completar; registro16-11-2026 | Montaje final RAK/Heltec | 20 enviados/20 recibidos |>=9/10 y<60s |100 % recepción, 0 pérdidas, todos <60 s |Cumple en condiciones reportadas |[Cierre funcional](cierre-funcional-avance3.md) |
| Energía | Fecha y duración por completar | Solar 12 V/25 W y batería 3S | Ciclo día/noche |Sostener operación y recuperar consumo nocturno |Autonomía suficiente; generación diurna repone consumo con excedente |Aceptado funcionalmente |[Cierre funcional](cierre-funcional-avance3.md) |
| Encaje | Fecha de impresión por completar |Gill V7 en PLA |460 g aproximados, interior 160 g + aletas y tapa unos 300 g |Encaje correcto del montaje |Tolerancias suficientes e impresora calibrada |Aceptado funcionalmente |[Cierre funcional](cierre-funcional-avance3.md) |

## Métricas

Usar unidades, tamaño de muestra y ventana temporal en cada resultado. No combinar variables con unidades diferentes.

- **Latencia:** hora de visualización menos hora de captura, con relojes sincronizados. Informar media, máximo y percentil 95; documentar el método de cálculo.
- **Tasa de pérdida:** muestras esperadas no recibidas / muestras esperadas × 100. Explicar cómo se calcula el número esperado.
- **Tasa de error:** muestras recibidas inválidas / muestras recibidas × 100. Declarar qué se considera inválido.
- **Error absoluto medio:** promedio de las diferencias absolutas entre sensor y referencia, usando pares de mediciones comparables.
- **Sesgo:** promedio de las diferencias sensor menos referencia.
- **Recuperación:** tiempo desde que vuelve la conexión hasta la siguiente muestra válida y persistida.

Si el denominador es cero o no hay referencia válida, informar «no calculable» y explicar la causa.

## Análisis crítico

- Cumplidos en el ensayo reportado: 20/20 entregas bajo 60 s y montaje satisfactorio; energía suficiente con recuperación diurna.
- No se reportaron fallos en los 20 envíos. No se asignan resultados a pruebas no informadas.
- Alcance: 20 mensajes sin distribución por punto ni serie temporal informada. Faltan fecha, lugar, distancia y condiciones para el acta. No se informó contraste metrológico del sensor.
- Fallas y correcciones verificadas: [registro de fallas](registro-fallas.md).
- Mejora: conservar tiempos por mensaje y energía por ciclo para cuantificar latencia y margen energético sin depender solo de la comprobación funcional.
- Conexión con el problema original: [validación](validacion.md).
