# Firmware

El [Avance 2](<../docs/avances/Informe Avance 2 - Cerro Seguro (2).pdf>), página física 7, reporta ensayos con firmware de LoRa puro y contiene capturas de TX/RX ambiental y SOS/ACK. El código utilizado no se ha aportado: esta carpeta no contiene firmware ejecutable. Por indicación del equipo, esta revisión usa solo lo documentado en el informe.

## Antecedentes del firmware de prueba

Las capturas muestran temperatura en °C, humedad en % y presión en hPa, identificador de nodo, secuencia y estado CRC. La secuencia SOS muestra descarte de un pulso breve, pulsación sostenida de 2 segundos, envío y confirmación ACK. Esto documenta el flujo presentado en A2, sin probar su implementación reproducible ni una tasa de entrega, latencia, persistencia o fiabilidad de emergencia.

El informe identifica RAK19007/RAK4631/RAK1906 y dos LILYGO LoRa32 de bandas distintas. Las fotos de la caja corresponden a LILYGO; no se deduce de ellas el montaje de RAK. Meshtastic es la integración objetivo posterior, no el protocolo usado en estos ensayos.

## Entorno reproducible

| Parámetro | Valor |
|---|---|
| Placa y revisión | RAK19007 + RAK4631 y LILYGO LoRa32 reportados en A2; revisión y programa por equipo pendientes |
| Microcontrolador | nRF52840 en RAK4631 según A2; variante concreta de LILYGO por confirmar |
| IDE o herramienta de compilación y versión | Pendiente |
| Paquete de soporte de placa y versión | Pendiente |
| Archivo de entrada del programa | Pendiente |
| Bibliotecas y versiones | Pendiente; registrar en [FUENTES.md](../FUENTES.md) |
| Puerto y velocidad del monitor serial | Pendiente |

## Organización

- `src/`: módulos del firmware; separar adquisición, conexión, persistencia y lógica de indicadores según la implementación.
- [libraries/](libraries/README.md): dependencias locales solo cuando corresponda; preferir un manifiesto de versiones reproducible.

Si se usa Arduino IDE, conservar la relación de nombre entre carpeta de sketch y archivo `.ino`. Si se usa PlatformIO, incluir su `platformio.ini` real. No mantener dos configuraciones que no se prueben.

## Configuración

Documentar las variables necesarias, su significado, unidad y valor por defecto: pines, sensores, intervalo de captura, zona horaria, endpoint de datos y estrategia de reconexión. Los secretos deben configurarse localmente en archivos excluidos de Git; publicar únicamente un archivo de ejemplo sin credenciales.

## Compilación y carga

1. Instalar las versiones de herramientas indicadas arriba.
2. Instalar las dependencias declaradas.
3. Preparar la configuración local y verificar conexiones y alimentación con el [esquemático](../hardware/esquematicos/README.md).
4. Compilar con el procedimiento exacto de la plataforma elegida.
5. Cargar en la placa y comprobar la primera medición válida.

**Comando de compilación:** no consignado en A2. **Procedimiento de carga:** no consignado. **Resultado de compilación en esta revisión:** no ejecutado; no se aportó código.

También faltan frecuencia central exacta por ensayo, SF, BW, CR, potencia, parámetros de trama, biblioteca y versión. El informe explica que deben coincidir entre emisor y receptor, pero no fija sus valores. No se infieren desde las capturas NanoVNA.

## Comportamiento a documentar

- Frecuencia de muestreo y relación con el fenómeno medido.
- Validación de rango, valores ausentes y errores del sensor.
- Unidades, marcas de tiempo e identificador del dispositivo.
- Recuperación de fallas de red y de alimentación, sin duplicar o perder datos silenciosamente.
- Formato de mensajes y destino del histórico.
- Indicadores derivados, umbrales y límites de interpretación.

Comentar decisiones técnicas y manejo de errores. Enlazar las [pruebas](../testing/protocolo-pruebas.md) que verifican cada módulo.
