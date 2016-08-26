#!/usr/bin/python
import utest, saurabh, gurunath, shivani
from saurabh import multiply

@utest.ok
def to_fail() :
	"A  test that fails"
	assert 1==2

print "Value of multiplication is ", multiply()

utest.oks()

