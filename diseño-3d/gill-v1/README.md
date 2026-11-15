# Escudo Gill V1 de Cerro Seguro

Paquete aportado por el equipo el 15 de noviembre de 2026, conservado sin modificaciones. El ZIP contiene fechas internas del 10 de noviembre; no se utilizan como prueba de fabricación ni se atribuye el diseño al cierre de octubre.

## Archivos disponibles

- [ZIP original](CerroSeguro_Gill_CAD_V1.zip).
- [Fuente paramétrica OpenSCAD](CerroSeguro_Gill_V1.scad).
- [Instrucciones originales](LEEME.txt).
- Cinco STL: [lama](louver_V1.stl), [techo](roof_V1.stl), [base](base_V1.stl), [bandeja](sensor_tray_V1.stl) y [soporte de pared](wall_bracket_V1.stl).

La fuente permite seleccionar `assembly`, `louver`, `roof`, `base`, `sensor_tray` o `wall_bracket` mediante `part`. Su disponibilidad no acredita apertura o renderizado en OpenSCAD; no se ejecutó un ensayo de fabricación en esta revisión documental.

## Parámetros declarados

Valores en milímetros, provisionales según el propio código: diámetro exterior de lama 112, apertura central 60, siete lamas con paso 14, base de diámetro 94 y espesor 5, tres varillas M4 en círculo de 83 y agujeros de 4,5. La bandeja supone una placa de 25 × 25 con holgura de 1; no son medidas verificadas del RAK1906.

## Limitaciones conocidas

El LEEME advierte que la bandeja no tiene anclajes específicos para la PCB ni conexión mecánica a la base. Faltan medir el sensor y su conector, definir cableado, fijaciones y separación de la caja, comprobar ventilación y drenaje y realizar piezas de prueba. ASA blanco es una recomendación de material, no evidencia de impresión.

Este conjunto es un escudo ambiental conceptual, no el gemelo completo del nodo. No incluye una representación integrada de placas, batería y electrónica, planos acotados, renders finales ni un ensamble `.f3d`/`.f3z`. No se acredita ajuste, resistencia exterior ni funcionamiento del sensor dentro del escudo.

Los [STL Ruuvi](../stl/gill/README.md) ya existentes son referencias de terceros distintas de esta V1. Sus condiciones y atribuciones se conservan en su carpeta. Los hashes de los aportes figuran en [inventario de aportes](../../docs/avances/inventario-aportes.csv).
