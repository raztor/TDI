# Resultados de pruebas

**Estado:** resultados de A2 documentados; protocolos T01–T08 pendientes de ejecución.

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
| T01 a T08 | Pendiente | Pendiente | Pendiente | Pendiente | Sin medir | No ejecutada | Pendiente |

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

- Resultados que cumplieron el criterio: pendiente.
- Resultados que no cumplieron y posible causa: pendiente.
- Limitaciones del tamaño de muestra, ambiente, referencia o montaje: pendiente.
- Fallas y correcciones verificadas: [registro de fallas](registro-fallas.md).
- Mejora propuesta, fundamento y prueba necesaria: pendiente.
- Conexión con el problema original: [validación](validacion.md).
