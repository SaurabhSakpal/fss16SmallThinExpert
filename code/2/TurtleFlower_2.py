from swampy.TurtleWorld import *

import math, BasicArc

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def TuttleFlowerPattern2(rotate, arc_angle, final_rotate, total_sides, size):
	for i in range(12):
		BasicArc.arc(bob, size, arc_angle);
		lt(bob, rotate);
		BasicArc.arc(bob, size, arc_angle);
		lt(bob, final_rotate);


n = 8;
arc_angle = (float(360) /(6));
rotate = 180 - (arc_angle);
final_rotate = 180 - (2 * (float(360) / n));
size = 150

TuttleFlowerPattern2(rotate, arc_angle, final_rotate, n, size);

wait_for_user()