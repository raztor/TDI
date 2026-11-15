# Mapa de conexiones

**Estado:** pendiente de levantar y contrastar con el montaje real. Esta tabla no constituye un pinout válido para conectar el dispositivo.

## Conexión definida para el botón SOS

Instalar una RAK13002 en la ranura IO de la RAK19007. Conectar un pulsador normalmente abierto entre IO6 y GND de la expansión. IO6 corresponde al pin nRF52840 P0.10 y al número Arduino GPIO 10; se configura como INPUT_PULLUP y la pulsación lleva la entrada a LOW. No se conecta el pulsador a una tensión externa.

IO5 permanece reservado al botón de usuario Meshtastic. No se utiliza RESET como SOS ni se instalan LED o buzzer de aplicación. El pulsador y la expansión están pendientes de montaje; comprobar que no haya otro periférico conectado a IO6.

Referencias de conexión: [GPIO RAK4631](https://meshtastic.org/docs/hardware/devices/rak-wireless/wisblock/core-module/), [pinout RAK13002](https://docs.rakwireless.com/product-categories/wisblock/rak13002/datasheet/). El resto del circuito de alimentación y sus protecciones sigue pendiente de levantamiento.

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
