# Mapa de conexiones

**Estado:** pulsador, sensor y estación USB verificados en banco. [Esquema editable y PDF](esquematicos/README.md) disponibles. La ruta solar del montaje final está definida por módulos; los terminales ocultos del BMS y las mediciones eléctricas requieren cotejo físico.

## Conexión definida para el botón SOS

Conectar un pulsador normalmente abierto entre AIN1 de J11 pin 1 y GND de la RAK19007. Se puede utilizar GND en J10 pin 2 o J12 pin 2. AIN1 corresponde al pin nRF52840 P0.31 y al número Arduino GPIO 31; se configura como INPUT_PULLUP y la pulsación lleva la entrada a LOW. Los pads permiten soldar directamente dos cables o instalar cabeceras de 2,54 mm, sin expansión adicional.

El RAK1906 ocupa el bus I²C, no AIN1. La medida de batería en el RAK4631 utiliza AIN0/P0.05. Dropzone permanece deshabilitado para que no utilice AIN1. No conectar el pulsador a VBAT, IO1, IO2 ni RESET; tampoco se aplica tensión externa al GPIO. No se instalan LED o buzzer de aplicación. El módulo probado conecta S a AIN1 y G a GND, dejando V libre; el [ensayo](../testing/banco-rak-heltec.md) registra la pulsación y el retorno REGISTERED.

Referencias: [J10/J11/J12 de RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/), [pines utilizados por RAK1906](https://docs.rakwireless.com/product-categories/wisblock/rak1906/datasheet/), [variante RAK4631 y pin de batería en Meshtastic](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/variants/nrf52840/rak4631/variant.h).

## Conexiones observadas en antecedentes

En las [fotografías LILYGO](fotos/README.md) se observan cables USB desde el módulo regulador hacia las placas y conexiones coaxiales hacia las antenas. A2 reporta panel solar, controlador, batería LiPo 3S, BMS y regulación. Quedan por registrar terminales, polaridad, tensiones medidas y circuito completo.

El [PoC](../docs/avances/referencias/poc-nodo-fijo.jpeg) es conceptual. El panel final es **12 V / 25 W**, revisado en etiqueta por el equipo; prevalece sobre los 24 V del PoC. El controlador GC **12 V / 10 A / Li-ion 3S**, la batería medida **120 × 50 × 40 mm** y el convertidor USB **5 V** son los componentes finales confirmados. El RAK se alimenta por USB-C desde el convertidor, con BAT y SOLAR de su base libres.

## Mapa del montaje definido

| Origen | Pin o conector | Destino | Pin o conector | Señal/interfaz | Tensión | Identificación del cable | Observaciones |
|---|---|---|---|---|---|---|---|
| Panel 12 V / 25 W | + / - | GC | PV+ / PV- | Potencia | 12 V nominal; Voc por medir | Identificar en montaje | Modelo y envolvente físicos por cotejar |
| Batería 3S | Potencia y cuatro tomas de celda | BMS encintado | Pads ocultos | Celdas / potencia | 11,1 V nominal | Conector de cuatro hilos fotografiado | Confirmar pinout; no inferir por colores |
| BMS | Puerto protegido funcional P+ / P- | GC | BAT+ / BAT- | Potencia | Bus 3S | Identificar en montaje | Nombres funcionales, no serigrafía confirmada |
| GC | LOAD+ / LOAD- | DC-DC | IN+ / IN- | Potencia | Según salida GC | Identificar polaridad | Verificar parámetros de carga y corte |
| DC-DC | USB-A | RAK19007 | USB-C | Potencia | 5 V regulado | Cable USB | Medir tensión en montaje final |
| Pulsador | S / G | RAK19007 | J11.1 / J12.2 o J10.2 | Digital | Pull-up interno 3,3 V | Dos hilos; V libre | Verificado con SOS físico |
| RAK1906 | Conector WisBlock | RAK19007 | Ranura pequeña trasera | I²C y alimentación | 3,3 V interno | Sin cables externos | Sensor montado y telemetría verificada |
| Computador | USB host | Heltec V3.2 | USB-C | Serial y alimentación | 5 V | Cable de datos | Verificado; estación independiente del nodo |

El BMS es la placa bajo cinta roja entre batería y controlador. Las [fotos](fotos/alimentacion-final/README.md) no permiten identificar modelo ni pads. No se puentean los retornos de celda y puerto protegido. La referencia CAD SGT20A no identifica automáticamente esta placa ni su función de balanceo.

Listado reutilizable: [conexiones.csv](esquematicos/conexiones.csv). El enlace RAK–Heltec es RF; no hay cable GPIO ni antena compartida entre ambas placas.

## Verificación del esquemático

- [ ] Fuente, polaridad, tierra común y protecciones identificadas.
- [ ] Todas las señales coinciden con el pinout oficial de la revisión utilizada.
- [ ] Tensiones y niveles lógicos compatibles.
- [ ] Conectores y cables identificados en el montaje y en el esquema.
- [x] Sensor, botón, radios y ruta de alimentación identificados en la BOM; referencias comerciales señaladas.
- [ ] Continuidad y ausencia de cortocircuitos comprobadas antes de energizar.
- [ ] Esquemático revisado contra el prototipo ensamblado.

Esquemático editable y PDF: [esquematicos/](esquematicos/README.md).
