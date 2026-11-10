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

## Librerías y dependencias

Pendiente de incorporar el firmware y dashboard para registrar nombre, versión exacta, uso, URL oficial y licencia de cada dependencia. No hay un inventario de software verificado todavía.

## Código externo adaptado

Pendiente de revisar la implementación. Registrar archivo y función, fuente, adaptación realizada y prueba de validación para cada fragmento utilizado.

## Uso de Inteligencia Artificial
