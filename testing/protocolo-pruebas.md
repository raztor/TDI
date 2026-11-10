# Protocolo de pruebas

## Identificación de la campaña

| Campo | Valor |
|---|---|
| Fecha, hora y zona horaria | Pendiente |
| Responsable | Pendiente |
| Lugar y condiciones ambientales | Pendiente |
| Dispositivo y revisión del hardware | Pendiente |
| Revisión o commit del firmware y dashboard | Pendiente |
| Configuración de radio/red y almacenamiento | Pendiente |
| Instrumento de referencia y calibración | Pendiente, si corresponde |
| Duración, intervalo y cantidad de muestras | Pendiente |
| Criterios de éxito aprobados antes de ejecutar | Pendiente |

Para cada prueba registrar valores esperados y observados, archivos de evidencia, resultado y limitaciones. El estado inicial de todas las pruebas es **no ejecutada**.

## T01 · Captura continua

**Objetivo:** comprobar que las variables del entorno se capturan con la frecuencia definida y sin pérdidas no explicadas.

**Condiciones:** dispositivo montado, sensores estabilizados según fabricante, reloj verificado, período de muestreo y duración documentados.

**Procedimiento:**
1. Registrar configuración, hora inicial, período de captura y número de muestras esperado.
2. Iniciar la captura real durante el intervalo definido antes de la prueba.
3. Registrar marcas de tiempo, valores, unidades y errores de cada sensor.
4. Identificar muestras ausentes, inválidas o duplicadas; contrastar con el intervalo configurado.
5. Documentar reinicios o cortes y su efecto en la continuidad.

**Criterio:** duración mínima, frecuencia y proporción máxima de muestras perdidas o inválidas por definir y justificar según el problema antes de ejecutar.

**Métricas:** muestras esperadas/recibidas/válidas, intervalo observado, tasa de pérdida y error. **Evidencia:** datos originales y log del dispositivo.

## T02 · Almacenamiento persistente e histórico

**Objetivo:** verificar que los datos permanecen disponibles al cerrar y reiniciar el sistema.

**Procedimiento:**
1. Capturar y guardar una secuencia identificable con marcas de tiempo.
2. Consultarla en la base de datos o archivo estructurado, sin depender del monitor serial.
3. Registrar el número de filas y rango temporal.
4. Reiniciar el dispositivo y el servicio de visualización de forma controlada.
5. Consultar nuevamente la misma secuencia y verificar integridad y ausencia de duplicados.

**Criterio:** todas las mediciones confirmadas como almacenadas antes del reinicio siguen consultables con valores e identificadores iguales.

**Evidencia:** consulta o exportación anterior y posterior, log de reinicio y captura del histórico.

## T03 · Dashboard y latencia

**Objetivo:** verificar que los datos llegan al dashboard y pueden interpretarse.

**Procedimiento:**
1. Abrir el dashboard usando las instrucciones del repositorio.
2. Comprobar que cada métrica tiene unidad, marca temporal y contexto.
3. Producir una variación segura y real del fenómeno, adecuada al sensor.
4. Registrar la hora de captura y la hora de visualización de cada muestra seleccionada, con relojes sincronizados.
5. Consultar el histórico y comprobar que coincide con la fuente persistente.
6. Interrumpir la actualización y verificar que datos antiguos no se presenten como actuales.

**Criterio:** datos correctos y trazables, histórico accesible y aviso de datos antiguos. Fijar una latencia máxima tolerable según la decisión que se apoya.

**Métricas:** latencia media, máxima y percentil 95 con tamaño de muestra. **Evidencia:** tabla temporal, capturas y registros.

## T04 · Indicadores y alertas

**Objetivo:** comprobar cálculos, unidades y estados que orientan una decisión.

**Procedimiento:**
1. Documentar fórmula, ventana temporal, umbral y justificación de cada indicador.
2. Contrastar el cálculo con un conjunto controlado, claramente separado de las mediciones reales.
3. Revisar comportamiento en el límite, datos faltantes y recuperación de la alerta.
4. Verificar con datos del prototipo al menos un resultado que responda al problema.
5. Explicar qué acción corresponde y cuáles son sus límites.

**Criterio:** cálculo correcto dentro de la tolerancia previamente definida, estados coherentes y vínculo explícito entre indicador y decisión. Una prueba con valores controlados no reemplaza la validación con datos reales.

**Evidencia:** cálculo de contraste, casos límite y captura de la decisión apoyada por el dashboard.

## T05 · Interrupciones y recuperación

**Objetivo:** medir qué ocurre cuando falla la conectividad o se reinicia el dispositivo.

**Procedimiento:**
1. Registrar el funcionamiento normal y el último dato persistido.
2. Interrumpir la conexión de forma controlada, sin retirar antenas de un transmisor encendido.
3. Registrar el error detectado, datos perdidos o retenidos y avisos del dashboard.
4. Restablecer la conexión y medir el tiempo hasta la siguiente muestra válida.
5. Revisar duplicados, pérdidas y coherencia temporal del histórico.

**Criterio:** falla visible, recuperación y tratamiento de datos conforme a la estrategia documentada. Definir previamente tiempo máximo de recuperación y pérdida tolerada.

**Evidencia:** línea de tiempo, log de eventos y datos antes/durante/después.

## T06 · Comparación de sensores

**Objetivo:** cuantificar el error de las variables para las que exista una referencia adecuada.

**Procedimiento:**
1. Identificar instrumento de referencia, resolución, incertidumbre y condiciones de validez.
2. Estabilizar ambos instrumentos y situarlos bajo condiciones comparables.
3. Tomar pares de lecturas con marcas temporales durante el rango disponible.
4. Calcular error, sesgo y error absoluto medio por variable y unidad.
5. Separar limitaciones de la referencia, del montaje y del sensor.

**Criterio:** umbral por variable definido antes de medir, relacionado con la necesidad del proyecto y condiciones de la hoja de datos. Si no hay referencia adecuada, registrar la limitación y no afirmar precisión validada.

**Evidencia:** pares de datos, cálculo y descripción del montaje. No interpretar la salida de gas del BME680 como medición directa de CO₂.

## T07 · Ensamble y reparación

**Objetivo:** verificar acceso a componentes sin destruir el encapsulado y correspondencia del gemelo 3D.

**Procedimiento:**
1. Revisar el montaje frente a BOM, esquemático y ensamble Fusion 360.
2. Desconectar alimentación y seguir el procedimiento de apertura.
3. Acceder a un componente crítico y realizar el reemplazo o desmontaje/reinstalación documentado.
4. Cerrar, revisar el cableado y restablecer alimentación.
5. Comprobar captura, almacenamiento y dashboard; registrar tiempo y dificultad.

**Criterio:** apertura reversible, ausencia de daños, acceso a componentes y funcionamiento restablecido. Las interferencias y diferencias con el modelo deben registrarse.

**Evidencia:** fotos antes/durante/después, registro de tiempo y prueba funcional posterior.

## T08 · Validación del problema y demo completa

**Objetivo:** comprobar que los datos del sistema permiten responder una pregunta del Avance 1.

**Procedimiento:**
1. Identificar usuario, escenario real, pregunta y decisión en [validacion.md](validacion.md).
2. Definir duración, condiciones y criterio que harían útil la información.
3. Ejecutar el ciclo completo con el prototipo y capturar datos reales.
4. Relacionar los resultados cuantitativos con la decisión, sin generalizar fuera de las condiciones probadas.
5. Ensayar captura, dashboard, apertura y gemelo 3D dentro del tiempo de presentación.

**Criterio:** información verificable que responde al problema, resultados interpretables y limitaciones explícitas. La demo debe funcionar en vivo.

**Evidencia:** datos originales, gráficos, conclusiones y [registro de ensayos](../docs/presentacion/ensayos.md).
