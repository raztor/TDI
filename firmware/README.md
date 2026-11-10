# Firmware

Código del dispositivo que realiza las mediciones reales. La implementación está pendiente; esta carpeta no contiene firmware ejecutable.

## Entorno reproducible

| Parámetro | Valor |
|---|---|
| Placa y revisión | Pendiente |
| Microcontrolador | Pendiente |
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

**Comando de compilación:** pendiente. **Comando o procedimiento de carga:** pendiente. **Resultado de compilación:** no ejecutado.

## Comportamiento a documentar

- Frecuencia de muestreo y relación con el fenómeno medido.
- Validación de rango, valores ausentes y errores del sensor.
- Unidades, marcas de tiempo e identificador del dispositivo.
- Recuperación de fallas de red y de alimentación, sin duplicar o perder datos silenciosamente.
- Formato de mensajes y destino del histórico.
- Indicadores derivados, umbrales y límites de interpretación.

Comentar decisiones técnicas y manejo de errores. Enlazar las [pruebas](../testing/protocolo-pruebas.md) que verifican cada módulo.
