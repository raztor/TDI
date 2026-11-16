# Lista de materiales y cotizaciones

Revisión del **16-11-2026**. [BOM.xlsx](BOM.xlsx) contiene **31 partidas con importe**, especificación, moneda y fuente. La hoja «Selección técnica» mantiene los mismos identificadores. Los datos editables de referencia están en [bom-materiales.json](bom-materiales.json).

## Presupuesto de referencia

| Moneda | Total |
|---|---:|
| USD | 204,78 |
| CLP | 102.397 |

Las monedas se mantienen separadas; no se aplica un tipo de cambio supuesto. Son referencias de reposición publicadas, no precios pagados. No incluyen flete ni tributos de importación. Los precios locales se conservan como publicados. Las referencias equivalentes no sustituyen los componentes que ya están instalados.

## Referencias completadas

| Partida | Cantidad | Precio de referencia | Fuente y criterio |
|---|---:|---:|---|
| Pulsador | 1 | CLP 4.149 | [KY-004 Electroart](https://www.electroart.cl/2064/boton-pulsador-ky-004/); referencia económica, conserva S/G y V libre del módulo probado |
| Latiguillo U.FL a N macho | 1 | USD 14,95 | [JEFA UFLNM250](https://www.jefatech.com/products/uflnm250), 250 mm de referencia |
| USB-A a USB-C con datos | 2 | CLP 3.990 por unidad | [UGREEN US288-W, 1 m](https://notebookstore.cl/us288-w1m-cable-usb-a-usb-c-blanco-1m); precio sin descuento por transferencia |
| M3×6 | 6 | CLP 25 por unidad | [Global Electrónica, 693006](https://globalelectronica.cl/69-accesorios-para-montaje); referencia publicada sin disponibilidad |
| M3×10 | 3 | CLP 45 por unidad | [Global Electrónica, 693010](https://globalelectronica.cl/69-accesorios-para-montaje); referencia de métrica y longitud |
| Insertos M3 L4 | 9 | CLP 50 por unidad | [Cimech, pack 20 a CLP 1.000](https://www.cimech3d.cl/producto/insertos-metalicos-m3-pack-20-4mm/); prorrateo 1.000/20; catálogo agotado |
| Cableado y terminaciones | 1 lote | CLP 7.269 | 1 m paralelo 18AWG a [CLP 4.200](https://www.litiopack.cl/categoria-producto/componentes-pack-li-ion/cable-siliconado/), tubo 4 mm/10 m a [CLP 2.569](https://altronics.cl/electronics-products/prototipos?limit=100) y dos borneras a [CLP 250](https://afel.cl/collections/conectores) |
| Sellado y fijación | 1 lote | CLP 7.194 | [Silicona neutra 280 ml a CLP 6.990](https://www.easy.cl/silicona-neutra-sella-todo-280-ml-transparente-1310639/p) y [bolsa de 100 amarras a CLP 204](https://requeteofertas.cl/product/bolsa-100-amarras-plasticas-color-negro-tamano-25x100/) |
| PLA utilizado | 0,160 kg | CLP 13.000/kg | [PLA AFEL 1 kg](https://afel.cl/products/filamento-pla-natural-afel-1-75mm-1kg); costo utilizado CLP 2.080 |

Los lotes de cableado y sellado presupuestan los envases o presentaciones indicados. Son una referencia comercial de reposición, no un metraje ni un consumo medido. Cabezas de tornillo, diámetros de inserto, calibres y longitudes de las ofertas no cambian automáticamente el montaje que el equipo ya comprobó.

## Impresión propia

El equipo informó **160 g aproximados de PLA utilizados en el interior; tapa y aletas no fabricadas**. El costo es **0,160 × 13.000 = CLP 2.080**. Se registra una sola vez en **BOM-031**. Las cantidades del inventario CAD se conservan como referencia del diseño completo. Base, guías, placa y bandejas corresponden al interior fabricado y comparten BOM-031. Aletas, tapa y disco de antena son diseño exterior no fabricado y no tienen filamento imputado. La BOM distingue estos estados en cada partida. El presupuesto conserva referencias de herrajes del diseño; no equivale a una rendición de compras ni a una lista de todo lo instalado.

Solo se contabiliza el filamento utilizado; no se suma servicio de impresión, mano de obra ni energía. La marca/color de la oferta es una referencia económica y no identifica el carrete usado.

## Componentes principales

Se mantienen RAK19007 USD 9,99, RAK4631 USD 17,99, RAK1906 USD 15,20, Heltec V3 USD 17,90, panel de referencia USD 43,80, Laird de referencia USD 66,95, BMS de referencia CLP 2.500 y DC-DC de referencia CLP 5.500. Las fuentes, variantes y fechas del 15–16 de noviembre están en cada fila de la BOM.

Batería comparable [LiPo 3S 5.200 mAh, 35C XT60](https://lipoplay.cl/products/bateria-lipo-5200mah-11-1v-3s-35c): **CLP 64.990**, impuesto incluido, envío aparte. Sus 136 × 43 × 26 mm no sustituyen la envolvente medida de la batería del proyecto, **120 × 50 × 40 mm**.

Controlador [Huine PWM 10 A para 3S](https://www.huinetech.com/products/0v-start-pwm-solar-panel-charging-controller-10a-fit-3s-lithium-battery): **USD 18** de catálogo. La [publicación original](https://es.aliexpress.com/item/1005007632831160.html) y la captura de compra del 24-12-2024 se conservan como antecedente: unitario $16.214, total de pedido $18.024. Esos importes históricos no se suman al costo actual.
