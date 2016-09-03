from swampy.TurtleWorld import *

import math

# The basic structure of arc() method is taken from the book the Think in Python (http://www.greenteapress.com/thinkpython/html/thinkpython005.html)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)