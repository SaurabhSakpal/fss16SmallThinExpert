from swampy.TurtleWorld import *
import math, BasicArc

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def TutleFlowerPattern1(rotate, arc_angle, final_rotate):
	for i in range(7):
		BasicArc.arc(bob, 100, arc_angle);
		lt(bob, rotate);
		BasicArc.arc(bob, 100, arc_angle);
		lt(bob, final_rotate);


n = 7;
arc_angle = float(360) /n;
rotate = 180 - (float(360) / n);
final_rotate = 180 - (2 * arc_angle);

TutleFlowerPattern1(rotate, arc_angle, final_rotate);

wait_for_user()