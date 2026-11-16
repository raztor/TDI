# Selección de componentes

La selección debe relacionar cada componente con una necesidad del problema. Los valores deben provenir de la hoja de datos de la revisión efectivamente utilizada.

## Decisiones de los avances anteriores

E1 comparó placas comerciales interconectadas, PCB integrado y PCB base modular; seleccionó este último como dirección conceptual. Para el prototipo de A2 se utilizaron placas comerciales. El equipo confirmó que la fabricación del PCB con varios transmisores/controladores, gestión energética y BMS se postergó por complejidad y tiempo. La antena única compartida mediante switching RF quedó en análisis y se descartó por posible pérdida de paquetes, sin fabricar circuito ni medir esa pérdida. [Actas y evolución](../docs/avances/actas-y-decisiones.md).

El [inventario histórico](inventario-historico.md) recupera los equipos utilizados, disponibles y retirados de A2. Las especificaciones de la tabla siguiente son referencias documentales existentes, no mediciones del prototipo.

| Componente y modelo | Necesidad que cubre | Rango | Precisión o resolución | Alimentación y consumo | Interfaz y compatibilidad | Justificación | Fuente |
|---|---|---|---|---|---|---|---|
| RAK19007 | Base de integración y alimentación | Base 30 × 60 mm | No aplica como sensor | USB 5 V / batería Li-ion 3,7 V nominal; consumo del conjunto por medir | 1 ranura Core, 1 IO y 4 de sensor | Integración modular; confirmar montaje y presupuesto de energía | [Ficha oficial](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/) |
| RAK4631 | Procesamiento y radio | Variante de 915 MHz comprobada en banco | Desempeño del enlace por medir | Módulo 2,0–3,6 V; consumo según modo, pendiente de medir | nRF52840 + SX1262, WisBlock Core | Núcleo usado; justificar alcance y configuración con pruebas | [Ficha oficial](https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/) |
| RAK1906 / BME680 | Telemetría ambiental | −40 a 85 °C; 0–100 % HR; 300–1100 hPa | Confirmar precisión por variable y condiciones en la ficha | 3,3 V; consumo según modo de medida | I²C, conector WisBlock | Sensor usado; vincular variables con la decisión del proyecto | [Ficha oficial](https://docs.rakwireless.com/product-categories/wisblock/rak1906/datasheet/) |

## Alimentación

- Fuente y tensión nominal: pendiente.
- Consumo en reposo y captura: pendiente de especificación y medición.
- Consumo máximo y margen de la fuente: pendiente.
- Batería, protección y autonomía, si corresponde: pendiente.
- Condiciones de operación y límites ambientales: pendiente.

## Criterios de compatibilidad

Verificar tensiones de alimentación y señal, niveles lógicos, interfaz, direcciones de bus, disponibilidad de pines, capacidad de corriente y espacio físico. Separar valores nominales del fabricante de resultados medidos en el prototipo.

Mantener cantidades y costos en [BOM.xlsx](BOM.xlsx), y fuentes de referencia en [FUENTES.md](../FUENTES.md).

## Otros elementos del nodo de prueba

A2 identifica dos LILYGO LoRa32 para 433 y 915 MHz, dipolo artesanal, antena Laird, controlador solar, LiPo 3S, BMS y DC-DC. El conjunto RAK se reporta como utilizado por separado del montaje LILYGO fotografiado. Faltan revisiones, conexiones y cantidades consolidadas; no agrupar todo como un único circuito ni duplicar radios en la BOM.

El controlador inicial SunSaver-20 se sustituyó tras desconexiones prematuras. El informe no cierra la validación de ajustes del controlador final. Las dos antenas tienen [lecturas NanoVNA documentadas](../testing/antenas-avance2.md); no prueban alcance ni ganancia.

No asumir que una misma variante RAK4631 sirve para ambas bandas. Verificar compatibilidad de antena, configuración regional y límites de entrada de cada placa antes de conectar alimentación solar.
