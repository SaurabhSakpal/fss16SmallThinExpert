from __future__ import print_function

import random, math

def say(x):
    print(x, end="")

def energy(x):
    
    f1 = pow(x, 2)
    f2 = pow(x-2, 2)
    #print(f1)
    #print(f2)
    energy = float((f1+f2) - min ) / float( max - min ) 
    #print (energy)
    return energy

def probability(e, en, ratio):
    
    return pow( math.e, (e-en) / ratio )
    
def neighbor(x):
    
    while True:
        step = 5
        xn = x + random.randint(-1*step, step)
        if xn > pow(10, -5) and xn < pow(10, 5):
            return xn

def randneighbor():
    
    while True:
        xn = random.randint(int(pow(10, -5)), int(pow(10, 5)))
        if xn > pow(10, -5) and xn < pow(10, 5):
            return xn

def simulatedannealing(x0):
    print("### saDemo ##################################################");
    print("# Basic Study")
    print("!!! Schaffer \n \n")
    print("Schaffer\n\n")

    kmax = 4000
    s = x0
    e = energy(x0)
    eb = e
    #print(e)
    sb = s
    k = 0
    sd = 1
    emax = -1
    random.seed(sd)
    say('\n')
    say(str(k) + ', ')
    say(str(sb) + ', ')
    
    while e > emax and k < kmax:
        sn = neighbor(s)
        en = energy(sn)

        if en < eb:
            eb = en
            sb = sn
            say('!')
        
        if en < e:
            s = sn
            e = en
            say('+')
            
        elif probability(e, en, (float(k)/float(kmax))) < random.random():
            
            s = randneighbor()
            e = energy(s)
            say('?')
        
        k += 1
        say('.')
        if k % 25 == 0:
            say('\n')
            say(str(k) + ', ')
            say(str(sb) + ', ')
    say("\n\ne : "+str(eb))
    say("\nx : "+str(sb)+"\n\n")
min=80000
max=1000000

simulatedannealing(random.randint(int(pow(10,-5)),int(pow(10,5)),))
