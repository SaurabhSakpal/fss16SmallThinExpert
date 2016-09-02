#!/usr/bin/env

# Exercise 3.1

repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# NameError : Name repeat_lyrics not found

# Exercise 3.2

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
repeat_lyrics()

# NameError : Name repeat_lyrics not found

# Exercise 3.3

def right_justify(sample_string):
    length = len(sample_string)
    
    for x in range(0, 70 - length):
        print ' ',
    
    print sample_string

string = "test"
right_justify(string)

# Exercise 3.4

# Part 1

def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)

# Part 2

def do_twice(f, value):
    f(value)
    f(value)

def print_spam(value):
    print 'spam', value

do_twice(print_spam, 10)

# Part 3

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(string):
    print string

string = "any_string"

do_twice(print_twice, string)

# Part 4

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(string):
    print string

string = "spam"

do_twice(print_twice, string)

# Part 5 

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(string):
    print string

string = "spam"

do_four(print_twice, string)

# Exercise Q5

# Part 1

def print_unique():
    print "+ - - - - + - - - - +"


def print_row():
    print "|         |         |"
    
def doMultiTimes(task, n):
    for x in xrange(n):
        task()

def print_grid():
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
    
print_grid()

# Part 2

def print_unique():
    print "+ - - - - + - - - - + - - - - + - - - - + "


def print_row():
    print "|         |         |         |         |"
    
def doMultiTimes(task, n):
    for x in xrange(n):
        task()

def print_grid():
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
    doMultiTimes(print_row, 4)
    doMultiTimes(print_unique, 1)
print_grid()