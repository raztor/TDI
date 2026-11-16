# Verificación del Avance 3

**Fecha de revisión:** 16 de noviembre de 2026. Referencia: [pauta TEI201, Avance #3](pautas/avance-03-estudiantes.pdf). Las páginas citadas corresponden a su numeración impresa.

## Resultado de la revisión

El prototipo de banco implementa el ciclo captura → radio → persistencia → dashboard → información para decidir. Se verificaron RAK4631 y RAK1906/BME680, estación Heltec V3.2 por USB, histórico SQLite, sondeo de 120 s y SOS físico con retorno al estado REGISTERED. El dashboard usa esos datos reales y no genera mediciones de demostración.

Esto permite demostrar la dimensión de software en banco; no cierra toda la entrega. La pauta también exige hardware, gemelo completo, planos, testing vinculado al problema, repositorio completo y presentación. El cumplimiento de las metas de E1 en montaña y energía continúa abierto.

## Software · 30 %, pp. 2–4

| Criterio | Resultado verificable | Estado y límite |
|---|---|---|
| Captura continua y frecuencia justificada | Solicitudes cada 120 s, sensor reconocido y lecturas recibidas por RF; [indicadores](indicadores.md) | Verificado en banco; falta campaña prolongada, calibración y autonomía |
| Persistencia e histórico | SQLite conserva lecturas y SOS al reiniciar el servicio; filtros de rango y exportación CSV | Verificado localmente; sin política de retención automática |
| Dashboard operativo | [Aplicación local](../dashboard/README.md), gráficas de temperatura/humedad, histórico y estados de conexión | Verificado con datos reales en escritorio y vista de 485 px |
| Información útil | Estadísticas, antigüedad, estado USB y SOS pendientes de revisión; vínculo con decisiones de E1 | Implementado; falta validación de uso con excursionistas/operadores |
| Calidad del código | Módulos separados para captura, protocolo, almacenamiento, sondeo, consultas y presentación; pruebas automatizadas | Pruebas y sintaxis verificadas; instalación documentada |

La pantalla se actualiza cada cinco segundos y la adquisición solicitada es de 120 s. El mínimo de publicación automática de Meshtastic en este canal es de 1800 s; ambos mecanismos se documentan por separado. «ACK encolado» y «Revisada» son estados distintos de REGISTERED en el RAK y de la atención de una emergencia.

## Hardware · 30 %, pp. 4–6

| Entregable | Evidencia existente | Pendiente |
|---|---|---|
| Selección de componentes | Fichas y justificación base; compatibilidad RAK/Heltec 915 MHz comprobada en banco | Precisión por variable, consumo medido y argumento energético del montaje final |
| Esquemático y BOM | [Esquema de dos hojas, SVG y CSV](../hardware/esquematicos/README.md); [BOM de 30 partidas](../hardware/BOM.xlsx), cantidades, moneda y [cotizaciones](../hardware/cotizaciones.md) | Pinout oculto del BMS y mediciones del conjunto solar por cotejar; 20 partidas sin precio, costo completo abierto |
| Montaje y fotografías | Fotografías históricas y montaje funcional de banco | Fotos finales desde al menos tres ángulos, etiquetado y fijaciones del montaje evaluado |
| Reparación | Diseño modular y antecedentes de apertura | Apertura, reemplazo, cierre y recuperación funcional demostrados sin destruir el ensamble |

## Diseño 3D · 20 %, pp. 6–7

El repositorio incorpora Gill V7, F3D de ensamble e interior, inventario de componentes y vistas. La pauta permite volúmenes referenciales, siempre que sus dimensiones y posiciones representen el hardware real. La existencia del CAD no acredita ajuste físico.

Los [planos Gill V7](../diseño-3d/planos/README.md) incorporan doce hojas A3: conjunto y once tipos de pieza, con vistas ortogonales, isométricas de apoyo, cotas funcionales, escala y objetivos provisionales de tolerancia. La correspondencia registra SHA-256, cantidades y envolventes de los STEP. No se cambió la geometría CAD al generar los planos.

Pendientes: contraste del montaje final RAK/Heltec y botón con el gemelo, parametrización nativa, comprobación de tolerancias impresas y verificación física de accesos/interferencias. Los objetivos de tolerancia documentados no equivalen a medidas obtenidas en la impresión.

## Testing · 10 %, pp. 7–8

- [Ensayo de banco](../testing/banco-rak-heltec.md): temperatura por radio, persistencia, dos ciclos de 120 s y SOS físico observado con ACK. Los logs contienen WAITING, TX y REGISTERED.
- [Resultados](../testing/resultados.md): el evento físico terminado en `00000002` tardó 2,955 s entre las observaciones WAITING y REGISTERED del monitor USB; no es una medición instrumental del tiempo en aire.
- [Fallas](../testing/registro-fallas.md): se resolvió el rechazo de mensajes directos por falta de clave pública del destino y se verificó el retorno del ACK después de asociar contactos.
- Dashboard: pruebas de estadísticas, tiempo sin sincronizar, datos antiguos, persistencia, filtros, CSV, revisión/reapertura y API. La revisión visual cubrió gráficas y rangos vacíos con datos reales.

Faltan campañas por punto para la meta 9/10, distribución de latencias y pérdidas, consumo/reserva energética, calibración contra referencia, pruebas de reparación y validación de uso. Tres SOS de banco no prueban fiabilidad en montaña. El [vínculo con E1](../testing/validacion.md) describe qué se comprobó y qué sigue abierto.

## GitHub y presentación · 5 % cada uno, pp. 8–13

La estructura de carpetas, fuentes de firmware, estación, dashboard y guías de uso están disponibles. Se incorporan la pauta y evidencias del ensayo. Antes de entregar se deben verificar la publicación de la revisión final, clonación limpia, acceso del evaluador y apertura de todos los entregables.

La presentación requiere participación de todos, 8–10 minutos y 3 minutos de preguntas. La demo debe mostrar captura y dashboard en vivo, interpretar un resultado, abrir el encapsulado y mostrar el gemelo. Permanecen pendientes las diapositivas finales, la apertura física y los tres ensayos completos del día anterior. Las capturas no sustituyen esa demo.

## Criterio de cierre

El dashboard cubre la visualización y la consulta del histórico que faltaban. Para cerrar el Avance 3 deben completarse los pendientes de hardware, diseño, campaña de validación y presentación descritos arriba, y comprobarse la revisión final publicada. No se asigna una nota estimada ni se equipara una prueba de banco a validación en terreno.
