# Ficha de pruebas documentadas en el Avance 2

Fuente: [Informe Avance 2, 25 de octubre de 2026](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>).
Esta ficha recupera lo documentado; no es un protocolo previo ni una nueva ejecución. La fecha del informe no se atribuye automáticamente a cada ensayo.

## 1. Comunicación LoRa puro

- **Objetivo documentado:** comprobar físicamente el intercambio de mensajes y documentar el montaje.
- **Equipos identificados:** RAK19007, RAK4631 y RAK1906; montaje fotografiado con LILYGO LoRa32 de variantes 433/470 y 868/915 MHz. Esto no implica comunicación entre bandas diferentes.
- **Método que consta:** pruebas físicas con firmware LoRa puro y observación de envío/recepción en terminal serial (páginas 3–7 y 9).
- **Resultado reportado:** enlace funcional de manera cualitativa; la página 7 presenta capturas de mensajes ambientales y SOS/ACK.
- **No registrado con detalle:** fecha, lugar, responsables, distancia, obstáculos, parámetros completos de radio, número de envíos/recepciones y tiempos individuales.
- **Criterio cuantitativo previo:** no consta en A2.
- **Conclusión limitada:** antecedente del flujo de comunicación mostrado. No demuestra por sí solo cobertura, continuidad, precisión ambiental ni persistencia.

## 2. Caracterización de antenas

| Dato del informe | Dipolo artesanal | Antena comercial Laird |
|---|---|---|
| Banda de uso indicada | 433 MHz | 915 MHz |
| Marcador M1 | 436,100 MHz | 915,000 MHz |
| SWR en M1 | 1,301 | 1,475 |
| Componente resistiva en M1 | No mostrada | 47,02 ohm |
| Barrido | 140–455 MHz | 900–950 MHz |
| Puntos | 101 | 101 |
| BW del instrumento | 1000 Hz | 1000 Hz |
| Calibración | El informe declara calibración previa | El informe declara calibración previa |

- **Método que consta:** caracterización con NanoVNA y lectura de los marcadores de las capturas.
- **Evidencias existentes:** [dipolo](evidencias/nanovna-dipolo-436-100-mhz.jpeg) y [Laird](evidencias/nanovna-laird-915-mhz.jpeg).
- **Condiciones no documentadas completamente:** modelo del instrumento, procedimiento/plano de calibración, coaxiales, adaptadores, entorno y archivos originales de barrido.
- **Criterio de aceptación previo:** no consta.
- **Conclusión limitada:** las lecturas describen adaptación en los marcadores. La del dipolo no es una lectura exacta a 433 MHz. No se deducen ganancia, alcance ni cobertura.
- [Detalle de caracterización y faltantes](antenas-avance2.md).

## 3. Integración y fallas

| Observación de A2, página 12 | Acción documentada | Límite |
|---|---|---|
| SunSaver-20 desconectaba prematuramente la carga con LiPo 3S | Sustitución por controlador blanco/azul descrito para LiPo 3S | A2 deja pendiente verificar ajustes y ruta eléctrica |
| Batería LiPo hinchada | Retirada de servicio y descartada | Causa no determinada |
| Placa LILYGO averiada | Daño registrado | Causa no determinada; no se estableció causa común con la batería |

[Registro de fallas y comprobaciones posteriores](registro-fallas.md).

## Uso en la entrega final

Estos antecedentes pueden citarse en el reporte final, conservando la revisión histórica del montaje. El código original del ensayo LoRa puro no está incluido en el PDF.

Las pruebas del montaje final RAK/Heltec con Meshtastic, SQLite y dashboard son evidencia separada:
- [Ensayo de banco](banco-rak-heltec.md).
- [Cierre funcional y resultado reportado de 20/20 mensajes](cierre-funcional-avance3.md).
- [Resultados consolidados](resultados.md).

No completar retrospectivamente distancias, fechas o tiempos que no se registraron. Incorporar los registros originales si se recuperan.

## Preparación de esta ficha

Organización y redacción asistidas por ChatGPT a solicitud del equipo. No se generaron mediciones ni resultados experimentales.
