import random

def energy(x):
    
    f1 = pow(x, 2)
    f2 = pow(x-2, 2)
    return ((f1+f2) - min ) / ( max - min )

def probability(e, en, ratio):
    
    return pow(e, (e - en) / ratio )
    
def neighbor(x):
    
    while True:
        step = 5
        xn = x + random.randint(-1*step, step)
        if xn > pow(10, -5) and xn < pow(10, 5):
            return xn

def randneighbor():
    
    while True:
        xn = random.randint(pow(10, -5), pow(10, 5))
        if xn > pow(10, -5) and xn < pow(10, 5):
            return xn

# class SimulatedAnnealing:
    
#     def __init__(self, )

def simulatedannealing(x0):
    
    kmax = 100
    s = x0
    e = energy(x0)
    eb = e
    sb = s
    k = kmax
    sd = 100
    emax = 10
    random.seed(sd)
    
    while e > emax and k > 0:
        sn = neighbor(s)
        en = energy(sn)
        
        if en < eb:
            eb = en
            sb = sn
            print '!'
        
        if en < e:
            s = sn
            e = en
            print '+'
            
        elif probability(e, en, (k/kmax)) < random.randint():
            
            s = randneighbor()
            e = energy(s)
            print '?'
        
        k -= 1
        
        if k % 25 == 0:
            print '\n'
            
max = pow(10, 3)
min = 10

simulatedannealing(0)