import math
from swampy.TurtleWorld import *

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)

def circle(t, r):
	circum = 2*math.pi*r
	n=50
	polygon(t,circum/n,n)

def arc(t,r,angle):
	length = 2*math.pi*r /360 * angle
	n = 50
	for i in range(n):
		fd(t, length/n)
		lt(t, float(angle)/n)

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

def turtle_pies(t,length,n):
	theta = float(360)/n
	alpha = 90-float(theta/2)
	alpha_rad = float(math.pi*alpha)/180
	radius = length / math.cos(alpha_rad) /2
	for i in xrange(n):
		for i in xrange(n):
			lt(t,theta/2)
			fd(t,radius)
			rt(t,180-alpha)
			fd(t,length)
			rt(t,180-alpha)
			fd(t,radius)
			rt(t,180-theta/2)
		lt(t,theta)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00001
move(bob,-100)
turtle_pies(bob,100,5)
move(bob,200)
turtle_pies(bob,100,6)
move(bob,300)
turtle_pies(bob,100,7)

wait_for_user()