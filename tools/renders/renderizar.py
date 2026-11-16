"""blender --background --factory-startup --python tools/renders/renderizar.py

Render geométrico del diseño exterior y del interior sin envolvente.
Lee las mallas incluidas; no requiere Fusion ni los STEP oficiales descargados.
"""
from pathlib import Path
import argparse
import sys
import gzip
import json
import math
import bpy
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--entrada',type=Path,default=ROOT/'diseño-3d/renders/gill-v7-75mm')
parser.add_argument('--salida',type=Path,default=ROOT/'diseño-3d/renders/gill-v7-75mm')
args=parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
OUT=args.salida
OUT.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=64
scene.cycles.use_denoising=True
scene.render.resolution_x=2000
scene.render.resolution_y=2200
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.world.use_nodes=True
background=scene.world.node_tree.nodes.get('Background')
background.inputs['Color'].default_value=(.55,.6,.65,1)
background.inputs['Strength'].default_value=.12
scene.view_settings.view_transform='AgX'


def mat(name,color,metal=0,rough=.38):
    m=bpy.data.materials.new(name)
    m.diffuse_color=(*color,1)
    m.use_nodes=True
    bs=m.node_tree.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value=(*color,1)
    bs.inputs['Metallic'].default_value=metal
    bs.inputs['Roughness'].default_value=rough
    return m


materials={n:mat(n,c,m,r) for n,c,m,r in [
    ('pla',(.032,.04,.046),0,.48),('asa',(.84,.86,.85),0,.28),
    ('battery',(.025,.027,.03),0,.4),('rubber',(.018,.022,.026),0,.53),
    ('metal',(.42,.46,.49),.8,.28),('ivory',(.7,.74,.72),0,.35),
    ('blue',(.018,.15,.34),0,.4),('pcb',(.025,.075,.055),0,.5),
    ('screen',(.035,.1,.12),.15,.23),('red',(.48,.025,.025),0,.42)]}
exterior=[]
with gzip.open(args.entrada/'mallas.json.gz','rt') as f:
    data=json.load(f)
print(f'Importando {len(data)} mallas',flush=True)
for p in data:
    mesh=bpy.data.meshes.new(p['name'])
    mesh.from_pydata([[c/1000 for c in v] for v in p['vertices']],[],p['faces'])
    mesh.update()
    obj=bpy.data.objects.new(p['name'],mesh)
    scene.collection.objects.link(obj)
    obj.data.materials.append(materials[p['material']])
    # Aristas planas conservadas: no se suavizan caras funcionales ni taladros.
    if p['exterior']:
        exterior.append(obj)

bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.0002))
bpy.context.object.data.materials.append(mat('Fondo',(.63,.69,.7),0,.7))


def aim(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()


for name,loc,power,size in [('Principal',(.45,-.4,.65),4.5,.48),('Relleno',(-.4,-.1,.35),2,.4),('Contorno',(.1,.4,.55),5,.3)]:
    light=bpy.data.lights.new(name,'AREA');light.energy=power;light.shape='DISK';light.size=size
    obj=bpy.data.objects.new(name,light);scene.collection.objects.link(obj);obj.location=loc;aim(obj,(0,0,.12))
camera_data=bpy.data.cameras.new('Camara')
camera=bpy.data.objects.new('Camara',camera_data)
scene.collection.objects.link(camera)
scene.camera=camera
camera_data.type='ORTHO';camera_data.ortho_scale=.43;camera_data.lens=50
camera.location=(.43,.7,.43)
aim(camera,(0,0,.15))
for name,hide,target,scale in [
    ('gill_v7_exterior_diseno.png',False,(0,0,.155),.43),
    ('gill_v7_interior_render.png',True,(0,0,.115),.36),
]:
    for obj in exterior:obj.hide_render=hide
    aim(camera,target);camera_data.ortho_scale=scale
    scene.render.filepath=str(OUT/name)
    print(f'Renderizando {name}',flush=True)
    bpy.ops.render.render(write_still=True)
print('Renders exterior e interior terminados')
