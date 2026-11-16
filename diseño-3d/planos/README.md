# Planos Gill V7

[Gill_V7_Planos.pdf](Gill_V7_Planos.pdf): doce hojas A3, revisión A del 15-11-2026, con vistas ortogonales, isométricas de apoyo, cotas generales y funcionales, cantidades, escalas y objetivos de tolerancia.

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

Objetivos provisionales: ±0,3 mm en longitudes hasta 150 mm; ±0,5 mm sobre 150 mm; ±0,2 mm en taladros y ±1° en ángulos. **Son criterios propuestos de control de impresión, no tolerancias medidas.** Probar insertos y paso de antena antes del conjunto. La validación física, térmica y frente a agua permanece pendiente.

Generación: [herramienta y versiones](../../tools/planos/README.md). Imprimir al 100 %; no medir una copia ajustada al papel.
