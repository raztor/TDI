# Renders y gráfica de distancia

## Renders CAD

Herramientas utilizadas: **Blender 5.1.2**, **CadQuery 2.8.0**. Python de Blender ejecuta el render; CadQuery solo es necesario para volver a teselar. No se modifica el diseño STEP ni se escala la electrónica para hacerla encajar.

Desde la raíz del repositorio, con Blender en el PATH:

```sh
blender --background --factory-startup --python tools/renders/renderizar.py
```

En macOS con Blender instalado en Aplicaciones:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python tools/renders/renderizar.py
```

Salida: dos PNG de 2000 × 2200, exterior completo e interior sin envolvente, en `diseño-3d/renders/gill-v7-75mm/`. Lee las mallas versionadas y no necesita Fusion ni descargar modelos. Ciclos de 64 muestras con reducción de ruido, materiales Principled BSDF, tres luces de área y cámara ortográfica. El exterior claro es el diseño previsto; no se fabricó. El interior representa los soportes impresos con 160 g de PLA.

### Volver a generar las mallas

Instalar `tools/planos/requirements.txt`. Descargar los tres STEP RAK indicados en `diseño-3d/fusion/componentes-nodo/descargas-oficiales.json` a una carpeta propia. Se comprueba su SHA-256 antes de procesarlos:

```sh
python tools/renders/preparar.py --rak-assets /ruta/a/STEP-oficiales
```

La teselación usa tolerancia de 0,12 mm y conserva las transformaciones del ensamble de `tools/planos/generar.py`. Base, guías, bandejas, placa, aletas, tapa, disco, batería y antena proceden de los STEP del proyecto. El conjunto RAK usa geometría oficial RAK19007/4631/1906. Controlador GC y DC-DC se reconstruyen con las mismas formas nominales de referencia del inventario CAD; el BMS es un volumen representativo protegido, sin modelo físico identificado. Se excluyen cables y herrajes de presentación. `fuentes-render.json` registra las fuentes, hashes y alcance.

## Gráfica de pruebas a distancia

Python y **Matplotlib 3.11.2**:

```sh
python tools/renders/graficar_distancia.py
```

Lee `testing/datos/distancia-snr.csv` y escribe PNG y SVG. Conserva todos los registros, identifica cada punto por número de prueba y utiliza las categorías originales. No aplica ajustes, interpolación ni infiere tasas de pérdidas. La metodología y límites están en `testing/pruebas-distancia.md`.

Fuentes de herramientas: [Blender](https://www.blender.org/), [CadQuery](https://github.com/CadQuery/cadquery), [Matplotlib](https://matplotlib.org/).
