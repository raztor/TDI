# Lista de materiales y cotizaciones

Revisión del 16-11-2026. [BOM.xlsx](BOM.xlsx) contiene treinta partidas: nodo RAK, energía, estación Heltec, cables, herrajes y los once tipos de pieza del Gill V7. La hoja «Selección técnica» conserva los mismos identificadores y distingue especificaciones nominales de mediciones pendientes. Cada partida cotizada indica su fecha de fuente, 15 o 16 de noviembre.

La fuente tabular de los datos es [bom-materiales.json](bom-materiales.json). Cantidades impresas: veinte piezas; herrajes del CAD: seis M3×6, tres M3×10 y nueve insertos M3 L4 Ø4,2. No se añaden LILYGO históricos, RAK13002, LED, buzzer, varillas largas ni PCB propio. La antena del Heltec está incluida en la referencia de su kit, sin duplicar su precio. El computador y la impresora son equipamiento de trabajo reutilizado, fuera del costo de materiales del prototipo.

## Precios de referencia publicados

| Partida | Unitario | Moneda | Alcance |
|---|---:|---|---|
| RAK19007 | 9,99 | USD | [Modelo exacto](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen?variant=41578719674566) |
| RAK4631 Arduino AU915 | 17,99 | USD | [Modelo exacto](https://store.rakwireless.com/products/rak4631-lpwan-node?variant=37505443922118) |
| RAK1906 | 15,20 | USD | [Modelo exacto](https://store.rakwireless.com/products/rak1906-bme680-environment-sensor?variant=35614169661598) |
| Heltec WiFi LoRa32 V3 | 17,90 | USD | [Familia V3, desde, sin carcasa](https://heltec.org/project/wifi-lora-32-v3/); unidad usada V3.2 |
| Panel 12 V / 25 W | 43,80 | USD | [ACOPOWER de referencia](https://www.acopower.com/products/hy-12p-25w?variant=16354693316674), marca real por cotejar |
| Antena Laird TRAB9023P | 66,95 | USD | [Referencia comercial/mecánica](https://theantennafarm.com/products/laird-te-connectivity-trab9023p-902-928-mhz-phantom-antenna-2-75-in-n-female-termination?variant=52591058485612); variante física por cotejar |
| BMS 3S20A | 2.500 | CLP | [Referencia Afel](https://afel.cl/products/cargador-bms-18650-3s-20a?variant=45125172428952); no identifica la placa encintada |
| DC-DC XY-3606 | 5.500 | CLP | [Referencia RBX](https://rbxelectronics.cl/producto/modulo-reductor-de-voltaje-dc-dc/); cotejar modelo y dimensiones |
| Controlador PWM 3S 10 A | 18,00 | USD | [Catálogo Huine](https://www.huinetech.com/products/0v-start-pwm-solar-panel-charging-controller-10a-fit-3s-lithium-battery), referencia de reposición |
| Batería LiPo 3S 5.200 mAh | 64.990 | CLP | [LipoPlay, 35C y XT60](https://lipoplay.cl/products/bateria-lipo-5200mah-11-1v-3s-35c); referencia comparable, impuesto incluido y envío aparte |

Subtotales de referencia: **USD 189,83** y **CLP 72.990**. Diez de treinta partidas tienen precio. Se mantienen separados; no se aplica una tasa de cambio supuesta. No son el total completo ni precios pagados. Los precios extranjeros excluyen flete y tributos de importación; los locales se conservan como publicados. Las fuentes y variantes están registradas también en cada fila del libro. Las referencias equivalentes no autorizan una sustitución sin verificar tensión, pinout y ajuste.

## Cierre económico pendiente

Veinte partidas no tienen importe verificable: pulsador, latiguillo, dos cables USB, tornillería, insertos, cableado, sellado y las once piezas impresas. No se asignan ceros a esos costos.

Para cerrar el presupuesto se requieren longitudes y terminaciones de cable; tipo de cabeza de tornillo y medidas exactas de inserto; consumo de sellado; y masa/tiempo de laminado de las veinte piezas. El volumen macizo STEP no sustituye el consumo laminado.

La [Multistar de referencia](https://hobbyking.com/multistar-high-capacity-3s-5200mah-multi-rotor-lipo-pack.html) figura discontinuada; su liquidación histórica no se presenta como una cotización vigente. Las cotizaciones se deben actualizar antes de comprar o presentar un total definitivo.

La batería cotizada es LiPo 3S, 11,1 V nominal, 5.200 mAh, 35C y XT60; la ficha declara **136 × 43 × 26 mm**. Solo se usa como referencia económica: la unidad del montaje mantiene la envolvente medida **120 × 50 × 40 mm**. No se cambia el soporte ni se presupone compatibilidad mecánica de un reemplazo.

La captura de compra del controlador en Huine Tech Store, del **24-12-2024**, muestra unitario **$16.214** y total de pedido **$18.024**. Se conservan como antecedente, sin desglosar la diferencia ni sumarlos al precio actual. [Publicación original aportada](https://es.aliexpress.com/item/1005007632831160.html). La referencia actual del catálogo Huine para 3S es la usada en el subtotal.
