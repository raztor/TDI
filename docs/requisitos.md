# Requisitos y evidencias del Avance 3

Referencia: guía TEI201 «Avance #3: Prototipo IoT Completo», evaluación del 23 de noviembre de 2026. Las páginas siguientes corresponden a la numeración impresa de la guía.

**Estado general:** E1 define el problema y los requisitos preliminares; A2 documenta el enlace cualitativo, las mediciones de antenas y las fallas de integración. Los requisitos del Avance 3 se siguen en la matriz siguiente. Ver [estado de los avances 1 y 2](avances/revision-avances-1-2.md). La [pauta](pautas/avance-03-estudiantes.pdf) se cotejó en la [verificación del Avance 3](verificacion-avance3.md).

| ID | Dimensión | Requisito | Evidencia o ubicación | Estado | Guía |
|---|---|---|---|---|---|
| S01 | Software, 30 % | Captura continua y frecuencia justificada | [Firmware](../firmware/README.md), [banco](../testing/banco-rak-heltec.md) | Verificado en banco a 120 s; campaña prolongada pendiente | pp. 2–4 |
| S02 | Software | Datos persistentes e histórico consultable | [Arquitectura](arquitectura.md), [dashboard](../dashboard/README.md) | SQLite e histórico verificados tras reiniciar el servicio | pp. 2–4 |
| S03 | Software | Dashboard accesible con gráficas en vivo/histórico | [Dashboard](../dashboard/README.md), [capturas](../testing/evidencias/README.md) | Operativo con datos reales; prueba visual y API aprobadas | pp. 2–4 |
| S04 | Software | Indicadores que apoyen decisiones | [Indicadores](indicadores.md), prueba T04 | Estadísticas, frescura y SOS implementados; validación de uso pendiente | pp. 3–4 |
| S05 | Software | Código modular, comentado y reproducible | [Firmware](../firmware/README.md), [estación](../station/README.md), [dashboard](../dashboard/README.md) | Código modular y pruebas disponibles | p. 4 |
| H01 | Hardware, 30 % | Selección por rango, precisión, consumo y compatibilidad | [Selección](../hardware/seleccion-componentes.md) | Fichas base incorporadas; justificación pendiente | pp. 4–6 |
| H02 | Hardware | Esquemático completo | [Esquemáticos](../hardware/esquematicos/README.md) | Archivos pendientes | pp. 5–6 |
| H03 | Hardware | BOM con cantidad, especificación y costos | [BOM.xlsx](../hardware/BOM.xlsx) | Componentes conocidos; cantidades y precios pendientes | pp. 5–6 |
| H04 | Hardware | Montaje seguro y fotos desde tres ángulos | [Fotografías](../hardware/fotos/README.md) | Dos vistas interiores históricas; vistas y verificación final pendientes | pp. 5–6 |
| H05 | Hardware | Acceso y reparación sin destruir el ensamble | [Reparación](../hardware/reparacion.md), prueba T07 | Por verificar | pp. 5–6 |
| D01 | Diseño 3D, 20 % | Gemelo completo con volúmenes reales | [Revisión del diseño](../diseño-3d/revision-diseno.md) | Parcial: Gill V7 e inventario representativo disponibles; modelos aproximados identificados | pp. 6–7 |
| D02 | Diseño 3D | Archivo paramétrico .f3d/.f3z que abre correctamente | [Fusion](../diseño-3d/fusion/README.md) | F3D completo e interior reabiertos; parametrización nativa pendiente | p. 6 |
| D03 | Diseño 3D | Encapsulado funcional, accesos y tolerancias | [Revisión del diseño](../diseño-3d/revision-diseno.md) | Por verificar | pp. 6–7 |
| D04 | Diseño 3D | Planos PDF con vistas, cotas, tolerancias y escala | [Planos](../diseño-3d/planos/README.md) | Archivos pendientes | p. 7 |
| D05 | Diseño 3D | Renders exterior e interior/explosionado | [Renders](../diseño-3d/renders/README.md) | Vistas exterior e interior disponibles; presentación final por revisar | p. 7 |
| T01 | Testing, 10 % | Objetivo, condiciones, pasos, éxito y evidencia | [Protocolo](../testing/protocolo-pruebas.md) | Base preparada; parámetros por definir | pp. 7–8 |
| T02 | Testing | Resultados cuantitativos y análisis crítico | [Resultados](../testing/resultados.md) | Datos, SOS y latencias de banco; campañas T01–T08 abiertas | p. 8 |
| T03 | Testing | Una falla real y su solución | [Fallas](../testing/registro-fallas.md) | PKI y cadencia diagnosticados, corregidos y verificados en banco | p. 8 |
| T04 | Testing | Validación explícita contra Avance 1 | [Validación](../testing/validacion.md) | Vínculo con E1 documentado; metas de montaña y energía abiertas | p. 8 |
| G01 | GitHub, 5 % | Carpetas y README con proyecto, equipo, instalación y uso | [README](../README.md), [inicio local](../dashboard/README.md) | Instalación y uso documentados; clonación final por comprobar | pp. 8–9 |
| G02 | GitHub | Código, esquemáticos, CAD, documentos y evidencias completos | [Checklist](checklist-entrega.md) | Entregables pendientes | pp. 8–9 |
| G03 | GitHub | Repo cloneable y accesible al evaluador | [Checklist](checklist-entrega.md) | Comprobar revisión final | pp. 8–9, 12 |
| G04 | Habilitante | FUENTES.md completo según las tres categorías de la guía | [FUENTES.md](../FUENTES.md) | Fuentes de componentes; declaración técnica pendiente | pp. 13–15 |
| P01 | Presentación, 5 % | Problema, solución, demo, diseño, resultados y repo | [Guion](presentacion/guion.md) | Base preparada; slides pendientes | pp. 10–11 |
| P02 | Presentación | Demo real, todos participan, 8–10 min + 3 min preguntas | [Demo](presentacion/demo.md) | Por ensayar | pp. 10–13 |
| P03 | Presentación | Tres ensayos el día anterior y URL del repo en slides | [Ensayos](presentacion/ensayos.md) | Pendiente | pp. 12–13 |

Una ubicación preparada no acredita el requisito funcional. Marcar completo solo tras comprobar el archivo final o la evidencia correspondiente.
