# Prueba de integración SOS y telemetría

**Estado:** pulsador físico, sensor y SOS/ACK ejecutados en banco; [evidencias](banco-rak-heltec.md). El [cierre funcional](cierre-funcional-avance3.md) incorpora20/20 mensajes bajo 60 s reportados por el equipo. La tabla siguiente conserva el protocolo; no implica ejecución de cada caso límite no informado.

## Preparación

- RAK4631 y LILYGO de 915 MHz, antenas compatibles y firmware/configuración registrados.
- Pulsador normalmente abierto instalado entre AIN1 de J11 pin 1 y GND de la RAK19007; GPIO 31 configurado como entrada digital.
- NodeID de la estación incorporado en el firmware del RAK y NodeID del RAK autorizado en el receptor.
- Ambos equipos configurados para MeshChile: ANZ, LongFast, slot 20 y canal primario coincidente.
- Servicio USB de estación activo con una base identificada para la campaña.
- Sensor RAK1906 reconocido por la telemetría del RAK.
- Guardar los logs de cada prueba en una carpeta de campaña con fecha, revisión, configuración y responsable.

## Casos y criterios

| Caso | Procedimiento | Resultado esperado |
|---|---|---|
| Pulsación breve | Pulsar y soltar antes de 2 s | Ningún evento SOS |
| Pulsación sostenida | Mantener al menos 2 s estables | Un evento con identificador, escritura en SQLite y respuesta `REGISTRADO` |
| Botón mantenido | Seguir manteniendo después del envío | Ningún evento adicional |
| Botón mantenido al arrancar | Encender con el botón presionado, luego liberar y volver a pulsar | Sin alerta durante el arranque; alerta solo tras la nueva pulsación válida |
| Reintentos | Mantener la estación sin servicio y generar un SOS | Máximo de intentos configurado; mismo evento y paquetes Meshtastic diferentes; estado `UNCONFIRMED` |
| Confirmación perdida | Interrumpir de forma controlada el retorno después de guardar y restaurarlo antes de un reintento | Un registro de alerta; el duplicado recibe otra confirmación |
| Almacenamiento no disponible | Ejecutar en una base de ensayo sin permisos de escritura | Sin confirmación de registro; error visible en el servicio |
| Reinicio de estación | Detener después de guardar con ACK aún pendiente y volver a iniciar | Alerta conservada y ACK pendiente recuperado |
| ACK incorrecto | Enviar en una red de ensayo un ACK de otro evento, emisor o canal | RAK permanece esperando el evento válido |
| Telemetría | Recibir al menos dos intervalos ambientales | Registros con origen, ID, unidades comprobadas y horas de captura/recepción diferenciadas |
| Reconexión USB | Desconectar y reconectar la LILYGO en el mismo puerto | Reintento de conexión; datos anteriores conservados |

El reinicio del RAK durante un SOS pendiente interrumpe ese estado en esta versión. Registrar esta limitación durante la campaña.

## Resultados por registrar

Por cada envío: identificador de evento, ID de paquete, intento, hora de envío, recepción, commit y recepción de ACK, resultado y archivos de evidencia. Para latencia, sincronizar o relacionar los relojes de ambos extremos; no restar directamente marcas de arranque del RAK y hora UTC del computador.

Verificar un primer enlace directo de banco y luego un recorrido mediante la malla disponible. La aceptación con relés de terceros requiere evidencia de ese recorrido, no solo configuración de hop limit. Registrar muestras enviadas, registradas y confirmadas, duplicados y pérdidas. El objetivo preliminar de E1 de 9/10 por punto y entrega menor a 60 s debe contrastarse con una campaña definida antes de probar.
