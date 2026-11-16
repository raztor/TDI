// Cerro Seguro Gill V7. Unidades mm. Piezas orientadas para imprimir.
// M3x6 x6, M3x10 x3, insertos M3 L4 D4.2 x9. Tuerca propia de antena.
// Tapa Z235.5; asiento plano Z252.5. Margen sobre interior: 75 mm.
hueco_antena=16.2;
part="montaje"; // [base,guia,lama,lama_superior,techo,disco_antena,probeta,probeta_antena,placa,controlador,dcdc,rak,bms,montaje]
$fn=160;
module bloque(x,y,z,w,h,t) {translate([x,y,z]) cube([w,h,t]);}
module cilindro(x,y,z,d,h) {translate([x,y,z]) cylinder(d=d,h=h);}
module ventana(x,y,w,h,r=3,t=20) {translate([x,y,-1]) hull() for(xx=[r,w-r],yy=[r,h-r]) translate([xx,yy,0]) cylinder(r=r,h=t);}
module ranura(x,y,ang=0,l=7,w=3.2,t=20) {translate([x,y,-1]) rotate([0,0,ang]) hull() for(dx=[-(l-w)/2,(l-w)/2]) translate([dx,0,0]) cylinder(d=w,h=t);}
module perfil_T(z,h,c=.25) {
 union() {bloque(92-c,-6-c,z,2.4+2*c,12+2*c,h);bloque(94.4-c,-4-c,z,3.6+2*c,8+2*c,h);}
}
module diamante(x1,x2,z,recorrido=0,lado=3.5) {
 hull() for(dz=[-recorrido/2,recorrido/2]) translate([x1,0,z+dz]) rotate([45,0,0]) translate([0,-lado/2,-lado/2]) cube([x2-x1,lado,lado]);
}
module base() {
 difference() {
  union() {
   cylinder(d=200,h=4);
   for(x=[-24,16]) bloque(x,-50,4,8,42,4);
   for(x=[-27.1,25.6]) bloque(x,-44,4,1.5,30,7);
   bloque(-20,-52,4,40,1.5,4);
   for(a=[0:120:240]) rotate([0,0,a]) difference() {
    bloque(90.5,-8,4,9,16,8);perfil_T(4,8.5);diamante(98,102,8);
   }
  }
  for(x=[-34.2,23.8]) bloque(x,-7.2,-1,10.4,4.4,6);
  for(v=[[-31,12,62,41],[-62,-16,18,48],[44,-16,18,48],[-30,-79,60,12]]) ventana(v[0],v[1],v[2],v[3],3,6);
  cilindro(50,45,-1,10,6);
  for(x=[-31,31]) ranura(x,76,90,t=6);
 }
}
module guia() {
 difference() {
  union() {
   bloque(-6,0,0,12,233.5,2.4);bloque(-4,0,2.4,8,233.5,3.6);
   translate([0,233.5,3]) rotate([-90,0,0]) cylinder(d1=5,d2=4.6,h=2);
   bloque(-8,8,0,16,18,10.2);
  }
  cilindro(0,4,1.2,3.9,5.1);
  translate([0,4,5.5]) cylinder(d1=3.9,d2=4.5,h=.6);
  translate([0,229.3,3]) rotate([-90,0,0]) cylinder(d=3.9,h=6.3);
 }
}
module cono_inferior() {translate([0,0,-.1]) cylinder(r1=118.1,r2=68,h=50.1);}
module lama(terminal=false) {
 difference() {
  union() {
   difference() {
    intersection() {cylinder(r1=120.4,r2=90,h=30.4);cilindro(0,0,-.1,236,31);}
    cono_inferior();cilindro(0,0,-1,180,50);
   }
   difference() {cylinder(r=118,h=2.4);cilindro(0,0,-.1,231.2,2.6);}
   for(a=[0:120:240]) rotate([0,0,a]) difference() {bloque(90.5,-9,18,12,18,terminal?17.5:23.5);cono_inferior();}
  }
  for(a=[0:120:240]) rotate([0,0,a]) {bloque(90.5,-9,-1,12,18,19);perfil_T(-1,64);}
 }
}
module techo_fisico() {
 difference() {
  union() {
   cylinder(r=128,h=3.2);translate([0,0,3.2]) cylinder(r1=128,r2=30,h=13.8);
   for(a=[0:120:240]) rotate([0,0,a]) cilindro(95,0,3.2,10,5.4);
  }
  cilindro(0,0,-1,44,20);cilindro(0,0,14,60.5,5);
  for(a=[0:120:240]) rotate([0,0,a]) {perfil_T(-.1,3.7);cilindro(95,0,2,5.5,4.2);cilindro(95,0,-1,3.6,12);}
  for(a=[60:120:300]) rotate([0,0,a]) cilindro(26,0,9.2,3.9,5);
 }
}
module techo() {techo_fisico();}
module disco_antena() {
 difference() {
  cylinder(d=60,h=3);cilindro(0,0,-1,hueco_antena,5);
  for(a=[60:120:300]) rotate([0,0,a]) cilindro(26,0,-1,3.4,5);
 }
}
module probeta() {
 difference() {
  cube([60,30,6]);
  for(i=[0:2]) cilindro(10+i*20,8,1.2,3.8+i*.1,5.1);
  translate([25-92,22,0]) perfil_T(-1,8);
 }
}
module balda(w,frente,atras=-3) {
 union() {
  bloque(-w/2,atras,0,w,frente-atras,3);
  for(x=[-29,21]) bloque(x,-7,0,8,4,3);
 }
}
module controlador() {
 union() {
  difference() {balda(68,62);ventana(-20,15,40,28,3,5);}
  for(x=[-32.1,30.6],y=[10,40]) bloque(x,y,3,1.5,10,3);
  bloque(-20,-2.6,3,40,1,3);
 }
}
module dcdc() {
 difference() {
  union() {balda(70,40);for(y=[10,35.5]) bloque(-31.5,y,3,63,1.5,3);}
  ventana(-24,14,48,19,3,5);
  for(x=[-23,23],y=[6.5,39]) ranura(x,y,t=5);
 }
}
module rak() {
 union() {
  difference() {balda(70,43);ventana(-20,16,40,15,3,5);}
  for(x=[-28,24],y=[12,34]) bloque(x,y,3,4,4,5);
 }
}
module bms() {
 difference() {
  balda(68,-7,-37);
  ventana(-22,-25,44,10,2.5,5);
  for(x=[-19,19],y=[-33.5,-10]) ranura(x,y,t=5);
 }
}

module placa() {
 difference() {
  union() {bloque(-39,0,0,78,154,4);for(x=[-34,24]) bloque(x,-4,0,10,4,4);for(y=[10,90]) bloque(-20,y,4,40,10,2);}
  for(v=[[15,14],[45,19],[88,21],[120,17]]) ventana(-18,v[0],36,v[1],3,8);
  for(y=[7,49,91,147],x=[-29.2,20.8]) bloque(x,y-.2,-1,8.4,3.4,8);
  for(y=[38,80],x=[-27.5,27.5]) ranura(x,y,90,t=8);
 }
}
module antena_ref() {
 // Referencia de montaje. No fabricar esta pieza comercial.
 color("black") translate([0,0,1]) union() {cylinder(d=36.6,h=66.9);translate([0,0,66.9]) intersection() {translate([0,0,-54.315]) sphere(r=57.315);translate([-60,-60,0]) cube([120,120,3]);}}
 color("silver") difference() {cilindro(0,0,-20,15.875,21);cilindro(0,0,-20.1,11,9.1);}
 color("silver") difference() {translate([0,0,-7]) cylinder(d=48/sqrt(3),h=3,$fn=6);cilindro(0,0,-7.1,16.2,3.2);}
 color("silver") difference() {cilindro(0,0,-4,30,1);cilindro(0,0,-4.1,16.2,1.2);}
}
module esqueleto() {
 base();
 for(a=[0:120:240]) rotate([0,0,a]) multmatrix([[0,0,1,92],[1,0,0,0],[0,1,0,4],[0,0,0,1]]) guia();
 translate([0,-3,4]) rotate([90,0,0]) placa();
 translate([0,0,11]) controlador();translate([0,0,53]) dcdc();translate([0,0,95]) rak();translate([0,0,151]) bms();
 if($preview) color("green",.65) bloque(-25,-49.5,8,50,40,120);
}
if(part=="base") base();
else if(part=="guia") guia();
else if(part=="lama") lama();
else if(part=="lama_superior") lama(true);
else if(part=="techo") techo();
else if(part=="disco_antena") disco_antena();
else if(part=="probeta") probeta();
else if(part=="probeta_antena") difference() {cube([78,28,3]);for(i=[0:2]) cilindro(14+25*i,14,-1,16+i*.2,5);}
else if(part=="placa") placa();
else if(part=="controlador") controlador();
else if(part=="dcdc") dcdc();
else if(part=="rak") rak();
else if(part=="bms") bms();
else if(part=="montaje") {
 esqueleto();
 for(i=[0:7]) translate([0,0,12+i*23.5]) lama();
 translate([0,0,200]) lama(true);
 translate([0,0,235.5]) techo_fisico();translate([0,0,249.5]) disco_antena();
 if($preview) translate([0,0,252.5]) antena_ref();
}
