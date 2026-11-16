# Planos Gill V7

[Gill_V7_Planos.pdf](Gill_V7_Planos.pdf): doce hojas A3, revisión documental B del 16-11-2026, con vistas ortogonales, isométricas de apoyo, cotas generales y funcionales, cantidades, escalas y objetivos de tolerancia. La geometría STEP V7 se conserva.

| Hoja | Pieza | Cantidad | Escala principal |
|---|---|---:|---|
| CS-M-00 | Conjunto y montaje | 1 | 1:2 |
| CS-M-01 | Base inferior Ø200 | 1 | 1:2 |
| CS-M-02 | Guía T de 235,5 mm | 3 | 1:2 |
| CS-M-03 | Aleta estándar Ø236 | 8 | 1:2 |
| CS-M-04 | Aleta terminal Ø236 | 1 | 1:2 |
| CS-M-05 | Tapa superior Ø256 | 1 | 1:2 |
| CS-M-06 | Disco Ø60, paso Ø16,2 | 1 | 1:1 |
| CS-M-07 | Placa vertical | 1 | 1:2 |
| CS-M-08 | Bandeja de controlador | 1 | 1:1 |
| CS-M-09 | Bandeja DC-DC | 1 | 1:1 |
| CS-M-10 | Bandeja RAK | 1 | 1:1 |
| CS-M-11 | Bandeja BMS | 1 | 1:1 |

Son **20 piezas impresas**, once tipos. Los [SVG de cada hoja](svg/) son editables y conservan las dimensiones A3 en milímetros. Las vistas de pieza siguen tercer diedro: planta sobre alzado y perfil derecho a su derecha. Las isométricas se identifican sin escala de fabricación.

## Correspondencia con el diseño

Las líneas visibles y ocultas se obtienen de los [STEP V7](../fusion/gill-v7-75mm/README.md) por proyección HLR de Open CASCADE. Las cotas de envolvente se calculan sobre los sólidos, no sobre las polilíneas de representación. Las curvas se aproximan a una deflexión de 0,035 mm para el dibujo; el STEP conserva la geometría exacta.

[correspondencia-step.json](correspondencia-step.json) identifica archivos, SHA-256, cantidades, envolventes y volúmenes. Las cotas funcionales se contrastan con la [fuente V7](../gill-v7/CerroSeguro_Gill_V7.scad) y la [verificación digital](../fusion/gill-v7-75mm/verificacion.json). La geometría CAD no se modifica al producir los planos.

Objetivos nominales: ±0,3mm en longitudes hasta150mm; ±0,5mm sobre150mm; ±0,2mm en taladros y ±1° en ángulos. El equipo confirmó encaje satisfactorio y tolerancias funcionalmente suficientes con la impresora recientemente calibrada. No se informaron desviaciones dimensionales medidas, por lo que esos valores siguen siendo objetivos de diseño.

Material fabricado: **PLA**, aproximadamente **160 g** del interior; tapa y aletas exteriores no fabricadas. Costo de material único en BOM-031. Fotografías del interior indexadas en hardware/fotos. La fecha de impresión y los ensayos ambientales no fueron informados.

Generación: [herramienta y versiones](../../tools/planos/README.md). Imprimir al 100 %; no medir una copia ajustada al papel.

## Estado de fabricación y renders

Interior fabricado: **160 g de PLA**, con ajuste funcional aceptado. Tapa, aletas y disco exteriores: **diseño no fabricado por indisponibilidad de ASA**; no se imputa consumo de PLA para la envolvente. Los archivos digitales completos se conservan. [Estado de fabricación](../revision-diseno.md) y [renders exterior e interior](../renders/README.md).
