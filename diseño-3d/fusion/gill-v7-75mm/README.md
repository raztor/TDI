# Gill V7: margen de 75 mm

Proyecto Autodesk **Cerro Seguro - TDI → Gill V7 - Margen 75 mm y nueve aletas**. Esta es la versión final de diseño para revisión e impresión de prueba; no acredita validación física.

| Documento | Contenido |
|---|---|
| [34_Gill_V7_Completo_Margen75.f3d](34_Gill_V7_Completo_Margen75.f3d) | Gill completo, antena, electrónica, batería, fijaciones y cableado representativo |
| [36_Gill_V7_Interior_Aletas_Ocultas.f3d](36_Gill_V7_Interior_Aletas_Ocultas.f3d) | Mismo montaje con nueve aletas ocultas; pueden volver a mostrarse desde el navegador de Fusion |
| [33_Torre_V7_Margen75.f3d](33_Torre_V7_Margen75.f3d) | Torre con batería, repisas, componentes y guías acortadas |
| [35_Detalle_V7_Tapa_y_Antena.f3d](35_Detalle_V7_Tapa_y_Antena.f3d) | Tapa inclinada, disco plano y fijaciones de antena |

Los archivos completos son autocontenidos: se reabren sin depender de otros archivos locales. El [inventario CAD](../componentes-nodo/README.md) reúne también las piezas comerciales por separado.

## Alturas y cambio de V6 a V7

| Medida | V6 | V7 |
|---|---:|---:|
| Margen entre punto más alto del interior y cara inferior de tapa | 103,5 mm | **75 mm** |
| Cara inferior de tapa, Z | 264 mm | 235,5 mm |
| Asiento exterior plano de antena, Z | 281 mm | 252,5 mm |
| Longitud de guía acostada | 264 mm | 235,5 mm |
| Aletas | 10 | 9: ocho estándar y una superior |
| Paso vertical entre aletas | 24 mm | 23,5 mm |

La tapa baja **28,5 mm**. El punto más alto del interior, incluidas las bridas del BMS, está en **Z160,5 mm**: 235,5 − 160,5 = **75 mm**. La placa vertical impresa termina en Z158 mm; respecto de ese borde la separación es 77,5 mm. El conector N recto y la curva de coaxial representados ocupan parte del volumen superior; no se interpreta el margen como una cámara vacía después de conectarlos.

Se conserva la batería medida de **120 × 50 × 40 mm**, de pie; las repisas, el controlador orientado hacia fuera, el DC-DC y sus reservas laterales, el RAK y el BMS. Las piezas comerciales no se escalan para encajarlas.

## Aletas y tapa

Las aletas tienen **Ø236 mm**, abertura **Ø180 mm** y pendiente de **45°** entre R90 y R118 mm. El espesor vertical es 2,4 mm, equivalente a unos 1,7 mm normales a la pendiente. Un anillo exterior de 2,4 mm ofrece apoyo sobre la cama.

El paso de 23,5 mm deja **21,1 mm de separación vertical**, unos **14,9 mm normales** a la pendiente, fuera de los tres collares. El perfil inclinado tiene una altura de 30,4 mm, con **6,9 mm de solape vertical proyectado**. El solape no acredita protección frente a lluvia impulsada por viento ni radiación en todos los ángulos.

Las ocho aletas estándar se colocan en Z12, 35,5, 59, 82,5, 106, 129,5, 153 y 176,5 mm. La terminal va en Z200 mm y sus collares terminan en Z235,5 mm, donde apoya la tapa. Los separadores son parte de cada collar y el primer apoyo está integrado en las guías. No hay separadores sueltos ni varillas largas.

La tapa tiene **Ø256 mm** y una pendiente exterior de aproximadamente **8°** hacia el borde. Su fondo es plano para imprimir. El disco de antena es horizontal, **Ø60 × 3 mm**, con agujero **Ø16,2 mm**, rebaje de Ø60,5 mm y acceso interior Ø44 mm para arandela y tuerca.

Los **tres M3×6 cercanos a la antena sujetan el disco** a la tapa mediante insertos. La antena se sujeta con su propia tuerca desde dentro. Los **tres M3×10 exteriores sujetan la tapa a las guías**, sobre asientos horizontales Ø10 mm. Los insertos axiales superiores de las guías ocupan Z233,5–237,5 mm.

La junta disco–tapa y los pasos de tornillos requieren sellador compatible con el material: la holgura de 0,25 mm por lado y las cabezas de los tornillos no forman por sí solas una unión estanca. Mantener la junta propia de la antena y descargar la tensión del latiguillo.

## Inventario digital de piezas

[STL individuales y paquete ZIP](../../stl/gill-v7-75mm/) y [fuente OpenSCAD](../../gill-v7/CerroSeguro_Gill_V7.scad).

| STL | Cantidad |
|---|---:|
| V4_Base_200_Sin_Varillas | 1 |
| V7_Guia_T_235_5_Tope_y_Inserto_Axial | 3 |
| V7_Aleta_236_45gr_Paso23_5 | 8 |
| V7_Aleta_Superior_236_45gr | 1 |
| V7_Tapa_256_Pendiente8gr | 1 |
| V7_Disco_Antena_60_Paso16_2 | 1 |
| V3_Placa_Vertical_154 | 1 |
| V3_Bandeja_Controlador / DCDC / RAK / BMS | 1 de cada una |
| Probetas de agujero de antena, inserto y perfil T | opcionales, antes del conjunto |

Herrajes: **6 M3×6, 3 M3×10 y 9 insertos M3 L4 Ø4,2**, además de la fijación propia de la antena. La probeta corta heredada comprueba el perfil T; no reproduce el inserto axial superior ni el tope nuevo.

Imprimir tapa y disco con fondo plano hacia la cama; guías acostadas y aletas apoyadas en el anillo exterior. La pieza más ancha es la tapa de 256 mm; todas caben individualmente en la H2D. Las pendientes de las aletas son de 45° y los alojamientos T tienen pequeños puentes locales. Revisar el laminado antes de fabricar.

Instalar insertos y probar encajes. Montar torre y guías; apilar las ocho aletas estándar y la terminal. Montar la antena en el disco, sellar su unión a la tapa, conectar coaxial y cerrar con los tres M3×10. Evitar tensión o pinzamiento del cableado.

## Referencia de antena

Modelo mecánico **Laird TRAB9023P**, radomo nominal Ø36,6 × 69,9 mm y montaje inferior N hembra de 5/8″. El agujero Ø16,2 mm incluye holgura respecto de 15,875 mm. La longitud de espiga de 20 mm, tuerca AF24 × 3, arandela Ø30 × 1, junta y envolvente del N macho son representativos; no se obtuvo el plano exacto de la unidad física. Las ranuras de la rosca son visuales, no una rosca para fabricar. Usar la probeta Ø16,0 / 16,2 / 16,4 para confirmar el ajuste.

La variante P requiere plano de masa conductor; la NP está prevista para funcionar sin él. Una tapa plástica no proporciona ese plano. El modelo exacto del equipo y su comportamiento RF deben confirmarse. Fuentes: [producto TE TRAB9023P](https://www.te.com/en/product-TRAB9023P.html), [manual de instalación Elster, página 6, paso 5/8″ y variantes P/NP](https://portal.elstersolutions.com/prod_docs.nsf/d9ec06ac151f043e85257ad4006e79af/597f91ca8b44c62e852579dd0072218a/$FILE/IL42-5101C.pdf).

## Verificación y límites

`verificacion.json` registra cotas e interferencias; `stl-verificados.json`, mallas cerradas; `archivos-locales.json`, tamaños y SHA-256. Se reabren el F3D completo y la variante interior para comprobar que conservan las nueve aletas y su estado de visibilidad. La interferencia de los insertos térmicos con sus pilotos es intencional.

El equipo confirmó impresión propia en PLA (160 g del interior; envolvente exterior no fabricada), calibración reciente de la impresora y encaje satisfactorio. El interior queda aceptado funcionalmente. La envolvente no tiene comprobación de ajuste físico. Fecha y responsables se conservan separados de la fecha de registro; los ensayos de resistencia, agua y comportamiento térmico no fueron informados. [Registro](../../../testing/cierre-funcional-avance3.md). El sensor está próximo a electrónica: no se deduce precisión meteorológica a partir de la carcasa. Criterios generales: [YOUNG, escudo multiplato](https://www.youngusa.com/product/multi-plate-radiation-shield/) y [BARANI, separación y flujo entre aletas](https://www.baranidesign.com/faq-articles/2022/6/6/how-to-design-a-solar-radiation-shield-for-weather-station-temperature-sensors-3cjb7). Estas fuentes no validan las dimensiones particulares del prototipo.

## Estado de fabricación y renders

El **interior se fabricó con aproximadamente 160 g de PLA** y su encaje fue aceptado por el equipo con la impresora calibrada. **La tapa superior y las nueve aletas no se fabricaron**: no fue posible imprimirlas en ASA y se descartó consumir PLA para esa envolvente destinada a exposición solar. El disco de antena pertenece al diseño de tapa; no se contabiliza como material fabricado. Los aproximadamente 300 g antes estimados para la envolvente no son consumo realizado.

El conjunto completo sigue disponible como diseño digital en F3D, STEP, STL y planos. Los renders distinguen el exterior previsto, no fabricado, del interior sin tapa ni aletas. El montaje construido no se declara cerrado, estanco ni protegido para exposición permanente a la intemperie. No se atribuyen ensayos de radiación solar o resistencia ambiental a la decisión de material.
