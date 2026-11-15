# Inventario histórico del Avance 2

Fuente: [informe A2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), tabla 2 y fotografías. Distingue equipos utilizados, disponibles, retirados y propuestos. No sustituye el inventario físico actual ni una BOM cotizada.

| Equipo | Estado reportado en A2 | Evidencia y dato pendiente |
|---|---|---|
| RAK19007 + RAK4631 | Utilizados como nodo principal | Identificado en A2; las imágenes RAK son referenciales. Confirmar cantidad, revisión y banda instalada |
| RAK1906 / BME680 | Utilizado como sensor | A2 muestra valores ambientales en terminal, sin serie original. Cantidad y configuración pendientes |
| LILYGO LoRa32 868/915 MHz TCXO | Radio de prueba para 915 MHz | Una visible en la foto interior horizontal; revisión exacta pendiente |
| LILYGO LoRa32 433/470 MHz | Radio de prueba para 433 MHz | Una visible junto a la anterior; revisión exacta pendiente |
| Heltec Wireless Tracker y Heltec V3 | Disponibles para desarrollo de red | No se acredita retransmisión mesh ni cantidad total |
| Dipolo de aluminio | Construido para 433 MHz | Foto en A2 y captura NanoVNA; dimensiones pendientes |
| Antena Laird Connectivity | Utilizada en 915 MHz | Foto y captura; modelo y especificaciones exactas pendientes |
| Morningstar SunSaver-20 | Controlador inicial retirado de esa configuración | Sustituido tras desconexiones prematuras; no contarlo como controlador final |
| Controlador blanco/azul | Sustituto utilizado | A2 lo describe para LiPo 3S; faltan modelo y comprobación de ajustes |
| Batería LiPo 3S y BMS | Alimentación reportada, tres celdas en serie | Capacidad, modelo del BMS, ajustes y estado actual pendientes |
| Módulo DC-DC con USB | Regulación del montaje fotografiado | Modelo, tensión medida, corriente y eficiencia pendientes |
| Panel solar, caja, soporte, coaxiales y conectores | Elementos de instalación reportados | Modelos, dimensiones, cantidades y especificaciones pendientes |
| NanoVNA y equipos de banco | Utilizados para caracterización y ensayos | Modelo y trazabilidad de calibración pendientes |
| Batería LiPo hinchada | Retirada y descartada | No contar como batería operativa; causa sin determinar |
| Placa LILYGO averiada | Daño reportado | Identificar unidad y si está incluida en las placas fotografiadas antes de consolidar cantidades |
| Botón protegido, LED, buzzer y escudo Gill en ASA | Arquitectura prevista | El flujo SOS/ACK aparece en A2; no acredita por sí solo el montaje físico completo de esos elementos |

## Consolidación pendiente en BOM.xlsx

La [BOM](BOM.xlsx) contiene solo tres referencias RAK, sin cantidades ni costos. Falta trasladar el inventario confirmado, con revisión, cantidad realmente disponible, especificación, precio, moneda y fuente. Dos placas visibles en una foto no establecen el total de equipos del proyecto ni cuántos siguen operativos.

El PoC propone panel de 24 V / 25 W, controlador MPPT y conversión a 5 V / 3,3 V. Son valores de una arquitectura de referencia: el informe no los confirma como especificaciones medidas del montaje. La especificación eléctrica definitiva requiere contrastarlos con el montaje.
