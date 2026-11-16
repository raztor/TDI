# Revisión del diseño Gill V7

La revisión entregada es el [Gill V7 con margen de 75 mm](fusion/gill-v7-75mm/README.md). El Gill V1 se conserva como antecedente conceptual. El [inventario CAD](fusion/componentes-nodo/README.md) distingue modelos oficiales, medidas aportadas y referencias aproximadas.

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

**Resultado:** revisión geométrica digital; impresión, ajuste, resistencia, sellado y comportamiento térmico pendientes. La tapa requiere sellar la junta del disco de antena y los pasos de tornillos. La precisión meteorológica y el rendimiento RF no se deducen del CAD. Los F3D usan geometría directa e híbrida; se conserva OpenSCAD editable y queda pendiente la parametrización nativa completa y los planos PDF.
