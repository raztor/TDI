# Selección de componentes

La selección debe relacionar cada componente con una necesidad del problema. Los valores deben provenir de la hoja de datos de la revisión efectivamente utilizada.

| Componente y modelo | Necesidad que cubre | Rango | Precisión o resolución | Alimentación y consumo | Interfaz y compatibilidad | Justificación | Fuente |
|---|---|---|---|---|---|---|---|
| RAK19007 | Base de integración y alimentación | Base 30 × 60 mm | No aplica como sensor | USB 5 V / batería Li-ion 3,7 V nominal; consumo del conjunto por medir | 1 ranura Core, 1 IO y 4 de sensor | Integración modular; confirmar montaje y presupuesto de energía | [Ficha oficial](https://docs.rakwireless.com/product-categories/wisblock/rak19007/datasheet/) |
| RAK4631 | Procesamiento y radio | Variante de banda por confirmar | Desempeño del enlace por medir | Módulo 2,0–3,6 V; consumo según modo, pendiente de medir | nRF52840 + SX1262, WisBlock Core | Núcleo usado; justificar alcance y configuración con pruebas | [Ficha oficial](https://docs.rakwireless.com/product-categories/wisblock/rak4631/datasheet/) |
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

Se ha descrito un nodo de prueba con transmisores para 433 y 915 MHz, dos antenas, controlador solar y batería LiPo con BMS. Faltan modelos, conexiones y cantidades consolidadas. Confirmar cómo se relacionan los transmisores con el RAK4631 antes de agregarlos a la BOM para evitar duplicar componentes.

No asumir que una misma variante RAK4631 sirve para ambas bandas. Verificar compatibilidad de antena, configuración regional y límites de entrada de cada placa antes de conectar alimentación solar.
