# Dashboard y repositorio de datos

**Estado:** plataforma, implementación y acceso pendientes.

## Acceso y ejecución

| Parámetro | Valor |
|---|---|
| Plataforma y versión | Pendiente |
| URL accesible o comando local | Pendiente |
| Requisitos de ejecución | Pendiente |
| Puerto local, si corresponde | Pendiente |
| Archivo de configuración o exportación | Pendiente |
| Fuente de los datos | Pendiente |
| Repositorio persistente e histórico | Pendiente |
| Período de actualización | Pendiente |
| Zona horaria | Pendiente |

## Instalación

1. Incorporar el código, exportación o configuración reproducible de la plataforma elegida.
2. Documentar dependencias y versiones en [FUENTES.md](../FUENTES.md).
3. Indicar la configuración local necesaria sin publicar secretos.
4. Documentar el comando de inicio o la URL de acceso.
5. Comprobar la conexión con el dispositivo y la consulta del histórico.

## Información visible

- Última medición válida y su marca temporal.
- Gráficas en tiempo real e histórico, con unidades y ejes identificados.
- Indicadores, estadísticas o alertas definidos en [indicadores](../docs/indicadores.md).
- Estado de conexión y aviso de datos antiguos o ausentes.
- Contexto para interpretar tendencias y decidir una acción.

## Persistencia

Registrar esquema de datos, unidades, zona horaria, política de retención y método para exportar o consultar el histórico en [arquitectura](../docs/arquitectura.md). Si se usan CSV, describir su estructura y organización. Una pantalla en tiempo real no acredita persistencia.

## Evidencias de funcionamiento

Guardar capturas o exportaciones en [testing/evidencias/](../testing/evidencias/README.md) y datos reales en [testing/datos/](../testing/datos/README.md). Mostrar el dashboard operando en vivo durante la evaluación; las capturas sirven de respaldo, no reemplazan la demo.
