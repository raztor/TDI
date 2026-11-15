# Arquitectura del sistema

## Implementación reportada y arquitectura prevista

Fuente histórica: [Avance 1](avances/E1_Grupo_CerroSeguro_Con_Actas.docx) y [Avance 2](<avances/Informe Avance 2 - Cerro Seguro (2).pdf>). E1 seleccionó conceptualmente un PCB base modular; A2 documenta pruebas con placas comerciales. La [nota de decisiones](avances/actas-y-decisiones.md) explica la postergación del PCB y el descarte de una antena compartida por posible pérdida de paquetes.

A2 reporta LoRa puro funcional y contiene capturas de telemetría y SOS/ACK. No reporta una red Meshtastic integrada ni persistencia y dashboard funcionando. El [PoC](avances/referencias/poc-nodo-fijo.jpeg) expresa una arquitectura objetivo y no constituye un circuito validado.

## Elementos conocidos

| Elemento | Función del componente | Decisión de implementación pendiente |
|---|---|---|
| RAK19007 | Base WisBlock: alimentación e interconexión | Montaje, revisión y alimentación efectiva |
| RAK4631 | Núcleo nRF52840 con transceptor SX1262 | Variante de banda, firmware y modo de comunicación |
| RAK1906 / BME680 | Sensado ambiental | Variables usadas, período de captura y procesamiento |
| Dos LILYGO LoRa32 | Radios separadas para pruebas en 433 y 915 MHz según A2 | Revisión exacta, firmware y configuración de cada ensayo |
| Heltec Wireless Tracker y V3 | Equipos disponibles para desarrollar la red | Integración y roles efectivos no acreditados |
| Solar, controlador, LiPo 3S, BMS y DC-DC | Alimentación reportada en A2 | Modelos, ajustes, ruta eléctrica y autonomía verificada |

RAK aparece como equipo utilizado en el relato de A2; el montaje de caja fotografiado contiene LILYGO. No se representa todo el inventario como si formara un único circuito simultáneo. Detalle en [inventario histórico](../hardware/inventario-historico.md).

Las capacidades de la hoja de datos no implican que todas estén implementadas. El BME680 no mide CO₂ directamente; cualquier índice derivado requiere especificar algoritmo y condiciones.

## Recorrido de una medición

1. Sensor: A2 muestra temperatura, humedad y presión en terminal; procedencia original, frecuencia y validación pendientes.
2. Firmware: A2 muestra identificador y secuencia; código, versión, reloj y gestión de errores reproducible no aportados.
3. Transporte: LoRa puro ensayado cualitativamente; configuración exacta y recuperación de cortes pendientes. Meshtastic previsto para la etapa siguiente.
4. Persistencia: servicio o archivos, esquema e histórico, pendientes.
5. Procesamiento: indicadores, ventanas y umbrales, pendientes.
6. Dashboard: acceso, actualización y estados de datos, pendientes.
7. Usuario: excursionistas y operadores de puntos fijos definidos preliminarmente en E1; receptor operativo, respuesta y utilidad por validar.

El [diagrama conceptual de E1](avances/referencias/arquitectura-e1.png) muestra sensor/botón, PCB unificado, repetidor, receptor/registro y confirmación de recepción. No es el esquema construido. Falta el diagrama del montaje real con puntos de almacenamiento efectivamente implementados.

## Configuración técnica

| Parámetro | Valor | Justificación |
|---|---|---|
| Intervalo de muestreo | Pendiente | Pendiente |
| Intervalo de transmisión | Pendiente | Pendiente |
| Banda, variante de módulo y antena | LILYGO separadas 433/470 y 868/915 MHz; dipolo usado para 433 y Laird para 915 según A2. RAK por confirmar | Frecuencia efectiva de ensayo, revisión y compatibilidad por verificar |
| Protocolo y formato del mensaje | LoRa puro; capturas AMB, SOS y ACK, con identificador y secuencia | Esquema formal, código y parámetros no aportados; Meshtastic pendiente |
| Origen del reloj y zona horaria | Pendiente | Pendiente |
| Detección de muestra duplicada | Pendiente | Pendiente |
| Política ante pérdida de conexión | Pendiente | Pendiente |
| Fuente de energía y autonomía | Panel/controlador/LiPo 3S/BMS/DC-DC reportados; sin autonomía medida aportada | Controlador inicial sustituido; ajustes y verificación final pendientes |

## Repositorio de datos

- Tecnología y versión: pendiente.
- Ubicación o endpoint sin secretos: pendiente.
- Esquema, campos, tipos y unidades: pendiente.
- Identificación del nodo y de cada muestra: pendiente.
- Retención, consulta y exportación del histórico: pendiente.
- Integridad ante reinicios, reintentos y duplicados: pendiente.
- Permisos y configuración local necesaria: pendiente.

## Límites y recuperación

Documentar qué datos se pierden o retienen durante una falla, cómo se informa al usuario y cuándo una medición deja de considerarse actual. Verificar con las pruebas T02, T03 y T05 del [protocolo](../testing/protocolo-pruebas.md).
