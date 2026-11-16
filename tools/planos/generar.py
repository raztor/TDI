"""Planos de conjunto/piezas derivados de los STEP Gill V7 y esquema de módulos.

Ejecutar desde la raíz: python tools/planos/generar.py
Dependencias: cadquery 2.8, reportlab 5.1. Unidades de dibujo: mm.
"""
from pathlib import Path
import sys
from math import sin, cos, radians
import hashlib
import json
import html
import cadquery as cq
from OCP.HLRBRep import HLRBRep_Algo, HLRBRep_HLRToShape
from OCP.HLRAlgo import HLRAlgo_Projector
from OCP.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCP.BRepLib import BRepLib
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.GCPnts import GCPnts_QuasiUniformDeflection
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'diseño-3d/fusion/gill-v7-75mm'
OUT = ROOT / 'diseño-3d/planos'
ELEC = ROOT / 'hardware/esquematicos'
MM = 72 / 25.4
NAVY, GRAY, BLUE, RED = '#183449', '#667782', '#176c91', '#a33529'


class Sheet:
    def __init__(self, pdf, path, title, number, count, code, scale):
        self.pdf, self.path, self.svg = pdf, path, []
        self.rect(8, 8, 404, 281)
        self.text(15, 20, 'CERRO SEGURO', 5, NAVY, True)
        self.text(15, 29, title, 4.5, NAVY, True)
        self.text(405, 20, code, 4, NAVY, True, 'end')
        self.line(8, 35, 412, 35)
        self.line(8, 268, 412, 268)
        self.text(14, 276, 'Rev. C | 16-11-2026 | Unidades: mm | Formato A3', 3)
        self.text(14, 284, 'Imprimir al 100 %. No medir sobre una copia ajustada al papel.', 2.7, GRAY)
        self.text(405, 276, f'Escala {scale} | Hoja {number}/{count}', 3, NAVY, False, 'end')
        self.text(405, 284, 'Gill V7 / documentación de prototipo', 2.7, GRAY, False, 'end')

    def line(self, x1, y1, x2, y2, color=NAVY, width=.2, dash=False):
        self.poly([(x1, y1), (x2, y2)], color, width, dash)

    def poly(self, pts, color=NAVY, width=.2, dash=False):
        if len(pts) < 2:
            return
        c = self.pdf
        c.setStrokeColor(HexColor(color)); c.setLineWidth(width*MM)
        c.setDash([1.3*MM, .9*MM] if dash else [])
        p = c.beginPath(); p.moveTo(pts[0][0]*MM, (297-pts[0][1])*MM)
        for x, y in pts[1:]: p.lineTo(x*MM, (297-y)*MM)
        c.drawPath(p)
        coords = ' '.join(f'{x:.4f},{y:.4f}' for x, y in pts)
        dashattr = ' stroke-dasharray="1.3 .9"' if dash else ''
        self.svg.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"{dashattr}/>')

    def rect(self, x, y, w, h, color=NAVY, width=.2):
        self.poly([(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],color,width)

    def circle(self, x, y, r, color=NAVY):
        self.poly([(x+r*cos(radians(a)), y+r*sin(radians(a))) for a in range(0,361,5)],color)

    def text(self, x, y, value, size=3, color=NAVY, bold=False, align='start'):
        c=self.pdf; c.setFillColor(HexColor(color)); c.setFont('Helvetica-Bold' if bold else 'Helvetica',size*MM)
        f={'start':c.drawString,'middle':c.drawCentredString,'end':c.drawRightString}[align]
        f(x*MM,(297-y)*MM,str(value))
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{align}" fill="{color}">{html.escape(str(value))}</text>')

    def notes(self, title, lines, x=302, y=48, size=2.8, pitch=4.7):
        self.text(x,y,title,3.3,NAVY,True)
        y+=7
        for t in lines:
            self.text(x,y,t,size,GRAY); y+=pitch
        return y

    def dimh(self,x1,x2,y,label,edge=None):
        if edge is not None:
            for x in (x1,x2): self.line(x,edge,x,y+2,GRAY,.12)
        self.line(x1,y,x2,y,GRAY,.12)
        for x,d in ((x1,1),(x2,-1)):
            self.line(x,y,x+d*2,y-0.7,GRAY,.12); self.line(x,y,x+d*2,y+.7,GRAY,.12)
        self.text((x1+x2)/2,y-1.5,label,2.8,align='middle')

    def dimv(self,y1,y2,x,label,edge=None):
        if edge is not None:
            for y in (y1,y2): self.line(edge,y,x+2,y,GRAY,.12)
        self.line(x,y1,x,y2,GRAY,.12)
        for y,d in ((y1,1),(y2,-1)):
            self.line(x,y,x-.7,y+d*2,GRAY,.12); self.line(x,y,x+.7,y+d*2,GRAY,.12)
        self.text(x+2,(y1+y2)/2,label,2.8)

    def finish(self):
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297">\n'+'\n'.join(self.svg)+'\n</svg>\n')
        self.pdf.showPage()


VIEWS = {
    'PLANTA': ((0,0,1),(1,0,0)),
    'ALZADO': ((0,-1,0),(1,0,0)),
    'PERFIL DERECHO': ((1,0,0),(0,1,0)),
    'ISOMETRICA': ((1,-1,1),(1,1,0)),
}


def project(shape, name):
    norm, axis = VIEWS[name]
    hlr=HLRBRep_Algo(); hlr.Add(shape.wrapped)
    hlr.Projector(HLRAlgo_Projector(gp_Ax2(gp_Pnt(),gp_Dir(*norm),gp_Dir(*axis))))
    hlr.Update(); hlr.Hide(); out=HLRBRep_HLRToShape(hlr)
    paths=[]
    for hidden, compounds in [(True,[out.HCompound(),out.OutLineHCompound()]),(False,[out.VCompound(),out.Rg1LineVCompound(),out.OutLineVCompound()])]:
        for compound in compounds:
            if compound.IsNull(): continue
            BRepLib.BuildCurves3d_s(compound,1e-6)
            for e in cq.Shape(compound).Edges():
                adaptor=BRepAdaptor_Curve(e.wrapped)
                d=GCPnts_QuasiUniformDeflection(adaptor,.035)
                if not d.IsDone(): raise RuntimeError('No se pudo discretizar una curva')
                pts=[(d.Value(i).X(),d.Value(i).Y()) for i in range(1,d.NbPoints()+1)]
                paths.append((hidden,pts))
    b=shape.BoundingBox()
    exact={
      'PLANTA':(b.xmin,b.ymin,b.xmax,b.ymax),
      'ALZADO':(b.xmin,b.zmin,b.xmax,b.zmax),
      'PERFIL DERECHO':(b.ymin,b.zmin,b.ymax,b.zmax),
    }
    if name in exact:
        bounds=exact[name]
    else:
        pts=[p for _,ps in paths for p in ps]
        bounds=(min(x for x,y in pts),min(y for x,y in pts),max(x for x,y in pts),max(y for x,y in pts))
    return paths,bounds


def draw_view(s, paths, cx, cy, scale, label, dimensions=False):
    paths,(x0,y0,x1,y1)=paths
    mx,my=(x0+x1)/2,(y0+y1)/2
    for hidden,ps in paths:
        s.poly([(cx+(x-mx)*scale,cy-(y-my)*scale) for x,y in ps],GRAY if hidden else NAVY,.1 if hidden else .22,hidden)
    s.text(cx,cy+(y1-y0)*scale/2+17,label,2.8,NAVY,True,'middle')
    if dimensions:
        s.dimh(cx-(x1-x0)*scale/2,cx+(x1-x0)*scale/2,cy-(y1-y0)*scale/2-8,f'{x1-x0:.2f}',cy-(y1-y0)*scale/2)
        s.dimv(cy-(y1-y0)*scale/2,cy+(y1-y0)*scale/2,cx+(x1-x0)*scale/2+8,f'{y1-y0:.2f}',cx+(x1-x0)*scale/2)


PARTS=[
 ('V4_Base_200_Sin_Varillas','Base inferior',1,.5,[
  'Disco: diam. 200 x 4. Origen: centro.',
  '3 encajes T a 0 / 120 / 240 grados.',
  'Radio de cara interior T: 91,75.',
  'T hembra: alma 2,90 x 12,50;',
  'cabeza 4,10 x 8,50. Paso libre.',
  'Cajeados de pies: 10,4 x 4,4.',
  'X inicial: -34,2 / 23,8; Y=-7,2.',
  'Ventanas (X,Y; ancho x alto):',
  '(-31,12; 62 x 41), R3',
  '(-62,-16; 18 x 48), R3',
  '(44,-16; 18 x 48), R3',
  '(-30,-79; 60 x 12), R3',
  'Paso diam.10: centro (50,45).',
  'Ranuras 7 x 3,2, eje Y:',
  'centros (+/-31,76).',
  'Apoyo bateria: ver STEP; no perforar.',
  'Suplementos llegan a Z12.',
 ]),
 ('V7_Guia_T_235_5_Tope_y_Inserto_Axial','Guia T y tope',3,.5,[
  'Longitud total: 235,5.',
  'Cuerpo recto hasta Y233,5.',
  'T macho: ala 12 x 2,4;',
  'alma 8 x 3,6. Espesor total 6.',
  'Tope: ancho16 x largo18 x alto10,2.',
  'Tope entre Y8 e Y26.',
  'Piloto inferior diam.3,9:',
  'centro X0,Y4; fondo Z1,2.',
  'Boca diam.4,5 en Z6,1.',
  'Piloto axial superior diam.3,9:',
  'eje X0,Z3; fondo Y229,3.',
  'Punta conica: largo2;',
  'diametros 5,0 / 4,6.',
  'Dos insertos M3 L4 por guia.',
  'No confundir con probeta antigua.',
  'Imprimir acostada sobre ala T.',
 ]),
 ('V7_Aleta_236_45gr_Paso23_5','Aleta estandar',8,.5,[
  'Exterior diam.236; hueco diam.180.',
  'Pendiente nominal: 45 grados.',
  'Espesor vertical: 2,4.',
  'Espesor normal aprox.: 1,70.',
  'Ancho radial util: 28.',
  'Altura del perfil inclinado: 30,4.',
  'Altura total con collar: 41,5.',
  '3 collares a 0 / 120 / 240 grados.',
  'Collar: X90,5..102,5; Y +/-9.',
  'Collar en Z18..41,5.',
  'Paso entre piezas: 23,5.',
  'Perfil T hembra: holgura 0,25/lado.',
  'Anillo apoyo: diam.236 / 231,2;',
  'espesor 2,4. Apoya en cama.',
 ]),
 ('V7_Aleta_Superior_236_45gr','Aleta terminal',1,.5,[
  'Exterior diam.236; hueco diam.180.',
  'Pendiente nominal: 45 grados.',
  'Espesor vertical: 2,4.',
  'Perfil inclinado igual al estandar.',
  'Altura total: 35,5.',
  'Collar en Z18..35,5.',
  '3 collares a 0 / 120 / 240 grados.',
  'Collar: X90,5..102,5; Y +/-9.',
  'T hembra: holgura 0,25/lado.',
  'Montaje: Z200; cara final Z235,5.',
  'No intercambiar con las 8 estandar.',
 ]),
 ('V7_Tapa_256_Pendiente8gr','Tapa superior',1,.5,[
  'Exterior diam.256. Fondo plano.',
  'Borde: 3,2; subida cono: 13,8.',
  'Pendiente nominal: 8,015 grados.',
  'Rebaje disco: diam.60,5 desde Z14.',
  'Acceso inferior tuerca: diam.44.',
  '3 pilotos diam.3,9 en PCD52:',
  '60 / 180 / 300 grados, fondo Z9,2.',
  'Profundidad modelada: 5.',
  '3 pasos diam.3,6 en PCD190:',
  '0 / 120 / 240 grados.',
  'Cajeado diam.5,5 en Z2..6,2.',
  'Asientos exteriores diam.10.',
  '3 ventanas T a 0 / 120 / 240.',
  'M3x6 para disco; M3x10 a guias.',
  'Disco apoya en Z14, no en cono.',
  'Altura envolvente STEP: 16,965.',
 ]),
 ('V7_Disco_Antena_60_Paso16_2','Disco de antena',1,1,[
  'Diametro exterior: 60.',
  'Espesor: 3; caras paralelas.',
  'Paso antena central: diam.16,2.',
  '3 pasos diam.3,4 en PCD52:',
  '60 / 180 / 300 grados.',
  'Coordenadas de centros:',
  '(13;22,517), (-26;0),',
  '(13;-22,517). Origen central.',
  'Holgura con tapa: 0,25 radial.',
  'Tres M3x6; tuerca propia antena.',
  'Probar paso con probeta de antena.',
  'Sellar junta y pasos al montar.',
 ]),
 ('V3_Placa_Vertical_154','Placa vertical',1,.5,[
  'Cuerpo: 78 x 154 x 4.',
  'Pies bajan hasta Y=-4.',
  'Pies: 10 x 4; X=-34 / 24.',
  'Sobrerrelieves hasta Z6.',
  'Ventanas: ancho36, R3, X=-18.',
  'Y inicial / alto:',
  '15/14; 45/19; 88/21; 120/17.',
  '8 pasos baldas: 8,4 x 3,4.',
  'X inicial=-29,2 / 20,8.',
  'Centros Y=8,5;50,5;92,5;148,5.',
  '4 ranuras 7 x 3,2, eje Y:',
  'centros X +/-27,5; Y38 / 80.',
  'Montaje: pie en base a Z4.',
  'Ventanas y guias libres de rebabas.',
 ]),
 ('V3_Bandeja_Controlador','Bandeja de controlador',1,1,[
  'Placa: ancho68, Y=-3..62.',
  'Espesor 3; tabs atras hasta Y=-7.',
  'Tabs: 8 x 4; X=-29 / 21.',
  'Ventana40 x 28, R3:',
  'esquina inferior (-20,15).',
  '4 retenes: 1,5 x 10 x 3.',
  'X inicial=-32,1 / 30,6;',
  'Y inicial=10 / 40.',
  'Tope frontal: 40 x 1 x 3,',
  'esquina (-20,-2,6,Z3).',
  'Controlador GC: 60 x 60 x 15.',
  'Montaje bandeja: Z11.',
 ]),
 ('V3_Bandeja_DCDC','Bandeja de convertidor',1,1,[
  'Placa: ancho70, Y=-3..40.',
  'Espesor3; tabs atras hasta Y=-7.',
  'Tabs: 8 x 4; X=-29 / 21.',
  'Ventana48 x 19, R3:',
  'esquina (-24,14).',
  '4 ranuras7 x 3,2, eje X:',
  'centros X +/-23; Y6,5 / 39.',
  'Retenes: 63 x 1,5 x 3;',
  'X=-31,5, Y10 / 35,5.',
  'Modelo DC-DC candidato XY-3606;',
  'validar conectores con unidad real.',
  'Montaje bandeja: Z53.',
 ]),
 ('V3_Bandeja_RAK','Bandeja de WisBlock',1,1,[
  'Placa: ancho70, Y=-3..43.',
  'Espesor3; tabs atras hasta Y=-7.',
  'Tabs: 8 x 4; X=-29 / 21.',
  'Ventana40 x 15, R3:',
  'esquina (-20,16).',
  '4 apoyos4 x 4 x 5:',
  'X=-28 / 24; Y12 / 34; Z3.',
  'Los apoyos no tienen taladros.',
  'Retencion final por verificar;',
  'no se especifica rosca adicional.',
  'Montaje bandeja: Z95.',
  'Conservar acceso USB y pulsador.',
 ]),
 ('V3_Bandeja_BMS','Bandeja de BMS',1,1,[
  'Placa: ancho68, Y=-37..-7.',
  'Espesor3. Tabs en Y=-7..-3.',
  'Tabs: 8 x 4; X=-29 / 21.',
  'Ventana44 x 10, R2,5:',
  'esquina (-22,-25).',
  '4 ranuras7 x 3,2, eje X:',
  'centros X +/-19; Y-33,5 / -10.',
  'BMS comercial CAD es referencial.',
  'Cotejar placa real bajo cinta roja.',
  'Montaje bandeja: Z151.',
 ]),
]


def make_mechanical():
    OUT.mkdir(exist_ok=True,parents=True)
    pdf=canvas.Canvas(str(OUT/'Gill_V7_Planos.pdf'),pagesize=(420*MM,297*MM))
    pdf.setTitle('Cerro Seguro - Gill V7 - Planos de conjunto y piezas'); pdf.setAuthor('Cerro Seguro')
    cache={}; manifest=[]
    for name,title,qty,scale,notes in PARTS:
        file=SRC/(name+'.step'); shape=cq.importers.importStep(str(file)).val()
        b=shape.BoundingBox()
        cache[name]=(shape,{k:project(shape,k) for k in VIEWS})
        manifest.append({'archivo':str(file.relative_to(ROOT)),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'cantidad':qty,'envolvente_mm':{'min':[b.xmin,b.ymin,b.zmin],'max':[b.xmax,b.ymax,b.zmax]},'volumen_mm3':shape.Volume()})
        print('Proyectado',name,flush=True)
    s=Sheet(pdf,OUT/'svg/00_Conjunto.svg','Gill V7 - conjunto y montaje',1,12,'CS-M-00','1:2')
    # Proyeccion del conjunto plastico. La antena comercial no forma parte del plano de fabricacion.
    assembly=[]
    assembly.append(cache[PARTS[0][0]][0])
    guide=cache[PARTS[1][0]][0]
    # Rotacion de coordenadas locales (x,y,z) -> (z,x,y), seguida de traslacion.
    for a in (0,120,240):
        g=guide.rotate((0,0,0),(1,1,1),120).translate((92,0,4)).rotate((0,0,0),(0,0,1),a)
        assembly.append(g)
    for i in range(8): assembly.append(cache[PARTS[2][0]][0].translate((0,0,12+i*23.5)))
    assembly.append(cache[PARTS[3][0]][0].translate((0,0,200)))
    assembly.append(cache[PARTS[4][0]][0].translate((0,0,235.5)))
    assembly.append(cache[PARTS[5][0]][0].translate((0,0,249.5)))
    assembly.append(cache[PARTS[6][0]][0].rotate((0,0,0),(1,0,0),90).translate((0,-3,4)))
    for j,z in zip(range(7,11),(11,53,95,151)): assembly.append(cache[PARTS[j][0]][0].translate((0,0,z)))
    assy=cq.Compound.makeCompound(assembly)
    draw_view(s,project(assy,'ALZADO'),83,132,.5,'ALZADO / plastico',True)
    draw_view(s,project(assy,'PERFIL DERECHO'),227,132,.5,'PERFIL DERECHO',False)
    s.notes('MONTAJE Y REFERENCIAS',[
      'Base diam.200; aletas diam.236;', 'tapa diam.256; asiento Z252,5.',
      '8 aletas: Z12 + n x 23,5; n=0..7.', 'Terminal: Z200. Tapa: Z235,5.',
      'Interior mas alto: Z160,5.', 'Margen a tapa: 75,0 (nominal CAD).',
      'Montaje: 3 guias + placa + 4 baldas.', 'Sin varillas ni separadores sueltos.',
      'Tornilleria: 6 M3x6 + 3 M3x10.', 'Insertos: 9 M3 L4, exterior4,2.',
      'Antena: tuerca propia y junta.', 'Paso central16,2; referencia 5/8".',
      'Cable coaxial: volumen representativo;', 'margen CAD sobre interior: 18,5.',
      'Bateria medida: 120 x 50 x 40.', 'Interior: encaje funcional aceptado.',
      'La vista no certifica estanqueidad,', 'resistencia ni temperatura de uso.',
    ])
    s.text(15,227,'INVENTARIO DIGITAL / ESTADO DE FABRICACION',3.2,NAVY,True)
    s.text(15,234,'1 base | 3 guias | 8 aletas estandar | 1 terminal | 1 tapa | 1 disco | 1 placa | 4 bandejas = 20 piezas',2.8)
    s.text(15,241,'Interior fabricado: aprox. 160 g PLA; ajuste aceptado. Tapa, aletas y disco: diseno exterior no fabricado; ASA no disponible.',2.8)
    s.text(15,248,'Objetivos provisionales de control: lineales +/-0,3 hasta150; +/-0,5 sobre150; taladros +/-0,2; angulos +/-1 grado.',2.65)
    s.text(15,255,'No son tolerancias medidas. Probar insertos y paso de antena; no compensar el STEP sin registrar una nueva revision.',2.65)
    s.finish()
    for idx,(name,title,qty,scale,notes) in enumerate(PARTS,2):
        shape,views=cache[name]
        scale_label='1:2' if scale==.5 else '1:1'
        s=Sheet(pdf,OUT/f'svg/{idx-1:02d}_{name}.svg',title,idx,12,f'CS-M-{idx-1:02d}',scale_label)
        yc=112
        draw_view(s,views['PLANTA'],88,yc,scale,'PLANTA',True)
        draw_view(s,views['ALZADO'],88,220,scale,'ALZADO',True)
        draw_view(s,views['PERFIL DERECHO'],235,220,scale,'PERFIL DERECHO',False)
        iso_scale=.28 if scale==.5 else .48
        draw_view(s,views['ISOMETRICA'],230,107,iso_scale,'ISOMETRICA / sin escala',False)
        y=s.notes(f'CS-M-{idx-1:02d} | CANTIDAD: {qty}',notes)
        s.notes('CONTROL DE FABRICACION',[
          'Cotas de envolvente derivadas de STEP.',
          'Otras cotas nominales: fuente V7.',
          'Objetivos: ver hoja CS-M-00.',
          ('Pieza de diseno exterior; no fabricada.' if idx in (4,5,6,7) else 'Interior: encaje funcional aceptado.'),
          'Las curvas se aproximan a 0,035 mm',
          'para la representacion en papel.',
          'STEP conserva la geometria exacta.',
        ],y=max(y+8,211),pitch=4.5,size=2.6)
        s.text(15,260,'Fuente: fusion/gill-v7-75mm/'+name+'.step',2.35,GRAY)
        s.finish()
    pdf.save()
    (OUT/'correspondencia-step.json').write_text(json.dumps({'revision':'C documental; geometria V7 conservada','fabricacion':'Interior: 160 g PLA. Tapa, aletas y disco exteriores no fabricados; ASA no disponible','unidades':'mm','metodo':'Proyeccion HLR de STEP; vistas de tercer diedro; deflexion grafica 0,035 mm','piezas':manifest},indent=2,ensure_ascii=False)+'\n')


def make_electrical():
    ELEC.mkdir(exist_ok=True,parents=True)
    pdf=canvas.Canvas(str(ELEC/'CerroSeguro_Esquematico.pdf'),pagesize=(420*MM,297*MM))
    pdf.setTitle('Cerro Seguro - Esquema electrico de modulos'); pdf.setAuthor('Cerro Seguro')
    s=Sheet(pdf,ELEC/'svg/01_Alimentacion.svg','Alimentacion solar del nodo RAK',1,2,'CS-E-01','S/E')

    def box(x,y,w,h,ref,title,lines):
        s.rect(x,y,w,h)
        s.text(x+3,y+7,ref+' | '+title,3.15,NAVY,True)
        for j,t in enumerate(lines): s.text(x+3,y+13+j*4.6,t,2.7,GRAY)

    def wire(pts,color=RED,dashed=False,label=None):
        s.poly(pts,color,.5,dashed)
        if label:
            x,y=pts[0]; s.text(x+1,y-2,label,2.6,color)

    box(15,52,75,35,'PV1','Panel solar',['12 V nominal / 25 W','Envolvente CAD: 510 x 360 x 20','Referencia de costo: ACOPOWER'])
    box(128,52,114,46,'U4','Controlador PWM GC',['Etiqueta: 12 V / 10 A / Li-ion 3S','60 x 60 x 15 mm','Bornes por pictograma: PV / BAT / LOAD','Polaridades impresas en el frontal'])
    box(285,52,112,35,'U5','DC-DC USB',['Entrada desde salida LOAD','Salida USB regulada: 5 V','Referencia visual/costo: XY-3606'])
    box(285,126,112,35,'U1','RAK19007 + RAK4631',['Entrada de energia por USB-C 5 V','BAT y SOLAR de la base: sin conexion','I/O y radio: hoja CS-E-02'])
    box(128,128,114,40,'U6','BMS 3S bajo cinta roja',['Entre bateria y controlador (confirmado)','P+ / P-: puerto protegido funcional','Terminales cotejados con esquema por equipo','Modelo comercial no identificado'])
    box(15,128,75,40,'BT1','Bateria LiPo 3S',['11,1 V nominal / 12,6 V a plena carga','Envolvente medida: 120 x 50 x 40','Modelo visual: Multistar 5200 mAh','Conector de balanceo: 4 hilos'])

    # Cada par termina en un puerto identificado; no se puentea B- con P- del BMS.
    wire([(90,65),(128,65)],RED,label='PV+'); wire([(90,77),(128,77)],NAVY,label='PV-')
    wire([(242,65),(285,65)],RED,label='LOAD+')
    wire([(242,77),(285,77)],NAVY,label='LOAD-')
    wire([(167,98),(167,128)],RED,label='BAT+ <-> P+')
    wire([(207,98),(207,128)],NAVY,label='BAT- <-> P-')
    wire([(90,141),(128,141)],GRAY,True,label='C0..C3 / celdas')
    wire([(90,157),(128,157)],GRAY,True,label='Potencia bateria')
    wire([(320,87),(320,126)],RED,label='VBUS +5 V')
    wire([(369,87),(369,126)],NAVY,label='GND USB')
    s.text(15,112,'ROJO: positivo | AZUL OSCURO: retorno | GRIS DISCONTINUO: conexiones internas de celdas y potencia',2.6,GRAY)
    s.notes('CONEXIONES Y LIMITES DEL LEVANTAMIENTO',[
      'PV+/- del panel a PV+/- del GC; LOAD+/- del GC a IN+/- del DC-DC. USB-A del DC-DC al USB-C de RAK19007.',
      'BAT+/- del controlador al puerto protegido de potencia del BMS. No identificar los pads por colores o por esta posicion grafica.',
      'C0..C3 designan nodos de celda: 0 / 1 / 2 / 3 celdas acumuladas. No son numeros de pin ni una secuencia de conexion.',
      'El equipo confirmo la correspondencia de terminales y esquema. Los nombres funcionales no sustituyen la serigrafia del BMS.',
      'El BMS protege el pack; no sustituye al controlador de carga. No se acredita balanceo activo ni umbrales de corte del modelo real.',
      'Salida correcta y autonomia suficiente confirmadas por el equipo. La generacion diurna repone el consumo nocturno con excedente.',
      'No aplicar la bateria 3S a BAT de RAK19007 (1S), ni el panel de 12 V a SOLAR de RAK19007 (5 V). Ambos quedan libres.',
      'Aceptacion funcional reportada el 16-11-2026. No se informaron mA, Wh, horas exactas ni reserva porcentual; no se asignan valores.',
    ],x=15,y=190,size=2.7,pitch=6)
    s.text(15,259,'Fuente: fotos IMG_2188/2189 y IMG_2197/2198; datos de montaje confirmados; ficha RAK19007. Esquema de interconexion de modulos.',2.45,GRAY)
    s.finish()

    s=Sheet(pdf,ELEC/'svg/02_Sensor_SOS_Estacion.svg','Sensor, pulsador SOS y estacion de monitoreo',2,2,'CS-E-02','S/E')
    box(15,54,83,45,'SW1','Pulsador SOS N.A.',['Modulo S / V / G','S a AIN1; G a GND','V sin conectar','Sin alimentacion externa del modulo'])
    box(136,54,112,55,'U1','RAK19007',['J11 pin1: AIN1 / P0.31 / GPIO31','J12 pin2 o J10 pin2: GND','USB-C: 5 V desde CS-E-01','J12 pin1 VDD: 3,3 V interno','J12 pin3 SCL / pin4 SDA: bus interno'])
    box(15,140,83,35,'U3','RAK1906 / BME680',['Montado en ranura pequena trasera','Alimentacion 3,3 V e I2C por WisBlock','No conectar cables externos I2C'])
    box(136,140,112,35,'U2','RAK4631',['Core WisBlock: nRF52840 + SX1262','Radio compatible 915 MHz','Meshtastic con modulo SOS propio'])
    box(291,54,112,45,'U7','Heltec WiFi LoRa32 V3.2',['Estacion 915 MHz; firmware Meshtastic','USB-C: energia y datos desde el PC','Antena 915 MHz conectada','Sin cable GPIO hacia el nodo RAK'])
    box(291,140,112,40,'PC1','Computador de monitoreo',['USB serial -> station/main.py','Persistencia SQLite -> dashboard local','Registra SOS y emite ACK dirigido','Revision del operador separada del ACK'])
    wire([(98,68),(136,68)],BLUE,label='S / AIN1')
    wire([(98,88),(136,88)],NAVY,label='G / GND')
    wire([(98,153),(117,153),(117,103),(136,103)],BLUE,label='WisBlock I2C + 3V3 / GND')
    wire([(192,109),(192,140)],BLUE,label='Core / bus base')
    wire([(248,157),(268,157),(268,74),(291,74)],BLUE,True,label='LoRa 919,875 MHz')
    wire([(345,99),(345,140)],BLUE,label='USB datos + 5 V')
    s.circle(48,93,1.1); s.circle(67,93,1.1)
    s.line(49,93,65,89); s.line(67,93,87,93)
    s.text(15,118,'Contacto seco: INPUT_PULLUP interno. Reposo HIGH; pulsado LOW. V del modulo queda aislado.',2.65,GRAY)
    s.notes('SECUENCIA FUNCIONAL Y CONFIGURACION',[
      'Boton: rebote 40 ms, pulsacion mantenida 2 s; hasta 3 intentos separados 60 s. No se instalan LED ni buzzer externos.',
      'SOS: WAITING -> TX -> ACK de registro de la estacion -> REGISTERED en el RAK. ACK no equivale a atencion de rescate.',
      'Telemetria: el PC solicita lecturas cada 120 s. La publicacion automatica publica usa su intervalo separado de 1800 s.',
      'RAK !1630f9c9 / Heltec !849c7328. Ambos CLIENT_MUTE; ANZ / LONG_FAST / slot20 / 919,875 MHz; MQTT deshabilitado.',
      'Antenas: un puerto RF por placa, sin conmutador compartido. Latiguillo RAK al radiador 915 MHz; Heltec a su antena de kit.',
      'Las conexiones internas WisBlock son board-to-board; el esquema indica su funcion, no reproduce los circuitos de las placas.',
    ],x=15,y=198,size=2.7,pitch=6)
    s.text(15,258,'Referencias: docs.rakwireless.com / RAK19007 y RAK1906; firmware/meshtastic; testing/banco-rak-heltec.md. Sin revision ERC de PCB.',2.45,GRAY)
    s.finish(); pdf.save()


if __name__=='__main__':
    if '--electrico' in sys.argv:
        make_electrical()
    else:
        make_mechanical(); make_electrical()
