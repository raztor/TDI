# Mapa de conexiones

**Estado:** pendiente de levantar y contrastar con el montaje real. Esta tabla no constituye un pinout válido para conectar el dispositivo.

## Conexiones observadas en antecedentes

En las [fotografías LILYGO](fotos/README.md) se observan cables USB desde el módulo regulador hacia las placas y conexiones coaxiales hacia las antenas. A2 reporta panel solar, controlador, batería LiPo 3S, BMS y regulación. No se deducen de esas imágenes los terminales, polaridad, tensiones medidas ni el circuito completo.

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
