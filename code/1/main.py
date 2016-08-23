#!/usr/bin/python
import utest, saurabh
from saurabh import multiply

@utest.ok
def add() :
	return 4 + 5

print "Value of addition is ", add()

print "Value of multiplication is ", multiply()

utest.oks()

