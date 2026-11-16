# Componentes del nodo en Fusion

Proyecto Autodesk: **Cerro Seguro - TDI** → **Componentes del nodo**.

El documento `17_CerroSeguro_Inventario_Completo` presenta el inventario en una disposición abierta de inspección, con los subconjuntos separados para ver cada pieza. No es un circuito eléctrico ni una distribución final de montaje en la caja. El conjunto RAK19007–RAK4631–RAK1906 muestra las placas conectadas por los conectores WisBlock; se mantienen además los modelos individuales.

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
| Gill final | [V7 con componentes y margen de 75 mm](../gill-v7-75mm/README.md) | Montaje actual completo y variante de inspección; prueba física pendiente |
| Gill de referencia histórica | Ensamble V1.2 con RAK1906 | Se conserva en el inventario general como alternativa anterior; no define la carcasa final |

El conjunto RAK y el montaje LILYGO se documentaron por separado en el Avance 2. Su presencia conjunta en este inventario no confirma que se haya construido un único equipo con todas esas radios. El SunSaver-20 fue retirado y no se representa como controlador actual.

El inventario `17_CerroSeguro_Inventario_Completo` y la [torre del Gill V7](../gill-v7-75mm/README.md) utilizan la batería medida. El archivo anterior de Multistar se conserva como referencia histórica y no define el asiento actual.

## Fuentes

- [CAD y fichas RAK19007](https://docs.rakwireless.com/product-categories/wisblock/rak19007/overview/), [RAK4631](https://docs.rakwireless.com/product-categories/wisblock/rak4631/overview/), [RAK1906](https://docs.rakwireless.com/product-categories/wisblock/rak1906/overview/).
- [STEP oficial Heltec V3](https://resource.heltec.cn/download/WiFi_LoRa_32_V3/3D/) y [documentación Wireless Tracker V1.1](https://resource.heltec.cn/download/Wireless_Tracker/Wireless_Tracker%20_1.1.pdf).
- [Turnigy Multistar 5200mAh 3S 10C, SKU 912700001-0](https://hobbyking.com/multistar-high-capacity-3s-5200mah-multi-rotor-lipo-pack.html).
- [BMS SGT, ficha de referencia](https://www.mantech.co.za/datasheets/products/BMS-20A-3S-S_SGT.pdf).
- [XY-3606, ficha alternativa](https://www.gotronik.pl/przetwornica-napiecia-ladowarka-usb-5v-p-6422.html). Se localizaron candidatos en AliExpress; la política de navegación bloqueó el acceso directo y no se verificó una coincidencia exacta ni se encontró CAD.
- [Catálogo TE/Laird](https://www.te.com/content/dam/te-com/documents/consumer-devices/global/te-connectivity-antenna-catalog.pdf).
- [Panel ACOPOWER HY025-12P](https://www.acopower.com/products/hy-12p-25w).

El detalle de las fuentes y de cada referencia figura en `fuentes-modelos.json`. Las dimensiones sin confirmar necesitan medición antes de fabricar soportes definitivos.

## Gill V1.2 y vistas de detalle

`15_Gill_V1_2_con_RAK1906` conserva las lamas, el techo, la base, el puente y el soporte del V1.1. Sustituye la bandeja provisional del PCB de 25 mm por una bandeja para el RAK1906 nominal de 10 mm:

- Separación interior entre guías: 10,6 mm, holgura nominal de 0,3 mm por lado.
- Cuatro apoyos de esquina dejan libre el conector inferior.
- Dos retenedores desmontables sobre los bordes del PCB, sujetos por cuatro tornillos y tuercas M2 representativos.
- Se mantienen las orejas M3 al puente y la salida para el cable.
- El conector y la cinta de extensión WisBlock se representan como referencia. No se diseñó un cableado eléctrico ni una placa de extensión.

`16_Bandeja_y_sensor_RAK1906` permite ver el sensor y su fijación sin las lamas. Se exportaron la bandeja y un retenedor a STL. Las fijaciones nuevas necesitan una impresión de prueba y comprobación con el sensor físico.

El sensor conectado directamente al RAK y el sensor dentro del Gill representan **dos ubicaciones alternativas**. Su aparición en las dos vistas no implica dos sensores en la BOM.

## Archivos locales

Los F3D y STL derivados se encuentran en `modelos/`. `archivos-locales.json` registra tamaños, SHA-256 y la comprobación de integridad de los archivos nativos. `14_Todos_los_STL_originales` reúne las 13 mallas originales visibles en una cuadrícula. Los archivos individuales y los subconjuntos se mantienen disponibles para abrir en Fusion. El inventario general presenta componentes y referencias por separado; el [Gill V7](../gill-v7-75mm/README.md) es el montaje actual.

## Abrir el inventario

Descargar [17_CerroSeguro_Inventario_Completo.f3d](modelos/17_CerroSeguro_Inventario_Completo.f3d) y abrirlo desde Fusion. Los F3D individuales están en [modelos/](modelos/). [Vista general actual](vista_general_final.png). Los archivos de Multistar y Gill V1.1/V1.2 se conservan como antecedentes identificados; la batería medida y el Gill V7 definen el montaje actual. Los componentes propuestos o de revisión desconocida no se consideran compras ni equipos ensayados.
