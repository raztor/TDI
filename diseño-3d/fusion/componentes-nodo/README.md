# Componentes del nodo en Fusion

Proyecto Autodesk: **Cerro Seguro - TDI** → **Componentes del nodo**.

El inventario conserva modelos individuales de placas, energía, antenas y referencias dimensionales. El conjunto RAK19007–RAK4631–RAK1906 representa las placas conectadas por los conectores WisBlock. La distribución final del prototipo corresponde al [Gill V7](../gill-v7-75mm/README.md).

## Procedencia y medidas

| Pieza | Modelo utilizado | Estado |
|---|---|---|
| RAK19007 | STEP oficial RAK, base 60 × 30 mm | Modelo comercial oficial |
| RAK4631 | STEP oficial RAK | Modelo comercial oficial; banda del equipo por verificar |
| RAK1906 / BME680 | STEP oficial RAK, PCB 10 × 10 mm | Modelo comercial oficial |
| Heltec V3 | STEP oficial V3.7 | Revisión concreta del equipo por confirmar |
| Dos LILYGO LoRa32 | STEP oficial candidato T3 V1.6, dos instancias | Revisión real por confirmar; no implica que ambas placas sean la misma variante RF |
| Wireless Tracker | Forma simplificada, 65,48 × 28,06 × 13,52 mm de V1.1 | Referencia dimensional, revisión real por confirmar |
| Controlador solar | Forma de las fotos GC, blanco/azul, **60 × 60 × 15 mm** | Medidas confirmadas por el equipo; etiqueta marcada 12 V, 10 A, Li-ion(3S) |
| Batería actual | Envolvente medida por el equipo, **120 × 50 × 40 mm** | Esta medición sustituye las cotas comerciales anteriores; modelo `04_Bateria_Medida_120x50x40` |
| BMS | SGT 3S 20 A, **59 × 20 × 3,4 mm** | Referencia; modelo real no identificado |
| DC-DC USB | Candidato XY-3606, PCB **63 × 27 mm** | Forma aproximada de la foto; conectores y alturas representativos |
| Caja | **180 × 140 × 50 mm** | Medidas de IMG_2192; paredes, soportes interiores y taladros aproximados |
| Antena Laird 915 | Referencia mecánica TRAB9023P, Ø36,6 × 69,9 mm y espiga inferior N nominal 5/8″ | Montaje actualizado; espiga, tuerca y conector aproximados. Ver [Gill final V7](../gill-v7-75mm/README.md) |
| Dipolo artesanal | Brazo horizontal 300 mm y semibrazo vertical 150 mm | Cotas aportadas en IMG_2193/2194; diámetro y soporte aproximados |
| Panel solar | ACOPOWER HY025-12P, 25 W, **510 × 360 × 20 mm** | Referencia geométrica; no identifica el panel real ni confirma el concepto 24 V del diagrama |
| Botón SOS, LED, buzzer | Formas nominales de presentación | Propuesta conceptual, sin compra o montaje confirmados |
| Gill final | [V7 con componentes y margen de 75 mm](../gill-v7-75mm/README.md) | Diseño digital completo y variante de inspección; interior impreso, exterior no fabricado |

El conjunto RAK y el montaje LILYGO se documentaron por separado en el Avance 2. Su presencia conjunta en este inventario no confirma que se haya construido un único equipo con todas esas radios. El SunSaver-20 fue retirado y no se representa como controlador actual.

La [torre del Gill V7](../gill-v7-75mm/README.md) utiliza la batería medida. El archivo anterior de Multistar se conserva como referencia histórica y no define el asiento actual.

## Fuentes

- [CAD y fichas RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/), [RAK4631](https://docs.rakwireless.com/product-categories/wisblock/rak4631/overview/), [RAK1906](https://docs.rakwireless.com/product-categories/wisblock/rak1906/overview/).
- [STEP oficial Heltec V3](https://resource.heltec.cn/download/WiFi_LoRa_32_V3/3D/) y [documentación Wireless Tracker V1.1](https://resource.heltec.cn/download/Wireless_Tracker/Wireless_Tracker%20_1.1.pdf).
- [Turnigy Multistar 5200mAh 3S 10C, SKU 912700001-0](https://hobbyking.com/multistar-high-capacity-3s-5200mah-multi-rotor-lipo-pack.html).
- [BMS SGT, ficha de referencia](https://www.mantech.co.za/datasheets/products/BMS-20A-3S-S_SGT.pdf).
- [XY-3606, ficha alternativa](https://www.gotronik.pl/przetwornica-napiecia-ladowarka-usb-5v-p-6422.html). Se localizaron candidatos en AliExpress; la política de navegación bloqueó el acceso directo y no se verificó una coincidencia exacta ni se encontró CAD.
- [Catálogo TE/Laird](https://www.te.com/content/dam/te-com/documents/consumer-devices/global/te-connectivity-antenna-catalog.pdf).
- [Panel ACOPOWER HY025-12P](https://www.acopower.com/products/hy-12p-25w).

El detalle de las fuentes y de cada referencia figura en `fuentes-modelos.json`. Las dimensiones sin confirmar necesitan medición antes de fabricar soportes definitivos.

## Bandeja de sensor de referencia

`16_Bandeja_y_sensor_RAK1906` conserva una vista aislada del sensor y su fijación. La bandeja y un retenedor disponen de STL individuales. Son referencias de diseño; el montaje final del sensor y la electrónica se documenta en el Gill V7 y en el esquema eléctrico.

## Archivos locales

Los F3D y STL derivados se encuentran en `modelos/`. `archivos-locales.json` registra tamaños, SHA-256 y la comprobación de integridad de los archivos nativos. Los archivos individuales y los subconjuntos se mantienen disponibles para abrir en Fusion. Los componentes y referencias se presentan por separado; el [Gill V7](../gill-v7-75mm/README.md) es el montaje actual.

## Abrir los modelos

Los F3D individuales están en [modelos/](modelos/). Para inspeccionar el montaje completo, abrir el [Gill V7 con componentes](../gill-v7-75mm/34_Gill_V7_Completo_Margen75.f3d) o su [variante interior](../gill-v7-75mm/36_Gill_V7_Interior_Aletas_Ocultas.f3d). La batería medida y el Gill V7 definen el montaje actual. Los componentes propuestos o de revisión desconocida no se consideran compras ni equipos ensayados.
