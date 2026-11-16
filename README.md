# Cerro Seguro · TEI201

Cerro Seguro es un proyecto de seguridad y comunicaciones en montaña, con un prototipo de nodo fijo SOS y telemetría ambiental sobre Meshtastic. Este repositorio reúne el software, hardware, diseño 3D y validación para el Avance 3 de TEI201, Universidad Adolfo Ibáñez.

**Estado al 16 de noviembre de 2026:** nodo RAK con sensor y SOS, estación Heltec USB, persistencia y dashboard operativos. El equipo confirmó 20/20 mensajes recibidos en menos de 60 s, salida de alimentación correcta, autonomía suficiente y encaje satisfactorio del montaje. Fabricación propia en PLA: 460 g aproximados. [Cierre funcional y alcance de las pruebas](testing/cierre-funcional-avance3.md).

El Avance 3 dispone de [firmware SOS sobre Meshtastic](firmware/meshtastic/README.md), [estación USB con SQLite](station/README.md), [dashboard local](dashboard/README.md), [esquema eléctrico](hardware/esquematicos/README.md), [BOM con referencias de costo](hardware/cotizaciones.md) y [planos Gill V7](diseño-3d/planos/README.md). El sondeo ambiental es de 120 s y el pulsador físico retorna REGISTERED. Faltan fotografías finales, datos de fecha/lugar/responsables para las actas y la presentación. La cobertura general en montaña, precisión ambiental y validación con usuarios conservan sus límites en la [verificación](docs/verificacion-avance3.md).

## Descripción del proyecto

| Campo | Definición |
|---|---|
| Nombre del proyecto | Cerro Seguro |
| Descripción | Nodo fijo SOS y telemetría ambiental sobre Meshtastic para seguridad y comunicaciones en montaña. Alcance operativo por validar. |
| Usuario y contexto de uso | Excursionistas y operadores de puntos fijos en cerros de la Región Metropolitana; caracterización preliminar en E1. |
| Problema identificado en Avance 1 | Comunicar alertas y disponer de monitoreo local donde la conectividad es irregular; integrar radios, sensores y energía en una plataforma mantenible. |
| Variable o fenómeno medido | Temperatura y humedad recibidas en vivo del RAK1906/BME680; calibración física pendiente. |
| Información que genera el sistema | Histórico ambiental, estadísticas, antigüedad del dato y registro SOS con revisión del operador. |
| Decisión que permite tomar | Revisar un SOS y consultar condiciones locales; coordinación operativa y utilidad en terreno por validar. |

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
| Captura | RAK1906/BME680, radio Meshtastic y solicitudes de banco cada 120 s | [Firmware](firmware/README.md) |
| Persistencia | SQLite con lecturas, alertas únicas y cola de ACK | [Arquitectura](docs/arquitectura.md) |
| Visualización | Dashboard local con gráficas, filtros, histórico y CSV | [Dashboard](dashboard/README.md) |
| Información | Estadísticas ambientales, frescura y SOS pendientes de revisión | [Indicadores](docs/indicadores.md) |
| Decisión | Revisar alertas y evaluar la vigencia y tendencia del dato; validación de uso pendiente | [Validación](testing/validacion.md) |

## Estructura del repositorio

```text
.
├── README.md
├── FUENTES.md
├── firmware/           # Código del dispositivo y dependencias
├── station/            # Recepción USB, SQLite, sondeo y ACK
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

Para la implementación actual, seguir los [comandos de compilación y configuración](firmware/meshtastic/README.md). El código original del ensayo LoRa puro de A2 sigue pendiente de versionar.

### 4. Conectar almacenamiento y dashboard

En el Mac, conectar el Heltec por USB y ejecutar desde la raíz del proyecto:

```bash
./iniciar.sh
```

El comando prepara las dependencias si faltan, detecta el puerto compatible con Heltec/CP210x, inicia la recepción y el dashboard y abre el navegador. Usa el RAK `!1630f9c9`, sondeo de 120 s y el histórico `station-data/cerroseguro.sqlite3`. Ctrl+C detiene ambos servicios. Si hay varios puertos compatibles, indicar `./iniciar.sh --port /dev/cu.usbserial-0001` con el puerto real.

**Acceso local:** [http://127.0.0.1:8765](http://127.0.0.1:8765). [Opciones del inicio conjunto y ejecución manual](dashboard/README.md).

### 5. Verificar el ciclo completo

Ejecutar [el protocolo de pruebas](testing/protocolo-pruebas.md). Comprobar una medición real, su persistencia, su visualización y al menos un indicador que permita decidir una acción. Reiniciar el sistema y verificar que el histórico continúa disponible.

## Uso y resultados

1. Encender el dispositivo según el procedimiento de hardware.
2. Abrir el dashboard y verificar la hora de la última medición válida.
3. Interpretar los indicadores con sus unidades, ventanas temporales y umbrales documentados.
4. Registrar las pruebas y revisar las limitaciones antes de tomar decisiones.

Los resultados, fallas y conclusiones se documentan en [testing/](testing/README.md). Hay antecedentes de A2: enlace cualitativo, [mediciones de antenas](testing/antenas-avance2.md) y [fallas de integración](testing/registro-fallas.md). El [ensayo RAK/Heltec](testing/banco-rak-heltec.md) incorpora logs de SOS, series ambientales y capturas del dashboard. Los protocolos T01–T08 requieren completar sus campañas, especialmente energía, alcance, calibración y reparación.

## Diseño 3D

Está disponible el [Gill final V7 con componentes](diseño-3d/fusion/gill-v7-75mm/README.md), con margen de 75 mm, nueve aletas, tapa inclinada y disco plano de antena. Se incluyen el [montaje completo](diseño-3d/fusion/gill-v7-75mm/34_Gill_V7_Completo_Margen75.f3d) y una [variante con aletas ocultas](diseño-3d/fusion/gill-v7-75mm/36_Gill_V7_Interior_Aletas_Ocultas.f3d) para inspeccionar el interior, además de [todo el inventario CAD](diseño-3d/fusion/componentes-nodo/README.md), piezas F3D/STEP/STL, fuente OpenSCAD y vistas exterior e interior.

La verificación digital y la reapertura de archivos no sustituyen la prueba física. Faltan los planos PDF, el ajuste real, ensayos de resistencia, agua y comportamiento térmico. Los modelos comerciales aproximados están identificados.

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
