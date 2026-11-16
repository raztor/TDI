# Diseño 3D y gemelo del prototipo

**Estado:** [Gill V7](fusion/gill-v7-75mm/README.md), con nueve aletas y [doce hojas de planos](planos/README.md). El equipo confirmó impresión propia en PLA y encaje satisfactorio con la impresora recientemente calibrada: 160 g del interior; tapa y aletas exteriores no fabricadas. El [cierre funcional](../testing/cierre-funcional-avance3.md) distingue esa comprobación de las cotas nominales y de los ensayos ambientales no documentados. Fotografías del interior disponibles en [hardware/fotos](../hardware/fotos/README.md). Gill V1 y diseños anteriores se conservan como antecedentes.

| Entregable | Ubicación | Requisito |
|---|---|---|
| Gill V7 actual | [fusion/gill-v7-75mm/](fusion/gill-v7-75mm/README.md) | Ensamble, STL, fuente y planos; encaje funcional confirmado por el equipo |
| Escudo conceptual Gill V1 | [gill-v1/](gill-v1/README.md) | Fuente y exportaciones disponibles; dimensiones provisionales y anclajes pendientes |
| Ensamble editable | [fusion/](fusion/README.md) | Archivo `.f3d` o `.f3z` que abre correctamente |
| Planos técnicos | [planos/](planos/README.md) | PDF con vistas, cotas funcionales, tolerancias y escala |
| Renders | [renders/](renders/README.md) | Vista exterior y vista interior o explosionada |
| Registro de revisión | [revision-diseno.md](revision-diseno.md) | Dimensiones, ajuste, acceso e interferencias |

El gemelo debe representar el sistema completo, no solo la carcasa. Los sólidos referenciales de MCU, sensores, actuadores, batería y PCB deben tener dimensiones y posiciones representativas de los componentes reales que correspondan al proyecto.

El encapsulado debe alojar y proteger todos los componentes, permitir acceso a puertos y controles y abrirse sin destruir el ensamble.


La envolvente actual es el [Gill V7 con tapa inclinada y nueve aletas](fusion/gill-v7-75mm/README.md): aletas de 45°, tapa de 8° y asiento de antena plano. Mantiene la batería medida, el cableado y los tornillos cortos; el margen sobre el interior es de 75 mm.

## Estado de fabricación y renders

Interior fabricado: **160 g de PLA**, con ajuste funcional aceptado. Tapa, aletas y disco exteriores: **diseño no fabricado por indisponibilidad de ASA**; no se imputa consumo de PLA para la envolvente. Los archivos digitales completos se conservan. [Estado de fabricación](revision-diseno.md) y [renders exterior e interior](renders/README.md).
