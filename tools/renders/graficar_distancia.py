"""Gráfica de la transcripción de las pruebas de distancia/SNR (Matplotlib)."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
rows=list(csv.DictReader((ROOT/'testing/datos/distancia-snr.csv').open()))
colors={'Muy buena':'#24766c','Buena':'#2685ad','Moderada':'#bd8126','Baja':'#a14c54'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(11,5.8),layout='constrained')
fig.patch.set_facecolor('#f8fafb');ax.set_facecolor('#f8fafb')
for quality,color in colors.items():
    group=[r for r in rows if r['calidad_orientativa']==quality]
    ax.scatter([float(r['distancia_km']) for r in group],[float(r['snr_db']) for r in group],s=65,c=color,label=quality,edgecolors='white',linewidths=1,zorder=3)
offsets={1:(-15,9),2:(-16,-15),3:(6,8),4:(8,-2),5:(7,5),6:(-14,-17),7:(7,-17),8:(-18,-15),9:(7,5),10:(5,8),11:(5,-15),12:(-24,-16),13:(-23,8),14:(-28,3),15:(10,5),16:(-25,-16),17:(6,-15),18:(6,12),19:(10,-15),20:(7,8)}
for r in rows:
    n=int(r['prueba']);ax.annotate(str(n),(float(r['distancia_km']),float(r['snr_db'])),xytext=offsets[n],textcoords='offset points',fontsize=9,color='#314954',arrowprops=dict(arrowstyle='-',color='#a5b1b7',lw=.5))
ax.axhline(0,c='#82929b',ls='--',lw=.8)
ax.set(xlabel='Distancia (km)',ylabel='SNR (dB)',xlim=(-.6,19),ylim=(-12,16))
ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
ax.set_title('Cerro Seguro · Recepción a distancia',loc='left',fontweight='bold',fontsize=17,pad=20)
ax.legend(loc='upper right',frameon=False,title='Clasificación de la tabla original')
fig.text(.015,-.035,'20 lecturas · Etiquetas = número de prueba · Categorías orientativas; sin inferir pérdidas ni cobertura continua.',fontsize=10,color='#536973')
for ext in ('png','svg'):
    fig.savefig(ROOT/f'testing/evidencias/distancia-snr-grafica.{ext}',dpi=180,bbox_inches='tight')
svg=ROOT/'testing/evidencias/distancia-snr-grafica.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
plt.close(fig)
