# Información e indicadores

Los indicadores relacionan el nodo fijo con dos necesidades del Avance 1: consultar condiciones locales y comunicar una alerta a una estación. Se calculan con datos reales persistidos. Los resultados de banco no representan toda una ruta ni acreditan aptitud para rescate.

| Indicador | Datos y cálculo | Ventana y umbral | Decisión apoyada | Límites |
|---|---|---|---|---|
| Temperatura y humedad actuales | Última lectura válida, °C y % HR; mostrar su hora de recepción | Última muestra, incluso al cambiar el rango del gráfico | Consultar las condiciones del punto medido | Sin calibración contra referencia; el calor del montaje puede influir |
| Tendencia de temperatura | Media, mínima, máxima y última menos primera muestra | Período seleccionado; variación requiere al menos dos muestras del mismo nodo | Reconocer cambios y contrastarlos con el entorno antes de planificar una actividad | Sin umbrales meteorológicos de seguridad ni extrapolación de pronóstico |
| Antigüedad del dato | Hora actual menos hora UTC de recepción | Aviso tras 3 × intervalo esperado: 360 s para el sondeo de 120 s | Revisar alimentación y radio antes de usar una lectura antigua | Puede existir recepción intermitente; no identifica por sí sola la causa |
| Estado de la estación | Estado USB y edad del heartbeat del servicio | Heartbeat cada 5 s; actualización de más de 15 s deja de acreditar conexión activa | Revisar el servicio y el USB cuando el nodo deja de actualizarse | El USB conectado no demuestra enlace RF |
| SOS por revisar | Conteo de eventos únicos sin revisión humana | Registro completo del nodo, independiente del rango ambiental | Abrir el evento y coordinar la atención según el procedimiento del proyecto | Guardar o revisar no significa activar ni completar un rescate |
| Confirmación de registro | Estado persistente de la cola de ACK | Pendiente o encolado después del commit | Distinguir almacenamiento de la entrega al radio | Solo el RAK puede confirmar su estado REGISTERED; no se infiere del encolado |
| Intervalo observado | Mediana de diferencias de recepción entre muestras del mismo nodo | Período seleccionado; al menos dos muestras | Detectar cambios de cadencia y revisar vacíos en el histórico | No es pérdida de paquetes: pueden coexistir respuestas solicitadas y publicaciones automáticas |

## Frecuencia de banco

El BME680 observa variables que cambian en una escala de minutos en el ensayo interior. Solicitar una lectura cada 120 s permite observar tendencias sin emitir una lectura de radio por cada consulta del navegador. El dashboard consulta cada 5 s para reflejar con rapidez la recepción de un SOS. La generación del SOS es independiente del sondeo ambiental.

La cadencia de 120 s es una elección de banco; su costo energético y el tráfico de una campaña prolongada requieren medición. No prueba la reserva energética objetivo de E1. El firmware oficial conserva su mínimo de publicación automática de 1800 s en el canal público utilizado.

## Variables no interpretadas como indicadores

La resistencia de gas no se presenta como calidad del aire, concentración de contaminantes ni riesgo para la salud. Tampoco se usa la presión para calcular altitud o pronosticar condiciones. La interfaz principal limita las unidades ambientales a temperatura y humedad, cuya representación se comprobó con los paquetes recibidos. Validación y precisión física son aspectos distintos.
