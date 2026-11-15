# Fuentes del proyecto

Documentación de los componentes electrónicos confirmados de Cerro Seguro. Las especificaciones del fabricante no son resultados de medición del prototipo.

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
- [Inventario de aportes](docs/avances/inventario-aportes.csv): nombres originales, rutas, hashes y duplicados. Las [decisiones retrospectivas](docs/avances/actas-y-decisiones.md) identifican las aclaraciones del equipo del 15 de noviembre de 2026.

## Librerías y dependencias

Pendiente de incorporar el firmware y dashboard para registrar nombre, versión exacta, uso, URL oficial y licencia de cada dependencia. No hay un inventario de software verificado todavía.

## Código externo adaptado

Pendiente de revisar la implementación. Registrar archivo y función, fuente, adaptación realizada y prueba de validación para cada fragmento utilizado.

## Uso de Inteligencia Artificial
