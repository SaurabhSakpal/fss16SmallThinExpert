from swampy.TurtleWorld import *

import math, BasicArc

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def TurleFlowerPattern3(rotate, arc_angle, final_rotate, n, size):
	for i in range(n):
		BasicArc.arc(bob, size, arc_angle);
		lt(bob, rotate);
		BasicArc.arc(bob, size, arc_angle);
		lt(bob, final_rotate);


n = 20;
arc_angle = float(360) /n;
rotate = 180 - (float(360) / n);
final_rotate = 180 - (2 * arc_angle);
size = 200;

TurleFlowerPattern3(rotate, arc_angle, final_rotate, n, size);

wait_for_user()