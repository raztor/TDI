# Caracterización de antenas del Avance 2

Fuente: [informe del 25 de octubre de 2026](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), páginas físicas 9–11, y capturas originales aportadas. La fecha exacta del ensayo no se consigna; la fecha de los nombres de las imágenes no sustituye un registro de laboratorio.

## Lecturas disponibles

| Parámetro | Dipolo artesanal de aluminio para 433 MHz | Antena comercial Laird utilizada en 915 MHz |
|---|---|---|
| Captura | [NanoVNA dipolo](evidencias/nanovna-dipolo-436-100-mhz.jpeg) | [NanoVNA Laird](evidencias/nanovna-laird-915-mhz.jpeg) |
| Marcador M1 | 436,100 MHz | 915,000 MHz |
| SWR en M1 | 1,301 | 1,475 |
| Componente resistiva R en M1 | No mostrada | 47,02 Ω |
| Barrido | 140–455 MHz | 900–950 MHz |
| Puntos | 101 | 101 |
| BW indicado por el instrumento | 1000 Hz | 1000 Hz |
| Calibración | A2 declara calibración previa | A2 declara calibración previa |

El BW mostrado corresponde al instrumento; no es el ancho de banda de modulación LoRa ni un ancho útil de antena medido. No se leen valores adicionales de la curva sin marcadores o exportaciones.

## Trabajo realizado y alcance

El equipo construyó el dipolo para la banda de 433 MHz, utilizó la antena comercial en 915 MHz y caracterizó la respuesta con NanoVNA. El informe incluye fotos de ambas antenas instaladas y reporta comunicación LoRa funcional de manera cualitativa.

Las capturas permiten registrar la adaptación en las frecuencias de los marcadores. No permiten afirmar una ganancia, patrón de radiación, alcance, cobertura de una ruta ni porcentaje de paquetes recibidos. La lectura del dipolo está a 436,100 MHz, no exactamente a 433 MHz. Tampoco el valor resistivo de 47,02 Ω, sin reactancia, constituye una impedancia compleja completa.

## Información que falta recuperar

- Modelo y revisión del NanoVNA; kit, fecha, plano y procedimiento de calibración.
- Modelo exacto de la antena Laird y dimensiones, material y alimentación del dipolo.
- Cable coaxial, longitud, adaptadores y condiciones del montaje durante cada medición.
- Archivos originales de barrido, por ejemplo Touchstone, si se conservaron.
- Lecturas en la frecuencia exacta usada por cada radio y criterio de aceptación previo.
- Configuración y registros del enlace para relacionar la selección de antena con su desempeño.

No se reconstruyen estas condiciones a partir de las fotos. Las pruebas nuevas se registrarán como ejecuciones posteriores, sin cambiar la fecha o el alcance de las capturas existentes.
