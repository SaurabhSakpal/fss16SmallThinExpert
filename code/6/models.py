from utils import *
import copy
import math

class Schaffer(O):
    def __init__(self):
        #print "Inside Schaffer"
        self.decisions = [Decision('x',-100000,100000)]
        self.threshold = -1
        
    def evaluate(self, point):
        #print point
        if not point.objectives:
            x = point.decisions[0]
            point.objectives = [x**2,(x-2)**2]
        return point.objectives
    
    @staticmethod
    def is_valid(point):
        x = point.decisions[0]
        if x >= -100000 and x <= 100000:
            return True
        return False 

    def generate_one(self):
        point = Point([random_value(d.low, d.high) for d in self.decisions])
        return point

    @staticmethod
    def energy(point):
        """
        calculates the energy for given point
        energy(f1,f2) = ((f1 + f2) - min) / (max - min)
        """
        objectives = point.objectives
        return (sum(objectives) - 80000)/(1000000 - 80000)

    def neighbor(self, point):
        """ This method returns a random neighbor of the current point """
        x = point.decisions[0]
        while True:
            step = 5
            xn = x + random.randint(-1*step, step)
            #print xn
            #print (xn > pow(10, -5) and xn < pow(10, 5))
            if xn >= -100000 and xn <= 100000:
                return Point([xn])

    def randomNeighbor(self):
        """ This method returns a random neighbor of the current point """
        return self.generate_one()

class Osyczaka2(O):
    def __init__(self):
        self.decisions = [Decision('x1',0,10), Decision('x2',0,10), Decision('x3',1,5), Decision('x4',0,6), Decision('x5',1,5), Decision('x6',0,10)]
        self.threshold = -1000
    
    def evaluate(self, point):
        if not point.objectives:
            decs = point.decisions
            point.objectives = [Osyczaka2.f1(*point.decisions), Osyczaka2.f2(*point.decisions)]
        return point.objectives
    
    @staticmethod
    def is_valid(x1, x2, x3, x4, x5, x6):
        """ This method returns if selected points are valid or not """
        # g1
        if x1 + x2 - 2 < 0:
            return False
        # g2    
        if 6 - x1 - x2 < 0:
            return False
        # g3
        if 2 - x2 + x1 < 0:
            return False
        #g4
        if 2 - x1 + 3 * x2 < 0:
            return False
        #g5
        if 4 - ((x3 - 3)**2) - x4 < 0:
            return False
        #g6
        if (x5 - 3)**3 + x6 - 4 < 0:
            return False
        return True

    @staticmethod
    def f1(x1, x2, x3, x4, x5, x6):
        """ This method returns value of function 1 for given point """
        return -(25 * (x1 - 2)**2 + (x2 - 2)**2 + ((x3 - 1)**2)*((x4 - 4)**2) + (x5 - 1)**2);

    @staticmethod
    def f2(x1, x2, x3, x4, x5, x6):
        """ This method returns value of function 2 for given point """
        return x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2;


    @staticmethod
    def energy(point):
        """ The energy is used to check if the point is better or not """

        return Osyczaka2.f1(*point.decisions) + Osyczaka2.f2(*point.decisions); 


    def generate_one(self):
        while True: 
            point = Point([random_value(d.low, d.high) for d in self.decisions])
            #print point
            #print self.is_valid(*point.decisions)
            if self.is_valid(*point.decisions):
                return point

    def neighbor(self, point):
        index = random.randint(0,5)
        #print index
        tempPoint = copy.deepcopy(point)
        decision = self.decisions[index]
        oldValue = point.decisions[index]
        newValue = random_value(decision.low, decision.high)
        tempPoint.decisions[index] = newValue
        while oldValue == newValue or not self.is_valid(*tempPoint.decisions):
            step = random_value(-1,1)
            newValue = min(max(oldValue+step,decision.low),decision.high)
            tempPoint.decisions[index] = newValue
        return tempPoint

    def randomNeighbor(self):
        """ This method returns a random neighbor of the current point """
        return self.generate_one()
            

class Kursawe(O):
    def __init__(self):
        self.n = random.randint(3,8)
        self.decisions = [Decision('',-5,5)] * self.n
        self.threshold = -100
        
    def evaluate(self, point):
        if not point.objectives:
            point.objectives = [self.f1(point.decisions), self.f2(point.decisions)]
        return point.objectives
    
    @staticmethod
    def is_valid(point):
        for x in point.decisions:
            if x < -5 or x > 5:
                return False
        return True

    def generate_one(self):
        point = Point([random_value(d.low, d.high) for d in self.decisions])
        return point

    @staticmethod
    def energy(point):
        """
        calculates the energy for given point
        energy(f1,f2) = ((f1 + f2) - min) / (max - min)
        """
        return sum(point.objectives)

    def f1(self, decisions):
        """ This method returns value of function 1 for given point """
        return sum([ -10*math.e**(-0.2*(decisions[i]**2 + decisions[i+1]**2)**0.5) for i in range(self.n-1)])

    def f2(self, decisions):
        """ This method returns value of function 2 for given point """
        return sum([abs(d)**2 + 5*math.sin(d**4) for d in decisions])

    def neighbor(self, point):
        index = random.randint(0, self.n-1)
        tempPoint = copy.deepcopy(point)
        decision = self.decisions[index]
        oldValue = point.decisions[index]
        newValue = random_value(decision.low, decision.high)
        tempPoint.decisions[index] = newValue
        while oldValue == newValue or not self.is_valid(tempPoint):
            step = random_value(-1,1)
            newValue = min(max(oldValue+step,decision.low),decision.high)
            tempPoint.decisions[index] = newValue
        return tempPoint

    def randomNeighbor(self):
        """ This method returns a random neighbor of the current point """
        return self.generate_one()

    def test(self):
        min = 0
        max = 0
        for i in range(1000000):
            point = self.generate_one()
            self.evaluate(point)
            value = self.energy(point)
            if value < min:
                min = value
            if value > max:
                max = value
        print min
        print max