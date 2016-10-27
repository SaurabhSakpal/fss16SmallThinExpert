from utils import *
import copy

class Schaffer(O):
    def __init__(self):
        decisions = [Decision('x',-100000,100000)]
        self.threshold = 0
        
    @staticmethod
    def evaluate(point):
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

    @staticmethod
    def generate_one(point):
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

    @staticmethod
    def neighbor(point):
        """ This method returns a random neighbor of the current point """
        x = point.decisions[0]
        while True:
            step = 5
            xn = x + random.randint(-1*step, step)
            if xn > pow(10, -5) and xn < pow(10, 5):
                return xn
    @staticmethod
    def randomNeighbor():
        """ This method returns a random neighbor of the current point """
        return self.generate_one()

class Osyczaka2(O):
    def __init__(self):
        decisions = [Decision('x1',0,10), Decision('x2',0,10), Decision('x3',1,5), Decision('x5',1,5), Decision('x4',0,6), Decision('x6',0,10)]
        self.threshold = 0
        
    def evaluate(point):
        if not point.objectives:
            decs = point.decisions
            point.objectives = [self.f1(*point.decisions),self.f2(*point.decisions)]
        return point.objectives
    
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
        if (x5 - 3)**3 + x6 - 4:
            return False
        return True

    def f1(x1, x2, x3, x4, x5, x6):
        """ This method returns value of function 1 for given point """
        return -(25 * (x1 - 2)**2 + (x2 - 2)**2 + ((x3 - 1)**2)*((x4 - 4)**2) + (x5 - 1)**2);

    def f2(x1, x2, x3, x4, x5, x6):
        """ This method returns value of function 2 for given point """
        return x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2;


    @staticmethod
    def energy(point):
        """ The energy is used to check if the point is better or not """

        return f1(*point.decisions) + f2(*point.decisions); 

    @staticmethod
    def generate_one(point):
        while True: 
            point = Point([random_value(d.low, d.high) for d in self.decisions])
            if self.is_valid(*point):
                return point

    @staticmethod
    def neighbor(point):
        index = random.randint(6)
        tempPoint = copy.deepcopy(point)
        decision = model.decisions[index]
        oldValue = point.decisions[index]
        newValue = random_value(decision.low, decision.high)
        tempPoint.decision[index] = newValue
        while oldValue == newValue or not self.is_valid(*tempPoint.decisions):
            step = random_value(-1,1)
            newValue = min(max(oldValue+step,decision.low),decision.high)
            tempPoint.decision[index] = newValue
        return tempPoint

    @staticmethod
    def randomNeighbor():
        """ This method returns a random neighbor of the current point """
        return self.generate_one()
            

class Kursawe(O):
    def __init__(self):
        n = random.randint(3,8)
        decisions = [Decision('',-5,5)]*n
        self.threshold = 0
        
    @staticmethod
    def evaluate(point):
        if not point.objectives:
            point.objectives = [f1(point.decisions),f2(point.decisions)]
        return point.objectives
    
    @staticmethod
    def is_valid(point):
        for x in point.decisions:
            if x < -5 or x > 5:
                return False
        return True

    @staticmethod
    def generate_one(point):
        point = Point([random_value(d.low, d.high) for d in self.decisions])
        return point

    @staticmethod
    def energy(point):
        """
        calculates the energy for given point
        energy(f1,f2) = ((f1 + f2) - min) / (max - min)
        """
        return sum(point.objectives)

    def f1(self):
        """ This method returns value of function 1 for given point """
        return sum([ -10*math.e**(-0.2*(self.decisions[i]**2 + self.decisions[i+1]**2)**0.5) for i in range(self.n-1)])

    def f2(self):
        """ This method returns value of function 2 for given point """
        return sum([abs(d)**2 + 5*math.sin(d**4) for d in self.decisions])

    @staticmethod
    def neighbor(point):
        index = random.randint(self.n)
        tempPoint = copy.deepcopy(point)
        decision = model.decisions[index]
        oldValue = point.decisions[index]
        newValue = random_value(decision.low, decision.high)
        tempPoint.decision[index] = newValue
        while oldValue == newValue or not self.is_valid(*tempPoint.decisions):
            step = random_value(-1,1)
            newValue = min(max(oldValue+step,decision.low),decision.high)
            tempPoint.decision[index] = newValue
        return tempPoint

    @staticmethod
    def randomNeighbor():
        """ This method returns a random neighbor of the current point """
        return self.generate_one()