# Cerro Seguro · TEI201

Cerro Seguro es un proyecto de seguridad y comunicaciones en montaña, con un prototipo de repetidor y telemetría ambiental. Este repositorio reúne el software, hardware, diseño 3D y validación para el Avance 3 de TEI201, Universidad Adolfo Ibáñez.

**Estado al 15 de noviembre de 2026:** el Avance 2 documenta un enlace LoRa funcional, fotografías del montaje, capturas de terminal, mediciones de antenas y fallas de integración. La reproducción de los ensayos y la validación del sistema completo siguen pendientes. Ver [estado y pendientes de los avances 1 y 2](docs/avances/revision-avances-1-2.md).

## Descripción del proyecto

| Campo | Definición |
|---|---|
| Nombre del proyecto | Cerro Seguro |
| Descripción | Prototipo de repetidor y telemetría ambiental para un proyecto de seguridad y comunicaciones en montaña. Alcance operativo por validar. |
| Usuario y contexto de uso | Excursionistas y operadores de puntos fijos en cerros de la Región Metropolitana; caracterización preliminar en E1. |
| Problema identificado en Avance 1 | Comunicar alertas y disponer de monitoreo local donde la conectividad es irregular; integrar radios, sensores y energía en una plataforma mantenible. |
| Variable o fenómeno medido | Temperatura, humedad y presión mostradas en capturas de A2; series originales y validación pendientes. |
| Información que genera el sistema | Mensajes de alerta, estado de recepción y telemetría; alcance reportado y límites en la revisión de antecedentes. |
| Decisión que permite tomar | Recibir e interpretar una alerta y consultar condiciones locales; receptor operativo y protocolo de respuesta por definir. |

El problema, sus antecedentes y los criterios de validación se registran en [problema y alcance](docs/problema-y-alcance.md).

## Equipo

| Integrante | Responsabilidad técnica | Rol en la presentación |
|---|---|---|
| Benjamín Muñoz | E1: conceptualización, investigación y borrador; tareas actuales por asignar | Pendiente |
| Benjamín Quijada | E1: bibliografía, datos y análisis técnico; tareas actuales por asignar | Pendiente |
| Exequiel Najle | E1: metodología, alternativas y visualización; tareas actuales por asignar | Pendiente |
| Javiera Cárdenas | E1: gestión, revisión y edición; tareas actuales por asignar | Pendiente |

Las contribuciones corresponden al Avance 1. Los roles del Avance 3 están pendientes de asignación. Las [actas y decisiones](docs/avances/actas-y-decisiones.md) describen el PCB modular, el descarte de la antena compartida y la evolución hacia placas comerciales.

Todos los integrantes deben participar en la presentación y poder explicar el funcionamiento del sistema.

## Ciclo de datos

El sistema debe completar el recorrido **captura real → almacenamiento persistente → visualización → información → decisión**.

| Etapa | Implementación del proyecto | Evidencia |
|---|---|---|
| Captura | A2 muestra TX/RX de temperatura, humedad y presión; fuente y configuración por recuperar | [Firmware](firmware/README.md) |
| Persistencia | Pendiente: servicio o archivo estructurado e histórico | [Arquitectura](docs/arquitectura.md) |
| Visualización | Pendiente: dashboard en vivo e histórico | [Dashboard](dashboard/README.md) |
| Información | Pendiente: indicadores, estadísticas o alertas | [Indicadores](docs/indicadores.md) |
| Decisión | Pendiente: acción del usuario sustentada por los datos | [Validación](testing/validacion.md) |

## Estructura del repositorio

```text
.
├── README.md
├── FUENTES.md
├── firmware/           # Código del dispositivo y dependencias
├── dashboard/          # Visualización y configuración reproducible
├── hardware/           # BOM, conexiones, esquemático y fotos
├── diseño-3d/          # Ensamble Fusion 360, planos y renders
├── testing/            # Protocolos, datos, resultados y evidencias
└── docs/               # Problema, arquitectura, reporte y presentación
```

Los archivos fuente deben conservarse junto a sus exportaciones. Las carpetas contienen instrucciones de entrega; no sustituyen los archivos técnicos que faltan.

## Componentes necesarios

El Avance 2 identifica RAK19007, RAK4631 y RAK1906/BME680 como utilizados, y fotografía dos LILYGO de bandas diferentes. También reporta Heltec disponibles, dos antenas y alimentación con LiPo 3S, BMS, controlador solar y DC-DC. El [inventario histórico](hardware/inventario-historico.md) distingue esos equipos de elementos retirados y propuestos. Faltan cantidades consolidadas, revisiones, modelos de energía y costos.

La lista de materiales se mantiene en [hardware/BOM.xlsx](hardware/BOM.xlsx). Antes de replicar el dispositivo debe contener componente, modelo o especificación, cantidad, costo unitario, costo total, moneda y fuente de compra.

- [Justificación técnica](hardware/seleccion-componentes.md): rango, precisión, consumo y compatibilidad.
- [Conexiones](hardware/conexiones.md): pines, señales y alimentación.
- [Esquemático](hardware/esquematicos/README.md): fuente editable y PDF.
- [Montaje y reparación](hardware/reparacion.md): apertura, acceso y reemplazo de componentes.

**Pendiente:** confirmar la lista real de componentes, el esquema eléctrico y la alimentación antes de conectar el hardware.

## Instalación y puesta en marcha

### 1. Obtener el proyecto

```bash
git clone https://github.com/raztor/TDI.git
cd TDI
```

Usar la rama o revisión correspondiente al prototipo que se va a probar.

### 2. Preparar el entorno

1. Consultar [firmware/README.md](firmware/README.md) y confirmar placa, IDE, versiones y dependencias.
2. Instalar las dependencias declaradas en [FUENTES.md](FUENTES.md).
3. Preparar la configuración local. No publicar contraseñas, tokens ni claves privadas.

### 3. Cargar el firmware

1. Verificar el montaje contra el esquemático y revisar polaridad y tensión de alimentación.
2. Abrir el proyecto indicado en [firmware/README.md](firmware/README.md).
3. Seleccionar la placa y el puerto correctos; compilar y cargar con el comando o procedimiento documentado allí.
4. Confirmar lecturas reales, unidad, fecha/hora y frecuencia de captura.

**Pendiente:** incorporar el código y los comandos exactos de compilación y carga usados en A2. Se conocen las familias de placas; IDE, versiones, parámetros y revisión exacta no están documentados.

### 4. Conectar almacenamiento y dashboard

Seguir [dashboard/README.md](dashboard/README.md). Debe indicar la URL accesible durante la evaluación o el comando de ejecución local, su configuración y la forma de recuperar el histórico.

**Acceso al dashboard:** pendiente. **Inicio local:** pendiente.

### 5. Verificar el ciclo completo

Ejecutar [el protocolo de pruebas](testing/protocolo-pruebas.md). Comprobar una medición real, su persistencia, su visualización y al menos un indicador que permita decidir una acción. Reiniciar el sistema y verificar que el histórico continúa disponible.

## Uso y resultados

1. Encender el dispositivo según el procedimiento de hardware.
2. Abrir el dashboard y verificar la hora de la última medición válida.
3. Interpretar los indicadores con sus unidades, ventanas temporales y umbrales documentados.
4. Registrar las pruebas y revisar las limitaciones antes de tomar decisiones.

Los resultados, fallas y conclusiones se documentan en [testing/](testing/README.md). Hay antecedentes de A2: enlace cualitativo, [mediciones de antenas](testing/antenas-avance2.md) y [fallas de integración](testing/registro-fallas.md). Los logs de mensajes y las series ambientales están pendientes de versionar. Los protocolos T01–T08 del Avance 3 están pendientes de ejecución.

## Diseño 3D

Está disponible el [escudo Gill V1 conceptual](diseño-3d/gill-v1/README.md), con fuente OpenSCAD y cinco STL, además de referencias mecánicas previas. El [gemelo 3D](diseño-3d/README.md) completo sigue pendiente: carcasa y componentes internos representativos del montaje, ensamble `.f3d` o `.f3z`, planos PDF y renders.

## Entrega del Avance 3

- **Fecha:** 23 de noviembre de 2026.
- **Presentación:** 8–10 minutos y 3 minutos de preguntas, presencial con demo en vivo.
- **Ponderación:** software 30 %, hardware 30 %, diseño 3D 20 %, testing 10 %, GitHub 5 % y presentación 5 %.
- **Revisión completa:** [checklist de entrega](docs/checklist-entrega.md).
- **Trazabilidad:** [requisitos y evidencias](docs/requisitos.md).
- **Documentación final:** [reporte](docs/reporte-final.md) y [guion de presentación](docs/presentacion/guion.md).

La guía exige funcionamiento real durante la demo. Un video, datos de ejemplo o carpetas vacías no reemplazan el prototipo ni sus evidencias. Antes de la presentación, todos los entregables deben estar subidos y el evaluador debe poder acceder al repositorio.

## Fuentes

Las dependencias, el código externo y las declaraciones correspondientes se mantienen en [FUENTES.md](FUENTES.md).
