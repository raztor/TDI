# Cierre funcional del prototipo

Actualización: **16 de noviembre de 2026**. Resultados comunicados por el equipo del proyecto. Esta fecha corresponde al registro; las fechas y condiciones concretas de cada ensayo se completarán en sus actas.

## Montaje y energía

El equipo comprobó la correspondencia de los terminales con el [esquema](../hardware/esquematicos/README.md), la salida del convertidor, la suficiencia del consumo y la autonomía del conjunto. La generación diurna repone por completo la energía consumida durante la noche y deja excedente de generación. El montaje final se considera satisfactorio.

La recuperación diurna se refiere al balance energético del ciclo día/noche. No significa que el estado de carga de la batería supere el 100 %. No se han informado valores de corriente, energía en Wh, duración exacta ni reserva porcentual, por lo que no se asignan cifras a esas magnitudes. La suficiencia funcional está confirmada; el objetivo específico de reserva del 30 % no está cuantificado.

El BMS queda aceptado respecto de las conexiones del esquema. Su modelo comercial y sus umbrales internos no se deducen de esa comprobación. El panel utilizado es de **12 V / 25 W**, y el RAK se alimenta a través del DC-DC USB de **5 V nominales**.

## Comunicación

| Magnitud | Resultado reportado |
|---|---:|
| Mensajes enviados | 20 |
| Mensajes recibidos | 20 |
| Recepción observada | 100 % |
| Mensajes perdidos | 0 |
| Pérdidas observadas | 0 % |
| Tiempo de entrega | Todos inferiores a 60 s |
| Latencia | Baja según observación del equipo; sin serie de tiempos informada |

El ensayo satisface las metas de al menos 9/10 entregas y menos de 60 s en las condiciones probadas. Los veinte mensajes no se distribuyen por puntos ni distancias sin un registro que lo indique. La media, máximo exacto y percentil 95 de latencia no se calculan sin los tiempos individuales. Las dos diferencias WAITING–REGISTERED de 2,955 s y 2,583 s del [banco del 15 de noviembre](banco-rak-heltec.md) son una evidencia separada, no la distribución de estos veinte envíos.

No se atribuye al ensayo cobertura general en montaña, ni una medición de precisión meteorológica o una validación de uso con excursionistas. Esos alcances requieren antecedentes propios.

## Fabricación y ajuste

La impresión se realizó por el equipo en **PLA**, con aproximadamente **160 g utilizados en el interior**. La impresora había sido calibrada recientemente. El equipo confirmó encaje satisfactorio y tolerancias suficientes para el interior impreso. La tapa y las aletas no se fabricaron por indisponibilidad de ASA; se descartó imprimirlas en PLA para exposición solar. La estimación anterior de unos 300 g exteriores no corresponde a consumo realizado.

Se cierra la comprobación funcional de encaje del interior; no se declara comprobado el ajuste físico de la envolvente exterior. No se convierten esa observación ni la calibración de la impresora en desviaciones dimensionales medidas. Los objetivos nominales de los [planos](../diseño-3d/planos/README.md) se conservan como referencia de diseño.

El costo de fabricación propia incluye únicamente el filamento utilizado. A la referencia de **CLP 13.000/kg**, los **0,160 kg** equivalen a **CLP 2.080**. Se registra una sola vez en BOM-031; las piezas interiores no vuelven a cobrar material y la envolvente no fabricada no tiene consumo imputado. No se agrega servicio de impresión, mano de obra ni energía.

## Evidencias y datos que faltan para las actas

- Fotografías del interior: tres vistas incorporadas en [hardware/fotos](../hardware/fotos/README.md). La envolvente exterior no fue fabricada.
- Fecha, lugar, participantes y responsables de las pruebas de comunicación, energía y montaje.
- La serie de veinte distancias y SNR está incorporada en [pruebas de distancia](pruebas-distancia.md); no consta su correspondencia individual con los veinte envíos cronometrados. Obstáculos, ubicación y condiciones no figuran en la tabla; indicar si fueron mensajes de prueba, SOS o ambos, y qué punto del recorrido se cronometró.
- Duración del ensayo energético y condiciones de sol/carga. Incorporar lecturas si existen; no reconstruir cifras que no fueron registradas.
- Fecha de impresión y montaje, piezas intervenidas, decisiones de integración y responsables.
- Confirmación del ensayo de apertura, reemplazo o reinstalación y recuperación funcional, distinto del encaje satisfactorio.

Estos datos completan la trazabilidad de las pruebas ya reportadas. Los resultados funcionales no se vuelven a presentar como pruebas aún no realizadas.

## Serie de distancia y SNR

Se incorporan [20 lecturas](pruebas-distancia.md) entre 0,2 y 17,4 km, con SNR de −9,0 a 13,2 dB. El punto de 17,4 km registra −0,5 dB. Se conserva la imagen original, la transcripción CSV y la gráfica. Esta serie se documenta por separado del resultado 20/20 bajo 60 s: no contiene tiempos, conteo de pérdidas por punto ni saltos de red.
