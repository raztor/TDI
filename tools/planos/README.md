# Generación de planos

Desde la raíz del repositorio, con Python 3.12:

```sh
python3 -m venv /tmp/tdi-planos
/tmp/tdi-planos/bin/pip install -r tools/planos/requirements.txt
/tmp/tdi-planos/bin/python tools/planos/generar.py
```

Produce el PDF mecánico de doce hojas, sus SVG y la correspondencia de STEP en `diseño-3d/planos/`; también el PDF eléctrico de dos hojas y sus SVG en `hardware/esquematicos/`. Para regenerar solo electricidad, añadir `--electrico`.

ReportLab genera los PDF; CadQuery/Open CASCADE proyecta la geometría STEP. No modifica los sólidos ni los archivos Fusion. Las cotas funcionales de detalle se declaran en el generador y se contrastan con la fuente V7; actualizar ambas si cambia el diseño. La [documentación CadQuery](https://cadquery.readthedocs.io/en/latest/importexport.html#exporting-svg) describe la proyección y exportación de vistas.

Abrir cada hoja después de regenerar para revisar escalas, cotas, fijaciones y legibilidad. La comprobación geométrica no sustituye el ensayo de impresión. El esquema eléctrico representa interconexión de módulos; no genera una PCB ni ejecuta ERC.
