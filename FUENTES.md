# Fuentes del proyecto

Registro de bibliotecas, código y recursos reutilizados, y asistencia en el desarrollo de Cerro Seguro. Estructura basada en la sección 6 de la [pauta del Avance 3](docs/pautas/avance-03-estudiantes.pdf), páginas impresas 13–15. Revisión documental: **16 de noviembre de 2026**.

## Librerías utilizadas

### Firmware y protocolo

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| Meshtastic firmware | `v2.7.26.54e0d8d`, commit `54e0d8d0ab2ff56b3a9ce967e53f79e49af560fb` | Base del RAK4631: mensajería, radio y telemetría. Firmware oficial de la estación Heltec en el banco documentado. | [Código de la revisión](https://github.com/meshtastic/firmware/tree/v2.7.26.54e0d8d) |
| Meshtastic/Adafruit nRF52 Arduino | Commit `9ddcbc9568b12f102f9e88bd4d1b88ea789213a4` | Framework Arduino para nRF52840; GPIO, USB, buses y plataforma del RAK. | [Revisión fijada](https://github.com/meshtastic/Adafruit_nRF52_Arduino/tree/9ddcbc9568b12f102f9e88bd4d1b88ea789213a4) |
| Meshtastic protobufs | Commit `6b1ded439633cd03d4af85b44231b91d1d106278` del submódulo del firmware | Esquemas de mensajes, configuración y telemetría reutilizados. | [Definiciones del protocolo](https://github.com/meshtastic/protobufs/tree/6b1ded439633cd03d4af85b44231b91d1d106278) |
| RadioLib | `7.6.0` | Control de radio SX1262 a través de Meshtastic. | [Código](https://github.com/jgromes/RadioLib/tree/7.6.0) |
| Nanopb | `0.4.9+1` en el gestor; fuente `nanopb-0.4.9.1` | Codificación protobuf embebida. | [Código](https://github.com/nanopb/nanopb/tree/nanopb-0.4.9.1) |
| Bosch BSEC2, paquete Arduino `bsec2` | `1.10.2610`; algoritmo BSEC `2.6.1.0` | Procesamiento del BME680 mediante el controlador de telemetría upstream. El dashboard interpreta temperatura y humedad; no acredita calibración de IAQ ni medición directa de CO₂. | [Biblioteca Bosch](https://github.com/boschsensortec/Bosch-BSEC2-Library) |
| Bosch BME68x Sensor library | `1.3.40408` | Control de bajo nivel del sensor ambiental, dependencia de BSEC2. | [Código](https://github.com/boschsensortec/Bosch-BME68x-Library/tree/v1.3.40408) |

Las **75 entradas del grafo de dependencias del firmware** se detallan con versión y fuente en el [inventario completo](docs/fuentes/dependencias.md#dependencias-resueltas-del-firmware-rak4631). Incluye bibliotecas de pantalla, sensores y funciones disponibles en la base: su presencia no significa que todos esos periféricos estén instalados o activos.

El código de integración de Meshtastic conserva [GPL-3.0](firmware/meshtastic/COPYING) y sus avisos SPDX. Las bibliotecas y los binarios de terceros conservan sus propias licencias, incluida la [licencia de Bosch BSEC](https://github.com/boschsensortec/Bosch-BSEC2-Library/blob/master/LICENSE.md).

### Estación USB y configuración

| Librería | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| Meshtastic Python | `2.7.11` | `SerialInterface`, recepción de paquetes, mensajes dirigidos y solicitudes ambientales al RAK. | [Código](https://github.com/meshtastic/python), [API](https://python.meshtastic.org/) |
| pySerial | `3.5` | Transporte USB serie y detección mediante `serial.tools.list_ports`. | [Código](https://github.com/pyserial/pyserial), [API de puertos](https://pyserial.readthedocs.io/en/latest/tools.html) |
| PyPubSub | `4.0.7` | Suscripciones a recepción y pérdida de conexión publicadas por Meshtastic. Es un bus de eventos Python, no el cliente MQTT de la red. | [Código](https://github.com/schollii/pypubsub) |
| protobuf para Python | `7.36.2` en el entorno verificado | Decodificación de mensajes de telemetría y tratamiento de errores de protobuf. | [Código](https://github.com/protocolbuffers/protobuf) |
| PyYAML | `6.0.3` | Lectura y comprobación de perfiles YAML de configuración. | [Código](https://github.com/yaml/pyyaml) |

Las **18 distribuciones de la estación**, incluidas las dependencias transitivas de Meshtastic para macOS, figuran en el [inventario completo](docs/fuentes/dependencias.md#entorno-de-estación-usb-en-macos). `station/requirements.txt` fija Meshtastic; las versiones transitivas reflejan el entorno inspeccionado y no constituyen un archivo de bloqueo.

### Biblioteca estándar y frontend

| Librería o plataforma | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| Python | `3.11.9` en estación/dashboard; `3.12.14` en generación de planos | Ejecución de servicios, herramientas y pruebas. | [Python](https://www.python.org/), [biblioteca estándar 3.11](https://docs.python.org/3.11/library/) |
| `http.server` | Incluido en Python | API HTTP y archivos estáticos mediante `ThreadingHTTPServer` y `BaseHTTPRequestHandler`. | [Documentación](https://docs.python.org/3.11/library/http.server.html) |
| SQLite / `sqlite3` | SQLite `3.45.1` en el entorno de estación; módulo incluido en Python | Persistencia de mediciones, SOS, cola de ACK, estado USB y revisión del operador; transacciones y WAL. | [SQLite](https://www.sqlite.org/), [API Python](https://docs.python.org/3.11/library/sqlite3.html) |
| `json`, `csv`, `datetime`, `statistics`, `math`, `re` | Incluidos en Python | Serialización, exportación CSV, tiempo, estadísticas y validación de valores/formatos. | [Biblioteca estándar](https://docs.python.org/3.11/library/) |
| `queue`, `threading`, `time`, `logging`, `contextlib` | Incluidos en Python | Recepción desacoplada, sondeo, reconexión, estado del servicio y transacciones. | [Biblioteca estándar](https://docs.python.org/3.11/library/) |
| `argparse`, `pathlib`, `os`, `sys`, `signal`, `socket`, `subprocess`, `urllib`, `webbrowser`, `importlib`, `shutil`, `hashlib`, `html`, `errno` | Incluidos en Python | CLI, rutas, detección/preparación del entorno, supervisión de procesos, comprobación HTTP, navegación y generación/verificación de archivos. | [Biblioteca estándar](https://docs.python.org/3.11/library/) |
| `unittest`, `unittest.mock`, `tempfile`, `types` | Incluidos en Python | Pruebas, dobles de radio/procesos y bases temporales. | [unittest](https://docs.python.org/3.11/library/unittest.html) |
| HTML5, CSS y JavaScript del navegador | APIs nativas del navegador | Interfaz local, `fetch`, filtros, tablas, estadísticas y SVG. No se carga una biblioteca gráfica externa. | [Estándar HTML](https://html.spec.whatwg.org/), [Fetch](https://fetch.spec.whatwg.org/), [SVG](https://www.w3.org/TR/SVG2/) |

### Compilación, CAD y elaboración de documentos

| Librería o herramienta | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| PlatformIO Core | `6.1.18` | Compilación reproducible del firmware y gestión de paquetes. | [Código](https://github.com/platformio/platformio-core) |
| PlatformIO Nordic nRF52 | `10.11.0` | Plataforma y definición de placa `wiscore_rak4631`. | [Código](https://github.com/platformio/platform-nordicnrf52) |
| GNU Arm toolchain, paquete PlatformIO | `1.90301.200702`, GCC `9.3.1` | Compilación C/C++ del RAK. | [Paquete](https://registry.platformio.org/tools/platformio/toolchain-gccarmnoneeabi) |
| CadQuery | `2.8.0` | Lectura de STEP y preparación geométrica de vistas de planos. | [Código](https://github.com/CadQuery/cadquery), [documentación](https://cadquery.readthedocs.io/en/latest/importexport.html) |
| cadquery-ocp / OCP | `7.9.3.1.1` | Bindings Open CASCADE: proyección HLR y discretización de curvas. | [Código](https://github.com/CadQuery/OCP) |
| ReportLab | `5.1.0` | Composición y exportación PDF de planos mecánicos y esquema eléctrico. | [Documentación](https://docs.reportlab.com/) |
| pypdf | `6.21.4` en las herramientas de revisión | Extracción de texto y comprobación de páginas/formato de documentos PDF. | [Código](https://github.com/py-pdf/pypdf) |
| Pillow | `13.0.0` en las herramientas de revisión | Preparación de imágenes de comprobación y hojas de contacto para revisar planos. | [Código](https://github.com/python-pillow/Pillow) |
| Poppler / `pdftoppm` | `26.09.0` | Rasterización de PDF para inspección visual. | [Proyecto](https://poppler.freedesktop.org/) |
| Node.js | `24.22.1` en elaboración de la BOM | Ejecución de la herramienta JavaScript de edición de planillas; no sirve el dashboard. | [Proyecto](https://nodejs.org/) |
| `@oai/artifact-tool` | `2.8.157` | Edición, cálculo, exportación y revisión visual de la BOM XLSX. | Paquete suministrado por el entorno de OpenAI; URL pública del paquete no consignada. |
| Autodesk Fusion y su API | Versión de aplicación no consignada | Ensambles, representación de componentes, exportaciones F3D/STEP/STL y comprobación de apertura. | [API oficial](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/GettingStarted.htm) |
| Bash | Versión no fijada; intérprete del Mac | Entrada `iniciar.sh`, preparación de `.venv` y ejecución del supervisor Python. | [GNU Bash](https://www.gnu.org/software/bash/) |

Las **46 distribuciones del entorno de planos**, las **34 del entorno Python de compilación** y los paquetes del framework/toolchain se detallan en el [inventario completo](docs/fuentes/dependencias.md). Son herramientas de elaboración o compilación, separadas de las dependencias de ejecución del dashboard. Los archivos OpenSCAD aportados se conservan como fuentes CAD; no se atribuye una versión de OpenSCAD que no esté registrada.

## Código externo adaptado

Las entradas identifican la base reutilizada y la adaptación del proyecto. El uso de una API se distingue de la copia de un fragmento literal.

### Firmware Meshtastic y módulo SOS del RAK

- **Archivos del proyecto:** [CerroSeguroModule.cpp](firmware/meshtastic/CerroSeguroModule.cpp), [CerroSeguroModule.h](firmware/meshtastic/CerroSeguroModule.h), [SosState.h](firmware/meshtastic/SosState.h), [SosProtocol.h](firmware/meshtastic/SosProtocol.h) y [prepare.py](firmware/meshtastic/prepare.py).
- **Fuente:** [SinglePortModule](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/src/mesh/SinglePortModule.h), [ReplyModule](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/src/modules/ReplyModule.cpp), [API de módulos](https://meshtastic.org/docs/development/device/module-api/) y [Modules.cpp](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/src/modules/Modules.cpp).
- **Reutilización:** arquitectura de módulos, `concurrency::OSThread`, paquetes Meshtastic y envío mediante `service->sendToMesh`.
- **Adaptación:** incorporación del módulo del proyecto a la revisión fijada; entrada AIN1/P0.31 con pull-up, filtro de rebotes, pulsación mantenida, estados SOS y confirmación de registro por evento. `prepare.py` añade inclusión/instancia y crea el entorno PlatformIO sin duplicar la integración.
- **Límite:** se conserva el transporte Meshtastic; no se implementa un protocolo LoRa alternativo ni una función propia de repetidor.

### Sensor BME680 y esquemas protobuf

- **Archivos del proyecto:** [perfiles de radio/sensor](firmware/config/), [polling.py](station/polling.py) y [receiver.py](station/receiver.py).
- **Fuente:** [BME680Sensor.cpp](https://github.com/meshtastic/firmware/blob/v2.7.26.54e0d8d/src/modules/Telemetry/Sensor/BME680Sensor.cpp), [telemetría Meshtastic](https://meshtastic.org/docs/configuration/module/telemetry/) y [protobufs fijados](https://github.com/meshtastic/protobufs/tree/6b1ded439633cd03d4af85b44231b91d1d106278).
- **Reutilización:** adquisición del sensor y tipos `Telemetry`/`EnvironmentMetrics` del proyecto upstream; controlador Bosch a través de Meshtastic.
- **Adaptación:** habilitación del sensor del RAK1906, solicitudes ambientales desde el computador cada 120 s y selección de temperatura/humedad para el dashboard. La publicación automática del canal público conserva su intervalo separado de 1800 s.
- **Límite:** el procesamiento upstream no se presenta como un controlador BME680 escrito desde cero ni como calibración validada del prototipo.

### Adaptador USB, recepción y ACK desde el computador

- **Archivos del proyecto:** [main.py](station/main.py), [receiver.py](station/receiver.py), [polling.py](station/polling.py), [store.py](station/store.py) y [protocol.py](station/protocol.py).
- **Fuente:** [Meshtastic Python 2.7.11](https://pypi.org/project/meshtastic/2.7.11/), [API SerialInterface](https://python.meshtastic.org/meshtastic/serial_interface.html), [sendText/sendData y eventos](https://python.meshtastic.org/) y [SQLite en Python](https://docs.python.org/3.11/library/sqlite3.html).
- **Reutilización:** transporte USB/protobuf de la biblioteca oficial y suscripciones de PyPubSub; API SQLite de Python.
- **Adaptación:** filtrado de nodos/destino/canal, validación `CS1`, deduplicación de eventos, registro persistente antes del ACK, cola de confirmaciones recuperable, reconexión y sondeo ambiental no bloqueante. El Heltec mantiene firmware oficial y actúa como interfaz de radio.
- **Límite:** el ACK de registro, su encolado, la recepción en el RAK y la revisión humana son estados diferentes.

### Servidor HTTP, persistencia y supervisor de inicio

- **Archivos del proyecto:** [server.py](dashboard/server.py), [data.py](dashboard/data.py), [iniciar.sh](iniciar.sh) e [iniciar.py](tools/iniciar.py).
- **Fuente:** [http.server](https://docs.python.org/3.11/library/http.server.html), [sqlite3](https://docs.python.org/3.11/library/sqlite3.html), [subprocess](https://docs.python.org/3.11/library/subprocess.html), [signal](https://docs.python.org/3.11/library/signal.html) y [pySerial list_ports](https://pyserial.readthedocs.io/en/latest/tools.html).
- **Reutilización:** clases y funciones de esas API; no constituyen un framework web adicional.
- **Adaptación:** endpoints del proyecto, consultas por rango/nodo, CSV y revisión de alertas; detección Heltec/CP210x, espera de SQLite, arranque de ambos servicios y cierre de sus procesos propios con Ctrl+C. El frontend HTML/CSS/JavaScript y sus gráficas SVG se desarrollaron para Cerro Seguro con asistencia declarada en la sección siguiente.

### Generación de planos mecánicos y eléctricos

- **Archivo del proyecto:** [generar.py](tools/planos/generar.py).
- **Fuente:** [importación/exportación de CadQuery](https://cadquery.readthedocs.io/en/latest/importexport.html), [OCP](https://github.com/CadQuery/OCP) y [ReportLab](https://docs.reportlab.com/).
- **Reutilización:** APIs de importación STEP, geometría Open CASCADE, eliminación de líneas ocultas y dibujo PDF.
- **Adaptación:** proyección del conjunto y once tipos de pieza V7, cotas de envolvente del sólido, escalas, cartelas, inventario y salida SVG/PDF; dos hojas de interconexión eléctrica. El generador conserva los STEP y registra su correspondencia.

### Modelos y diseños externos reutilizados

- **RAK19007, RAK4631 y RAK1906:** modelos STEP oficiales usados como referencias/representaciones de componentes. Fuentes: [RAK19007](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK19007.stp), [RAK4631](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK4631.stp) y [RAK1906](https://downloads.rakwireless.com/3D_File/WisBlock/3D_RAK1906.stp). Descargas y procedencia en [descargas-oficiales.json](diseño-3d/fusion/componentes-nodo/descargas-oficiales.json).
- **Heltec V3:** [STEP oficial V3.7](https://resource.heltec.cn/download/WiFi_LoRa_32_V3/3D/HTIT-WB32LAF_V3.7%283%29.step), utilizado como referencia CAD; la unidad física de la estación es V3.2. No se confunden ambas revisiones.
- **LILYGO T3 V1.6:** [archivo T3_V1.6_3D.7z](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/blob/master/dimensions/T3_V1.6_3D.7z), del que se extrajo el [STEP candidato](diseño-3d/step/README.md). Referencia histórica; no identifica automáticamente las unidades de A2.
- **Envolventes dimensionales:** las fuentes de BMS, convertidor, antena, panel y otros componentes están en [fuentes-modelos.json](diseño-3d/fusion/componentes-nodo/fuentes-modelos.json). Las medidas aportadas por el equipo prevalecen sobre referencias comerciales diferentes. Se conservan las condiciones de los fabricantes; la atribución no asigna una licencia propia a sus modelos.

### Configuración y referencias de diseño

- **MeshChile:** [guía de configuración de nodos](https://meshchile.cl/node-configuration), aplicada a los [perfiles YAML](firmware/config/): ANZ, LONG_FAST, slot 20 y canal LongFast. Los perfiles del proyecto usan `CLIENT_MUTE`; el almacenamiento y el ACK se realizan en el computador.
- **Escudos de radiación multiplato:** [YOUNG](https://www.youngusa.com/product/multi-plate-radiation-shield/) y [BARANI](https://www.baranidesign.com/faq-articles/2022/6/6/how-to-design-a-solar-radiation-shield-for-weather-station-temperature-sensors-3cjb7), referencias de separación, ventilación y protección. No son validaciones térmicas del Gill V7.
- **Costos de componentes:** fuentes y criterios de comparación en [cotizaciones](hardware/cotizaciones.md) y [BOM](hardware/bom-materiales.json). Las referencias de precio no sustituyen la identidad del hardware real.

## Uso de Inteligencia Artificial

Se utilizó asistencia de OpenAI para programación, análisis técnico y documentación. Todas las solicitudes se realizaron con el modelo **GPT 6.1 sol**. La descripción de comprensión explica el mecanismo del código.

### 1. Adaptación Meshtastic del RAK: sensor y botón SOS

- **Herramienta:** OpenAI, asistencia de programación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Adapta Meshtastic v2.7.26 para un RAK4631 nRF52840/SX1262, base RAK19007 y sensor RAK1906/BME680. Conserva las API y la telemetría del firmware oficial. Implementa un módulo de aplicación para un pulsador normalmente abierto entre AIN1/P0.31 y GND con INPUT_PULLUP: muestreo no bloqueante, antirrebote de 40 ms, pulsación mantenida de 2 s y una alerta por pulsación. Inhibe la activación si arranca pulsado hasta liberarlo. Envía un texto SOS dirigido a un NodeID configurable, con identificador de evento estable entre intentos. Limita a tres intentos separados por 60 s y acepta únicamente un ACK de registro cuyo origen, destino, canal y evento coincidan. Expón WAITING, REGISTERED y UNCONFIRMED en logs, sin LED ni buzzer externos. Integra el módulo mediante un overlay reproducible con commits fijados y evita el conflicto con Dropzone en AIN1.»
- **Adaptación:** módulo `CerroSeguroModule`, máquina de estados y protocolo `CS1`; pin y destino parametrizados en `prepare.py`. El RAK del banco usa como estación `!849c7328`.
- **Comprensión técnica:** el filtrado del pulsador y los temporizadores avanzan sin bloquear la radio. Los reintentos conservan el evento pero emplean paquetes diferentes. El ACK de aplicación confirma registro persistente en la estación; no equivale al ACK nativo ni a atención humana.
- **Archivos:** [firmware/meshtastic/](firmware/meshtastic/), [pruebas C++](firmware/tests/).

### 2. Adaptador Meshtastic USB, telemetría y ACK persistente

- **Herramienta:** OpenAI, asistencia de programación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Implementa en Python una estación de monitoreo conectada por USB a una placa de 915 MHz con Meshtastic oficial, usando SerialInterface y los eventos de PyPubSub. Autoriza una lista explícita de NodeID RAK y valida origen, destino, canal y formato de cada SOS. Persiste alertas y una cola de ACK en una transacción SQLite antes de emitir la confirmación; deduplica por nodo/evento, pero vuelve a confirmar duplicados. Conserva los ACK pendientes al reiniciar y reintenta errores USB con espera creciente. Decodifica telemetría protobuf, guarda captura y recepción por separado junto con RSSI/SNR y rechaza valores no finitos. Solicita datos ambientales cada 120 s sin bloquear SOS, manteniendo independiente la publicación automática del firmware. Separa transporte, protocolo, almacenamiento y sondeo, y prueba el flujo con radios y bases temporales.»
- **Adaptación:** el receptor inicial previsto como LILYGO se concretó en Heltec V3.2; las responsabilidades de persistencia, sondeo y confirmación permanecen en el computador. La base conserva histórico, eventos y cola pendiente.
- **Comprensión técnica:** guardar antes de confirmar impide reconocer un registro que no se escribió. La clave única evita alertas repetidas; una salida persistente permite recuperar confirmaciones después de un reinicio.
- **Archivos:** [station/](station/), [ensayo RAK/Heltec](testing/banco-rak-heltec.md).

### 3. Dashboard: frontend JavaScript, backend Python y SQLite

- **Herramienta:** OpenAI, asistencia de programación y diseño de interfaz; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Construye un dashboard local para Cerro Seguro con frontend en HTML5, CSS y JavaScript nativo, backend HTTP en Python y la base SQLite de la estación como fuente persistente. Implementa endpoints JSON, filtros por nodo y período, histórico, exportación CSV y revisión/reapertura de SOS. Muestra temperatura y humedad, estadísticas del rango, tendencia, antigüedad del dato y estado USB mediante heartbeat; dibuja las gráficas con SVG y adapta la interfaz a escritorio y móvil. Actualiza la pantalla cada 5 s sin abrir el puerto serie desde el navegador ni detener la recepción al cerrar la página. Mantén independientes el ACK encolado y la revisión humana. Valida fechas, nodos y números, parametriza SQL y limita consultas. Sirve archivos y API desde 127.0.0.1:8765 sin CDNs. Conserva UTC en almacenamiento/exportaciones y presenta fechas en America/Santiago.»
- **Adaptación:** frontend y API ajustados al esquema real de SQLite, intervalos de banco, métricas disponibles y flujo SOS del proyecto. El estado del operador se guarda separado del protocolo de radio.
- **Comprensión técnica:** el navegador consulta la API y renderiza respuestas; el backend consulta SQLite sin ocupar el USB. El sondeo del sensor y la actualización visual tienen cadencias distintas. La antigüedad evita interpretar como reciente un valor antiguo.
- **Archivos:** [dashboard/server.py](dashboard/server.py), [dashboard/data.py](dashboard/data.py), [frontend](dashboard/static/).

### 4. Script de inicio conjunto para macOS

- **Herramienta:** OpenAI, asistencia de programación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Crea un comando de inicio para macOS que prepare un entorno Python local si falta, detecte el puerto del receptor Heltec y levante la estación USB y el dashboard. Enumera puertos con pySerial, diferencia Heltec/CP210x del USB nativo del RAK y exige selección explícita si existen varios candidatos. Usa por defecto el RAK !1630f9c9, canal 0, sondeo de 120 s, dashboard en 8765 y la misma base SQLite para ambos procesos. Resuelve rutas desde la raíz aunque se invoque desde otra carpeta. Espera el esquema de base antes del servidor y su respuesta HTTP antes de abrir el navegador. Captura Ctrl+C/SIGTERM y cierra únicamente los procesos iniciados; si uno falla, cierra su compañero. Informa puertos ocupados sin detener servicios anteriores y permite consultar puertos sin abrir las radios.»
- **Adaptación:** `iniciar.sh` prepara el entorno y delega la supervisión en Python; las opciones permiten cambiar puerto USB, puerto web, base, nodo e intervalo. Los servicios existentes quedan fuera de su cierre.
- **Comprensión técnica:** cada servicio se ejecuta en una sesión propia. El supervisor controla disponibilidad y terminación, envía señales a esos grupos y espera su cierre. Detectar un adaptador compatible no sustituye la comprobación del NodeID de radio.
- **Archivos:** [iniciar.sh](iniciar.sh), [tools/iniciar.py](tools/iniciar.py), [pruebas](tools/tests/test_iniciar.py).

### 5. Pruebas automatizadas y análisis de fallas

- **Herramienta:** OpenAI, asistencia de programación y depuración; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Diseña pruebas del flujo SOS y de la estación sin transmitir por radio. Usa un ejecutable C++ para rebotes, pulsación larga, reintentos, validación del ACK y desbordamiento de millis(). En Python, utiliza unittest, SQLite temporal y dobles de radio para demostrar que la alerta está comprometida antes del ACK, que los duplicados no crean eventos nuevos y que la cola sobrevive al reinicio. Prueba paquetes inválidos, valores no finitos, nodos ajenos, sondeo, consultas de dashboard, CSV y revisión humana persistente. Para el iniciador verifica puertos ambiguos, arranque parcial, fallo de un proceso y cierre con Ctrl+C. Distingue las pruebas sintéticas de las mediciones físicas y documenta diagnóstico, corrección y comprobación de las fallas observadas.»
- **Adaptación:** casos concretos de `CS1`, esquema SQLite, perfiles MeshChile, API local y supervisión de procesos. El diagnóstico de contactos públicos y cadencia se conserva separado de las averías históricas de energía.
- **Comprensión técnica:** los dobles permiten provocar errores y comprobar invariantes de persistencia/validación. Aprobar esas pruebas no mide alcance, autonomía ni precisión ambiental; los resultados físicos tienen registros independientes.
- **Archivos:** [firmware/tests/](firmware/tests/), [station/tests/](station/tests/), [dashboard/tests/](dashboard/tests/), [tools/tests/](tools/tests/), [registro de fallas](testing/registro-fallas.md).

### 6. Organización del repositorio y auditoría documental

- **Herramienta:** OpenAI, asistencia de análisis y documentación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Revisa los documentos E1, A2 y la pauta del Avance 3 junto con los README y archivos del repositorio. Organiza firmware, estación, dashboard, hardware, diseño 3D, testing y documentación con enlaces relativos verificables. Relaciona cada criterio de evaluación con sus entregables y evidencias; separa implementación, pruebas automatizadas, resultados físicos comunicados y pendientes documentales. Consolida decisiones y alternativas descartadas sin inventar fechas, asistentes, mediciones ni logs ausentes. Identifica información faltante y actualiza reporte, requisitos y checklist con los datos confirmados. Mantén la procedencia de documentos y modelos y distingue referencias históricas del montaje final.»
- **Adaptación:** organización y trazabilidad de Cerro Seguro; incorporación de los nombres de la portada de E1, material final PLA, panel 12 V/25 W y resultados reportados por el equipo. Las fechas de ensayo no se deducen de la fecha de actualización documental.
- **Comprensión técnica:** una matriz de requisitos relaciona criterio, archivo y evidencia. Mantener separados antecedentes, implementación y aceptación permite reconocer qué respalda cada afirmación sin convertir una tarea pendiente en un resultado.
- **Archivos:** [README](README.md), [verificación](docs/verificacion-avance3.md), [requisitos](docs/requisitos.md), [reporte](docs/reporte-final.md), [actas](docs/avances/actas-y-decisiones.md).

### 7. Orden y análisis de ideas y alternativas de integración

- **Herramienta:** OpenAI, asistencia de análisis técnico y documentación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Estructura las alternativas de integración estudiadas para un nodo LoRa modular: placas comerciales, PCB base, PCB con microcontroladores y varios transmisores, gestión de energía y BMS, y una antena compartida mediante switching RF. Compara complejidad de hardware/firmware, coordinación de radios, riesgos de pérdida de paquetes, verificabilidad y plazo de fabricación del PCB. Documenta qué opciones se analizaron y por qué se descartaron o postergaron usando los antecedentes del equipo. Diferencia una hipótesis de riesgo de una pérdida medida y no describas como fabricado un circuito que quedó en análisis. Relaciona estas decisiones con el prototipo comercial finalmente utilizado.»
- **Adaptación:** se registró el descarte de la antena compartida por posible pérdida de paquetes y la postergación de placas integradas por complejidad y plazo. Las pruebas de antena se citan mediante el informe A2 y capturas disponibles.
- **Comprensión técnica:** comparar alternativas permite justificar el alcance viable del prototipo. La posibilidad de perder paquetes durante una conmutación no equivale a haber construido y ensayado un conmutador RF.
- **Archivos:** [actas y decisiones](docs/avances/actas-y-decisiones.md), [selección de componentes](hardware/seleccion-componentes.md), [caracterización de antenas](testing/antenas-avance2.md).

### 8. Automatización CAD y generación de planos

- **Herramienta:** OpenAI, asistencia de programación y documentación técnica; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Organiza el montaje Gill con los componentes del nodo y las dimensiones confirmadas, distinguiendo modelos oficiales de envolventes representativas. Conserva las fuentes y genera exportaciones revisables del ensamble y sus piezas. Para los planos, escribe un generador Python con CadQuery/OCP que lea los STEP V7, obtenga vistas ortogonales y cotas de envolvente de los sólidos exactos, y utilice ReportLab para hojas A3 con escalas, cartelas, inventario y objetivos de tolerancia. Exporta además SVG editables y una correspondencia de archivos fuente. Representa la interconexión de módulos en dos hojas eléctricas, sin presentarla como una PCB fabricada. Mantén la geometría fuente y comprueba legibilidad, dimensiones y ausencia de solapamientos tras renderizar.»
- **Adaptación:** conjunto V7 y once tipos de pieza, veinte piezas impresas, margen nominal de 75 mm y componentes de la BOM; doce hojas mecánicas y dos eléctricas. Las medidas reales y la aceptación funcional del encaje se incorporaron sin atribuir tolerancias metrológicas no medidas.
- **Comprensión técnica:** la proyección muestra geometría existente; la discretización de curvas afecta al dibujo, no modifica el sólido. Las cotas y escalas del plano se distinguen de una medición del componente impreso.
- **Archivos:** [diseño-3d/](diseño-3d/), [generador](tools/planos/generar.py), [planos](diseño-3d/planos/README.md), [esquema](hardware/esquematicos/README.md).

### 9. BOM, referencias de costo y planilla

- **Herramienta:** OpenAI, asistencia de análisis y elaboración de planillas; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Consolida una BOM del montaje real con identificadores únicos, componente, cantidad, especificación, precio, moneda, fuente y alcance de la referencia. Busca cotizaciones comparables cuando el modelo original no esté disponible sin sustituir sus dimensiones reales. Conserva separados USD y CLP y no agregues conversiones, flete ni tributos no cotizados. Para fabricación propia cuenta únicamente el PLA utilizado: 160 g del interior y unos 300 g entre aletas y tapa, aproximadamente 460 g en total. Carga ese material una sola vez y evita repetirlo por cada tipo de pieza. Actualiza el XLSX con fórmulas de cantidad por precio y subtotales por moneda; comprueba cálculo, restauración de entradas y legibilidad.»
- **Adaptación:** 31 partidas, desglose de lotes de consumibles, referencias equivalentes identificadas y partida única de PLA. Los precios de reposición se diferencian de gastos pagados y del precio histórico del controlador.
- **Comprensión técnica:** separar monedas evita sumar magnitudes incompatibles. El material global cubre las piezas impresas; su costo no se vuelve a sumar en las filas de cada pieza. Una referencia comercial de batería no cambia el volumen medido del montaje.
- **Archivos:** [BOM.xlsx](hardware/BOM.xlsx), [datos de BOM](hardware/bom-materiales.json), [cotizaciones](hardware/cotizaciones.md).

### 10. Maquetación y conversión de Markdown a PDF

- **Herramienta:** OpenAI, asistencia de documentación y programación; modelo **GPT 6.1 sol**.
- **Prompt utilizado:** «Apoya la maquetación y conversión de documentos Markdown del proyecto a PDF con una presentación técnica coherente: jerarquía de títulos, tipografía legible, tablas, unidades, referencias y márgenes consistentes. Conserva contenido, cifras y procedencia; no completes mediciones ni atribuciones ausentes. Mantén una versión editable y comprueba el PDF rasterizado para detectar cortes, tablas desbordadas, símbolos incorrectos o páginas poco legibles. Para documentación gráfica, integra vistas y cartelas técnicas sin deformar escalas ni confundir una referencia conceptual con el montaje real.»
- **Adaptación:** apoyo a orden y presentación de documentos y exportaciones técnicas. El reporte actual se mantiene editable en Markdown; los planos y esquemas tienen generador y PDF propios. No se asigna a los PDF originales entregados por el equipo una autoría nueva por haberlos organizado.
- **Comprensión técnica:** convertir o maquetar no modifica la validez de los resultados. La inspección visual revisa la exportación; los datos y conclusiones se contrastan con sus fuentes por separado.
- **Archivos relacionados:** [reporte editable](docs/reporte-final.md), [documentación de planos](tools/planos/README.md), [planos PDF](diseño-3d/planos/Gill_V7_Planos.pdf), [esquema PDF](hardware/esquematicos/CerroSeguro_Esquematico.pdf).

## Documentación de componentes y antecedentes

Las especificaciones de fabricante son referencias técnicas, no resultados medidos del prototipo. Los antecedentes entregados por el equipo conservan su procedencia.

## Electrónica y componentes

### RAK19007 · WisBlock Base Board

- [Ficha técnica oficial de RAKwireless](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/).
- [Página del producto](https://store.rakwireless.com/products/rak19007-wisblock-base-board-2nd-gen).
- Referencia para alimentación, conectores, compatibilidad y dimensiones de la base. No atribuirle funciones de radio o sensado propias de los módulos instalados.

### RAK4631 · WisBlock Core

- [Ficha técnica oficial de RAKwireless](https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/).
- [Página del producto](https://store.rakwireless.com/products/rak4631-lpwan-node).
- Referencia para el núcleo nRF52840, transceptor SX1262 y variantes de radio. La banda, antena y configuración regional del montaje deben verificarse.
- RAK4631 y RAK4631-R comparten hardware, pero sus plataformas de firmware difieren. Confirmar la variante instalada antes de aplicar instrucciones de carga.

### RAK1906 · Sensor ambiental Bosch BME680

- [Ficha técnica oficial de RAKwireless](https://docs.rakwireless.com/product-categories/wisblock/rak1906/datasheet/).
- [Página del producto](https://store.rakwireless.com/products/rak1906-bme680-environment-sensor).
- Referencia para temperatura, humedad relativa, presión y sensado de gas; interfaz I²C y alimentación de 3,3 V.
- La salida de gas no es una medición directa de CO₂. Un índice de calidad del aire exige declarar el algoritmo y biblioteca que efectivamente se utilicen.

## Antecedentes internos disponibles

- [Avance 1 con actas](docs/avances/E1_Grupo_CerroSeguro_Con_Actas.docx): problema, alternativas de integración, metas preliminares y actas del 28 de agosto y 4 de septiembre de 2026.
- [Informe Avance 2](<docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), 25 de octubre de 2026: equipos, montaje, ensayo LoRa puro, capturas de terminal y NanoVNA, iteraciones de energía y fallas.
- [miniTarea](docs/avances/miniTarea.docx): tema y pregunta de investigación; fuente sobre parámetros regionales de LoRaWAN y cuestiones por investigar. Su referencia a LoRaWAN no significa que los ensayos LoRa puro utilicen ese protocolo.
- [Gill V1](diseño-3d/gill-v1/README.md): paquete original con fuente OpenSCAD y cinco exportaciones STL conceptuales.
- [Actas y decisiones de diseño](docs/avances/actas-y-decisiones.md): acuerdos, alternativas de integración y motivos de descarte.
