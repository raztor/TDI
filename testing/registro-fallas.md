# Registro de fallas y correcciones

**Estado:** tres incidencias históricas documentadas en el [Avance 2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), página física 12. El informe está fechado el 25 de octubre de 2026; no consigna la fecha exacta de cada incidente. La repetición cuantitativa de las pruebas está pendiente de registro.

| ID | Fecha/prueba | Síntoma y evidencia | Impacto | Causa investigada | Corrección y revisión | Resultado de repetir la prueba | Estado |
|---|---|---|---|---|---|---|---|
| A2-F01 | Durante integración de A2; fecha exacta no consignada | SunSaver-20 desconectaba la carga prematuramente con la LiPo 3S; relato y figura 10a | Interrupción de alimentación | A2 atribuye la incompatibilidad al perfil/umbrales del controlador para otra batería; faltan mediciones | Sustitución por controlador blanco/azul descrito para LiPo 3S; figura 10b | El equipo confirmó salida correcta y autonomía suficiente con recuperación diurna; umbrales numéricos no informados |Sustitución aceptada funcionalmente; causas históricas separadas |
| A2-F02 | Durante integración de A2; fecha exacta no consignada | Batería LiPo hinchada según relato | Batería fuera de servicio | No determinada | Retirada de servicio y descartada según A2 | Análisis causal y medición posterior pendientes | Retirada; causa sin determinar |
| A2-F03 | Durante integración de A2; fecha exacta no consignada | Transmisor LILYGO averiado; figura 10c con “Critical fault” | Pérdida de una unidad de radio | No determinada | No se documenta una reparación o sustitución concreta de esa unidad | Prueba posterior pendiente | Avería; resolución sin acreditar |

No se estableció una causa común para la batería y la placa. El análisis de antena compartida descartado por posible pérdida de paquetes pertenece a [decisiones de diseño](../docs/avances/actas-y-decisiones.md), no a fallas experimentales observadas.

Cada corrección se cierra con una repetición de la prueba y su resultado registrado. Las incidencias sin verificación permanecen abiertas.

## Integración del Avance 3 · 15 de noviembre de 2026

| ID | Síntoma y causa comprobada | Corrección | Repetición y resultado |
|---|---|---|---|
| A3-F01 | El USB del Heltec estaba ocupado por la pestaña del navegador conectada a la placa | Desconectar esa sesión antes de abrir la estación | La API serie respondió y el servicio recibió datos; un solo propietario del USB |
| A3-F02 | Mensajes directos rechazados con `PKI_SEND_FAIL_PUBLIC_KEY`: el RAK no conocía la clave pública del Heltec | Asociar los contactos públicos de ambas placas por USB | Mensaje por RF persistido, ACK recibido en el RAK y posteriores SOS físicos REGISTERED; [ensayo](banco-rak-heltec.md) |
| A3-F03 | El intervalo ambiental configurado a 900 s reaparecía como 1800 s; el firmware aplica su mínimo en el canal público predeterminado | Mantener la publicación automática en 1800 s y solicitar lecturas desde la estación a 120 s para banco | Capturas sucesivas separadas por 120 s; sondeo continuo observado en [eventos](evidencias/estacion-eventos.log) |

Estas correcciones corresponden al banco RAK/Heltec. La aceptación posterior del montaje energético se registra en el cierre funcional; no determina la causa de los daños históricos ni cierra pruebas de terreno no documentadas.
