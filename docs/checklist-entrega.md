# Checklist de entrega

**Evaluación:** 23 de noviembre de 2026. Completar y subir los entregables antes de la presentación.

El [estado de los avances 1 y 2](avances/revision-avances-1-2.md) resume los resultados y pendientes anteriores. Esta lista corresponde a la entrega final. La [pauta](pautas/avance-03-estudiantes.pdf) está cotejada en la [verificación](verificacion-avance3.md).

## Software · 30 %

- [ ] Dispositivo capturando datos reales de forma continua y confiable.
- [x] Frecuencia de muestreo justificada según el problema: sondeo de 120 s documentado.
- [x] Almacenamiento persistente e histórico accesible después de reiniciar.
- [x] Dashboard accesible, con gráficas y contexto de interpretación.
- [x] Estadísticas, alertas o indicadores útiles para decidir.
- [x] Código modular de firmware, estación y dashboard disponible en la revisión del proyecto.
- [x] Dependencias, configuración, instalación y carga reproducibles.

El banco y los resultados reportados cubren telemetría, SOS/ACK, 20/20 mensajes bajo 60 s y energía suficiente. Falta completar duración y condiciones de ensayo en las actas; no se informó calibración del sensor contra referencia.

## Hardware · 30 %

- [ ] Componentes justificados por rango, precisión, consumo y compatibilidad.
- [x] Esquema de módulos editable y PDF; terminales y salida aceptados por el equipo.
- [x] BOM con 31 partidas, cantidades, especificaciones, importes y moneda; material impreso contado una vez.
- [ ] Montaje ordenado, conexiones seguras y etiquetadas.
- [x] Fotografías reales del interior desde tres ángulos, indexadas en hardware/fotos; exterior no fabricado.
- [ ] Encapsulado abre sin destruirse y componentes críticos reemplazables.
- [ ] Demostración de apertura y acceso ensayada.

## Diseño 3D · 20 %

- [x] Ensamble completo de Fusion 360 exportado a .f3d: [Gill V7](../diseño-3d/fusion/gill-v7-75mm/README.md).
- [ ] Todos los componentes representados con dimensiones y posiciones reales.
- [ ] Parametrización, tolerancias e interferencias revisadas.
- [x] Encaje del interior impreso aceptado; fotografías interiores indexadas; exterior no fabricado.
- [x] Renders exterior e interior con materiales e iluminación; diseño exterior no fabricado identificado.
- [x] [Planos PDF](../diseño-3d/planos/README.md) con vistas ortogonales, cotas funcionales, objetivos de tolerancia y escala; encaje satisfactorio reportado.
- [x] Archivos completo e interior reabiertos en Fusion 360; nueve aletas conservadas en ambas variantes.

La entrega CAD incluye vistas exterior e interior, revisión digital de interferencias y planos PDF de doce hojas. Se aceptó funcionalmente el encaje del montaje impreso en PLA. Quedan el cotejo documental de modelos comerciales aproximados y la parametrización nativa. Los renders finales están disponibles e identifican la envolvente no fabricada.

## Testing · 10 %

- [ ] Protocolo con objetivo, condiciones, pasos, criterios de éxito y evidencias.
- [ ] Criterios cuantitativos fijados antes de ejecutar las pruebas.
- [x] Resultados de banco y tabla del ensayo reportado 20/20 bajo 60 s; sin registro de tiempos individuales.
- [x] Al menos una falla real, análisis de causa y corrección comprobada.
- [ ] Validación explícita contra el problema del Avance 1.
- [x] Alcance, limitaciones y mejoras documentados en resultados y cierre funcional.

## GitHub · 5 %

- [x] Carpetas firmware/, hardware/, diseño-3d/, testing/ y docs/ creadas.
- [x] README actualizado con arquitectura, integrantes, componentes y enlaces de instalación/uso; aportes y roles de A3 por confirmar en actas.
- [ ] FUENTES.md completo con las tres categorías solicitadas en la sección 6 de la guía.
- [ ] Todos los códigos, esquemáticos, CAD, documentos y evidencias subidos.
- [x] Historial con mensajes de commit descriptivos.
- [ ] Clonación limpia y apertura de los archivos comprobadas.
- [ ] Repositorio público o acceso del evaluador confirmado.
- [ ] URL del repositorio incluida en los slides.
- [ ] Revisión final sin credenciales ni archivos temporales.

## Presentación · 5 %

- [ ] Slides conectan problema, solución y resultados.
- [ ] Dispositivo cargado y conectado; dashboard abierto.
- [ ] Captura y visualización reales durante la demo.
- [ ] Al menos un resultado interpretado y conectado a una decisión.
- [ ] Apertura del encapsulado y gemelo 3D preparados.
- [ ] Tres ensayos completos el 22 de noviembre registrados.
- [ ] Todos los integrantes tienen rol y conocen el funcionamiento técnico.
- [ ] Presentación ensayada entre 8 y 10 minutos.
- [ ] Preparados para 3 minutos de preguntas técnicas.

## Cierre

- Responsable de revisión: pendiente.
- Fecha y hora: pendiente.
- Commit o revisión entregada: pendiente.
- Estado documental: renders, fotos interiores, BOM y serie distancia/SNR incorporados. Mantener trazables la revisión entregada, los metadatos no informados y el alcance físico sin envolvente exterior.

Un video pregrabado no reemplaza la demo en vivo. La existencia de FUENTES.md por sí sola no acredita una declaración completa.
