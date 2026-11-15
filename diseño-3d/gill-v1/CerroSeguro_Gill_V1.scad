// CERRO SEGURO — Gill shield V1 (parametric concept)
// Units: mm. Verify ALL fit dimensions on the actual hardware before printing.
// OpenSCAD: set part to assembly, louver, roof, base, sensor_tray, or wall_bracket.
$fn = 96;
part = "assembly";

// Envelope and ventilation
outer_d = 112;             // provisional overall louver diameter
inner_opening_d = 60;      // clear central airflow opening
louver_count = 7;
louver_pitch = 14;
louver_height = 8;
louver_thickness = 2.4;
roof_thickness = 3.2;

// Mechanical interface
rod_circle_d = 83;
rod_hole_d = 4.5;          // clearance for M4 rod
rod_count = 3;
base_thickness = 5;
base_d = 94;

// Sensor holder: PLACEHOLDERS — measure RAK1906 board and connector
sensor_board_x = 25;
sensor_board_y = 25;
sensor_clearance = 1.0;
tray_wall = 2.2;
tray_floor = 2.4;
tray_wall_height = 5;
wire_slot_w = 8;

// Wall bracket / fixing holes
wall_plate_w = 35;
wall_plate_h = 105;
wall_plate_t = 5;
wall_hole_d = 5.5;
arm_length = 53;
arm_w = 22;
arm_t = 7;

function z_louver(i) = base_thickness + 16 + i*louver_pitch;
function top_z() = z_louver(louver_count-1) + louver_height + 12;

module rod_holes(h=20) {
  for (i=[0:rod_count-1])
    rotate([0,0,i*360/rod_count])
      translate([rod_circle_d/2,0,-1]) cylinder(h=h+2,d=rod_hole_d);
}

module louver() {
  // Inclined ring: upper annular rain-shedding surface, open center.
  difference() {
    union() {
      cylinder(h=louver_height,d1=outer_d,d2=outer_d-16);
      cylinder(h=louver_thickness,d=outer_d);
    }
    translate([0,0,-1]) cylinder(h=louver_height+3,d=inner_opening_d);
    rod_holes(louver_height+2);
  }
}

module roof() {
  difference() {
    union() {
      cylinder(h=roof_thickness,d=outer_d+8);
      translate([0,0,roof_thickness]) cylinder(h=5,d1=outer_d+8,d2=outer_d-6);
    }
    rod_holes(roof_thickness+7);
  }
}

module base() {
  difference() {
    cylinder(h=base_thickness,d=base_d);
    // Open ventilation aperture; leave structural ring and tray mounts
    translate([0,0,-1]) cylinder(h=base_thickness+2,d=inner_opening_d-12);
    rod_holes(base_thickness+2);
  }
}

module sensor_tray() {
  sx=sensor_board_x+2*sensor_clearance+2*tray_wall;
  sy=sensor_board_y+2*sensor_clearance+2*tray_wall;
  difference() {
    union() {
      cube([sx,sy,tray_floor],center=true);
      for(x=[-1,1],y=[-1,1])
        translate([x*(sx/2-tray_wall/2),y*(sy/2-tray_wall/2),tray_wall_height/2])
          cube([tray_wall,tray_wall,tray_wall_height],center=true);
    }
    // Cable exits one side of the tray
    translate([0,sy/2,0]) cube([wire_slot_w,2*tray_wall+2,tray_floor+3],center=true);
  }
}

module wall_bracket() {
  // Wall plate and projecting arm, concept only; structural verification required.
  difference() {
    union() {
      translate([-wall_plate_w/2,-arm_length-wall_plate_t,-wall_plate_h/2])
        cube([wall_plate_w,wall_plate_t,wall_plate_h]);
      translate([-arm_w/2,-arm_length,-arm_t/2]) cube([arm_w,arm_length,arm_t]);
      translate([0,0,-arm_t/2]) cylinder(h=arm_t,d=30);
    }
    for (z=[-wall_plate_h/3,wall_plate_h/3])
      translate([0,-arm_length-wall_plate_t-1,z])
        rotate([-90,0,0]) cylinder(h=wall_plate_t+2,d=wall_hole_d);
    translate([0,0,-arm_t/2-1]) cylinder(h=arm_t+2,d=6);
  }
}

module assembly() {
  color("gainsboro") base();
  for(i=[0:louver_count-1])
    color("white") translate([0,0,z_louver(i)]) louver();
  color("white") translate([0,0,top_z()]) roof();
  // Rods are illustrative only: purchase M4 threaded rods and nuts.
  for(i=[0:rod_count-1])
    color("silver") rotate([0,0,i*360/rod_count])
      translate([rod_circle_d/2,0,0]) cylinder(h=top_z()+roof_thickness,d=4);
  color("orange") translate([0,0,base_thickness+6]) sensor_tray();
  color("gray") translate([0,-base_d/2-5,-wall_plate_h/2]) wall_bracket();
}

if(part=="assembly") assembly();
else if(part=="louver") louver();
else if(part=="roof") roof();
else if(part=="base") base();
else if(part=="sensor_tray") sensor_tray();
else if(part=="wall_bracket") wall_bracket();
else echo("Unknown part selection");
