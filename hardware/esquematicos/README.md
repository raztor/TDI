# Esquema eléctrico del prototipo

Revisión A, 15-11-2026. Interconexión de módulos: alimentación, polaridades, puertos, sensor, pulsador y estación USB.

| Archivo | Contenido |
|---|---|
| [CerroSeguro_Esquematico.pdf](CerroSeguro_Esquematico.pdf) | Dos hojas A3 para revisión e impresión |
| [01_Alimentacion.svg](svg/01_Alimentacion.svg) | Fuente vectorial editable: alimentación solar, BMS, batería, DC-DC y RAK |
| [02_Sensor_SOS_Estacion.svg](svg/02_Sensor_SOS_Estacion.svg) | Fuente editable: WisBlock, botón, radio y estación Heltec/PC |
| [conexiones.csv](conexiones.csv) | Conexiones externas y condición de verificación |

Los SVG se editan en Inkscape u otro editor vectorial sin bibliotecas de símbolos externas. El PDF conserva las mismas líneas y etiquetas. Generación reproducible: [herramientas y versiones](../../tools/planos/README.md). Es documentación del sistema por módulos; no es un diseño de PCB ni tiene validación ERC de KiCad.

## Alimentación definida

Panel **12 V / 25 W**, controlador GC **12 V / 10 A / Li-ion 3S**, batería medida **120 × 50 × 40 mm**, BMS externo y convertidor USB de **5 V**. Panel a PV del controlador; batería a través del BMS al puerto BAT; LOAD al DC-DC; USB a RAK19007. El Heltec se alimenta por USB desde el computador.

La tensión y potencia del panel están confirmadas por el equipo. La envolvente de 510 × 360 × 20 mm y la cotización ACOPOWER son referencias; fabricante y dimensiones del panel físico requieren cotejo. «12 V nominal» no equivale a su tensión de circuito abierto.

El BMS existe bajo la cinta roja, entre controlador y batería. Las [fotografías](../fotos/alimentacion-final/README.md) muestran el encapsulado y el conector de cuatro hilos; no permiten leer modelo ni serigrafía. `P+`, `P-` y `C0..C3` son nombres funcionales, **no un pinout para soldar**. Cotejar los pads y puertos de carga/descarga antes de rehacer ese cableado. No se deduce balanceo activo por la existencia del conector.

La ruta del montaje final está documentada; faltan mediciones de carga solar, corte del BMS, consumo, salida y autonomía. La alimentación USB de banco, el sensor y SOS/ACK tienen [evidencia funcional](../../testing/banco-rak-heltec.md).

## Señales

Pulsador S → J11.1 AIN1/P0.31; G → J12.2 o J10.2 GND; V libre. Sensor RAK1906 por conector WisBlock e I²C interno. Sin LED, buzzer ni expansión RAK13002.

No aplicar batería 3S a BAT de RAK19007 (1S), ni panel de 12 V a SOLAR de RAK19007 (5 V). Ambos quedan libres. Referencia: [límites y pinout oficiales](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/).

Cantidades: [BOM.xlsx](../BOM.xlsx). Estado y mapa: [conexiones.md](../conexiones.md).
