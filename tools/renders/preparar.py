"""Teselar los STEP V7 y referencias comerciales para los renders.

python tools/renders/preparar.py --rak-assets /ruta/a/STEP-oficiales
Los tres STEP RAK deben coincidir con descargas-oficiales.json.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import cadquery as cq

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'diseño-3d/fusion/gill-v7-75mm'
REF = ROOT / 'diseño-3d/fusion/componentes-nodo'
OUT = ROOT / 'diseño-3d/renders/gill-v7-75mm'
parts, sources = [], {}


def load(path):
    sources[str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return cq.importers.importStep(str(path)).val()


def add(name, shape, material, exterior=False):
    vertices, faces = shape.tessellate(.12, .15)
    parts.append(dict(name=name, material=material, exterior=exterior,
                      vertices=[[round(v.x, 4), round(v.y, 4), round(v.z, 4)] for v in vertices],
                      faces=[list(f) for f in faces]))


def box(name, xyz, size, mat, offset):
    shape = cq.Solid.makeBox(*size, cq.Vector(*xyz)).translate(offset)
    add(name, shape, mat)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rak-assets', type=Path, required=True)
    parser.add_argument('--salida', type=Path, default=OUT)
    args = parser.parse_args()
    for entry in json.loads((REF/'descargas-oficiales.json').read_text()):
        if not entry['file'].startswith('RAK'):
            continue
        assert hashlib.sha256((args.rak_assets/entry['file']).read_bytes()).hexdigest() == entry['sha256'], entry['file']

    add('Base', load(SRC/'V4_Base_200_Sin_Varillas.step'), 'pla')
    guide = load(SRC/'V7_Guia_T_235_5_Tope_y_Inserto_Axial.step')
    for a in (0, 120, 240):
        add(f'Guia {a}', guide.rotate((0,0,0),(1,1,1),120).translate((92,0,4)).rotate((0,0,0),(0,0,1),a), 'pla')
    fin = load(SRC/'V7_Aleta_236_45gr_Paso23_5.step')
    for i in range(8):
        add(f'Aleta {i+1}', fin.translate((0,0,12+i*23.5)), 'asa', True)
    for name, z in [('V7_Aleta_Superior_236_45gr',200),('V7_Tapa_256_Pendiente8gr',235.5),('V7_Disco_Antena_60_Paso16_2',249.5)]:
        add(name, load(SRC/(name+'.step')).translate((0,0,z)), 'asa', True)
    add('Placa vertical', load(SRC/'V3_Placa_Vertical_154.step').rotate((0,0,0),(1,0,0),90).translate((0,-3,4)), 'pla')
    for name,z in [('Controlador',11),('DCDC',53),('RAK',95),('BMS',151)]:
        add('Bandeja '+name, load(SRC/f'V3_Bandeja_{name}.step').translate((0,0,z)), 'pla')
    battery = load(REF/'modelos/04_Bateria_Medida_120x50x40.step')
    # Coordenadas locales (x,y,z) -> (y,z,x): 120 mm en vertical.
    battery = battery.rotate((0,0,0),(1,1,1),-120).translate((-25,-49.5,8))
    add('Bateria medida 120x50x40', battery, 'battery')
    antenna = load(REF/'modelos/09_Laird_TRAB9023P_Montaje_Panel.step').translate((0,0,252.5))
    for i, solid in enumerate(antenna.Solids()):
        add(f'Antena {i}', solid, 'rubber' if solid.BoundingBox().zlen>40 else 'metal', True)

    # Mismas envolventes y posiciones de las referencias del ensamble Fusion.
    off=(-30,-1,14.8)
    box('GC carcasa', (0,0,0), (60,60,14), 'ivory', off)
    box('GC frente', (1,1,14), (58,28,1), 'blue', off)
    box('GC LCD', (13,34,14.4), (34,20,.6), 'screen', off)
    for i in range(6):
        add(f'GC borne {i}', cq.Solid.makeCylinder(2.5,.4,cq.Vector(7+i*9.2,8,14.6)).translate(off), 'metal')
    off=(-31.5,10,59.5)
    box('DC PCB', (0,0,0), (63,27,1.6), 'blue', off)
    for name,xyz,size,mat in [('USB',(49,1,1.6),(14,13,6),'metal'),('Jack',(0,1,1.6),(12,9,8.4),'rubber'),('Inductor',(33,2,1.6),(12,12,7),'metal'),('Borne1',(1,19,1.6),(10,7,8),'blue'),('Borne2',(52,19,1.6),(10,7,8),'blue')]:
        box('DC '+name,xyz,size,mat,off)
    for x in (17,43):
        add(f'DC condensador {x}',cq.Solid.makeCylinder(3.5,8.4,cq.Vector(x,22,1.6)).translate(off),'metal')
    # BMS representativo protegido; el modelo físico bajo cinta no está identificado.
    box('BMS protegido referencia',(-29.5,-31,154.5),(59,20,3.4),'red',(0,0,0))
    for filename,delta in [('RAK19007.stp',(0,0,0)),('RAK4631.stp',(56.958,20.447,3.2114)),('RAK1906.stp',(34.25,6.5995,3.2114))]:
        shape=load(args.rak_assets/filename)
        for i,solid in enumerate(shape.Solids()):
            b=solid.BoundingBox()
            material='pcb' if b.xlen*b.ylen>80 and b.zlen<2 else ('metal' if max(b.xlen,b.ylen)>7 else 'rubber')
            add(f'{filename} {i}',solid.translate(delta).translate((-30,10,103.5)),material)
    out=args.salida
    out.mkdir(parents=True,exist_ok=True)
    with gzip.GzipFile(filename=str(out/'mallas.json.gz'),mode='wb',mtime=0) as f:
        f.write(json.dumps(parts,separators=(',',':')).encode())
    (out/'fuentes-render.json').write_text(json.dumps({'unidades':'mm','teselacion_mm':.12,'fuentes_sha256':sources,'alcance':'Piezas STEP V7 exactas teseladas; electrónica comercial de referencia. Exterior completo no fabricado. Interior impreso: 160 g PLA.','objetos':len(parts),'herramientas':{'CadQuery':'2.8.0','Blender':'5.1.2'},'renderizado':{'motor':'Cycles','muestras':64,'resolucion_px':[2000,2200]},'scripts_sha256':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [Path(__file__).resolve(),ROOT/'tools/renders/renderizar.py']}},ensure_ascii=False,indent=2)+'\n')
    print(f'{len(parts)} mallas exportadas')


if __name__ == '__main__':
    main()
