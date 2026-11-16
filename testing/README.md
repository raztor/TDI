# Pruebas y validación

Hay antecedentes de pruebas en el [Avance 2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>): enlace LoRa puro reportado funcional de forma cualitativa, capturas de terminal, caracterización NanoVNA y fallas de integración. El Avance 3 cuenta con banco RAK/Heltec, persistencia y dashboard verificados, más el [cierre funcional reportado por el equipo](cierre-funcional-avance3.md):20/20 mensajes bajo 60 s, suficiencia energética y encaje satisfactorio. Las fotografías interiores y las veinte lecturas distancia/SNR están incorporadas; las fechas y condiciones no informadas se distinguen de los resultados; no todos los protocolos T01–T08 tienen una ejecución completa documentada.

| Documento | Uso |
|---|---|
| [Protocolo de pruebas](protocolo-pruebas.md) | Objetivos, condiciones, pasos, criterios y evidencia |
| [Resultados](resultados.md) | Métricas cuantitativas, interpretación y limitaciones |
| [Antenas del Avance 2](antenas-avance2.md) | Capturas, lecturas de marcadores y límites de la caracterización |
| [Firmware y estación](firmware-software.md) | Compilación y pruebas de software del módulo SOS y la persistencia |
| [Integración SOS/Meshtastic](sos-meshtastic.md) | Protocolos de integración; resultados actuales en el banco y cierre funcional |
| [Registro de fallas](registro-fallas.md) | Causas, correcciones y repetición de pruebas |
| [Validación](validacion.md) | Relación de los datos con el problema del Avance 1 |
| [Datos](datos/README.md) | Mediciones originales, diccionario y exportaciones |
| [Evidencias](evidencias/README.md) | Capturas, fotografías, logs y trazabilidad |

Definir los criterios de aceptación antes de medir. Vincular cada resultado con la revisión de firmware, configuración, montaje y archivos originales. No reemplazar datos reales por ejemplos ni marcar pruebas aprobadas sin ejecutarlas.

## Pruebas de distancia

[20 lecturas de distancia y SNR](pruebas-distancia.md), con imagen original, CSV y gráfica reproducible. La recepción registrada alcanza 17,4 km; la serie se mantiene separada del ensayo de veinte entregas bajo 60 s.
