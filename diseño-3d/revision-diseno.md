# Revisión del diseño Gill V7

La revisión entregada es el [Gill V7 con margen de 75 mm](fusion/gill-v7-75mm/README.md). El Gill V1 se conserva como antecedente conceptual. El [inventario CAD](fusion/componentes-nodo/README.md) distingue modelos oficiales, medidas aportadas y referencias aproximadas.

**Aceptación funcional registrada el 16-11-2026:** el equipo confirmó montaje correcto, encaje satisfactorio y tolerancias suficientes después de calibrar la impresora. Fabricación propia en PLA: 160 g aproximados del interior; tapa y aletas exteriores no fabricadas. No se cambian las dimensiones de los STEP ni se asignan desviaciones metrológicas no medidas. Las fotografías del interior están indexadas en [hardware/fotos](../hardware/fotos/README.md); la fecha concreta de fabricación no fue informada. Ver [cierre funcional](../testing/cierre-funcional-avance3.md).

| Componente | Dimensiones o referencia | Evidencia |
|---|---|---|
| Batería | 120 × 50 × 40 mm, de pie | Medición del equipo; sustituye la envolvente comercial anterior |
| Controlador solar | 60 × 60 × 15 mm | Medición y fotografías del equipo |
| RAK19007 / RAK4631 / RAK1906 | CAD oficial, placas conectadas | Fuentes del inventario |
| DC-DC | PCB candidata 63 × 27 mm | Aproximación de XY-3606; modelo exacto por confirmar |
| BMS | Referencia 59 × 20 × 3,4 mm | Modelo físico por confirmar |
| Antena | Referencia mecánica TRAB9023P, montaje N inferior | Espiga, tuerca y conector aproximados; probar con hardware real |

| Parámetro | Valor |
|---|---:|
| Punto superior del interior, incluidas bridas | Z160,5 mm |
| Cara inferior de tapa | Z235,5 mm |
| Margen sobre el interior | 75 mm |
| Diámetro de tapa / aletas / abertura interior | 256 / 236 / 180 mm |
| Aletas | 8 estándar + 1 terminal |
| Pendiente de aletas / tapa | 45° / 8° |
| Paso vertical | 23,5 mm |
| Agujero y espesor de apriete de antena | Ø16,2 × 3 mm |
| Holgura radial del disco desmontable | 0,25 mm |
| Guía acostada | 235,5 mm de largo |

Las comprobaciones de [verificacion.json](fusion/gill-v7-75mm/verificacion.json) revisan las interferencias del marco, aletas, tapa, tornillos y antena, así como el espacio del conector sobre la torre. La interferencia entre los insertos térmicos y sus pilotos es intencional. [stl-verificados.json](fusion/gill-v7-75mm/stl-verificados.json) comprueba mallas cerradas y [archivos-locales.json](fusion/gill-v7-75mm/archivos-locales.json) conserva SHA-256 de los archivos.

El F3D completo y la variante interior se reabren para verificar su contenido y visibilidad. El segundo conserva las nueve aletas ocultas y reactivables. La batería, el controlador y los conectores rectos mantienen su distribución y dimensiones.

**Resultado:** revisión geométrica digital y ajuste funcional del interior impreso. Envolvente exterior sin fabricar; resistencia, sellado y comportamiento térmico sin ensayos documentados. La tapa requiere sellar la junta del disco de antena y los pasos de tornillos. La precisión meteorológica y el rendimiento RF no se deducen del CAD. Los F3D usan geometría directa e híbrida; se conserva OpenSCAD editable y queda pendiente la parametrización nativa completa; los planos PDF están disponibles.

## Estado de fabricación y renders

El **interior se fabricó con aproximadamente 160 g de PLA** y su encaje fue aceptado por el equipo con la impresora calibrada. **La tapa superior y las nueve aletas no se fabricaron**: no fue posible imprimirlas en ASA y se descartó consumir PLA para esa envolvente destinada a exposición solar. El disco de antena pertenece al diseño de tapa; no se contabiliza como material fabricado. Los aproximadamente 300 g antes estimados para la envolvente no son consumo realizado.

El conjunto completo sigue disponible como diseño digital en F3D, STEP, STL y planos. Los renders distinguen el exterior previsto, no fabricado, del interior sin tapa ni aletas. El montaje construido no se declara cerrado, estanco ni protegido para exposición permanente a la intemperie. No se atribuyen ensayos de radiación solar o resistencia ambiental a la decisión de material.
