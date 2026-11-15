# Mapa de conexiones

**Estado:** pendiente de levantar y contrastar con el montaje real. Esta tabla no constituye un pinout válido para conectar el dispositivo.

## Conexión definida para el botón SOS

Conectar un pulsador normalmente abierto entre AIN1 de J11 pin 1 y GND de la RAK19007. Se puede utilizar GND en J10 pin 2 o J12 pin 2. AIN1 corresponde al pin nRF52840 P0.31 y al número Arduino GPIO 31; se configura como INPUT_PULLUP y la pulsación lleva la entrada a LOW. Los pads permiten soldar directamente dos cables o instalar cabeceras de 2,54 mm, sin expansión adicional.

El RAK1906 ocupa el bus I²C, no AIN1. La medida de batería en el RAK4631 utiliza AIN0/P0.05. Dropzone permanece deshabilitado para que no utilice AIN1. No conectar el pulsador a VBAT, IO1, IO2 ni RESET; tampoco se aplica tensión externa al GPIO. No se instalan LED o buzzer de aplicación. El montaje y la verificación física del botón están pendientes.

Referencias: [J10/J11/J12 de RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/), [pines utilizados por RAK1906](https://docs.rakwireless.com/product-categories/wisblock/rak1906/datasheet/), [variante RAK4631 y pin de batería en Meshtastic](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/variants/nrf52840/rak4631/variant.h). El resto del circuito de alimentación y sus protecciones sigue pendiente de levantamiento.

## Conexiones observadas en antecedentes

En las [fotografías LILYGO](fotos/README.md) se observan cables USB desde el módulo regulador hacia las placas y conexiones coaxiales hacia las antenas. A2 reporta panel solar, controlador, batería LiPo 3S, BMS y regulación. Quedan por registrar terminales, polaridad, tensiones medidas y circuito completo.

La entrada usada por RAK y su ruta de regulación no están documentadas. A2 indica que la batería 3S no debe conectarse directamente a las entradas de batería o solar de la base RAK19007. El [PoC](../docs/avances/referencias/poc-nodo-fijo.jpeg) es conceptual y no sustituye el levantamiento eléctrico del montaje.

## Mapa por completar

| Origen | Pin o conector | Destino | Pin o conector | Señal/interfaz | Tensión | Identificación del cable | Observaciones |
|---|---|---|---|---|---|---|---|
| Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

## Verificación del esquemático

- [ ] Fuente, polaridad, tierra común y protecciones identificadas.
- [ ] Todas las señales coinciden con el pinout oficial de la revisión utilizada.
- [ ] Tensiones y niveles lógicos compatibles.
- [ ] Conectores y cables identificados en el montaje y en el esquema.
- [ ] Sensores, actuadores y alimentación coinciden con la BOM.
- [ ] Continuidad y ausencia de cortocircuitos comprobadas antes de energizar.
- [ ] Esquemático revisado contra el prototipo ensamblado.

Esquemático editable y PDF: [esquematicos/](esquematicos/README.md).
