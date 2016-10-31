from __future__ import print_function
from __future__ import division
from models import *
import inspect

class SimulatedAnnealing:
	def __init__(self, model):
		self.model = model
		self.solution = model.generate_one()

	def say(x):
	    print(x)

	def probability(self, e, en, ratio):
	    """ This method calculates the probability by which we do random jump """
	    #print(e,en,ratio)
	    return pow( math.e, (e-en) / ratio )

	def run(self):
		self.simulatedAnnealing()
	    
	def simulatedAnnealing(self):
	    print("### saDemo ##################################################");
	    print("# Basic Study")
	    print("!!! Schaffer \n \n")
	    print("Schaffer\n\n")

	    kmax = 4000
	    s = self.solution
	    self.model.evaluate(s)
	    e = self.model.energy(s)
	    eb = e
	    #print(e)
	    sb = s
	    k = 1
	    sd = 1
	    emax = self.model.threshold
	    random.seed(sd)
	    say('\n')
	    say(str(k) + ', ')
	    #say(str(sb) + ', ')
	    
	    while e > emax and k < kmax:
	        sn = self.model.neighbor(s)
	        self.model.evaluate(sn)
	        en = self.model.energy(sn)

	        if en < eb:
	            # new best solution has been found
	            eb = en
	            sb = sn
	            say('!')
	        
	        if en < e:
	            # energy of neighbour better than current so update the current
	            s = sn
	            e = en
	            say('+')
	            
	        elif self.probability(e, en, (float(k)/float(kmax))) < random.random():
	            # make a random jump to escape the local maxima            
	            s = self.model.generate_one()
	            self.model.evaluate(s)
	            e = self.model.energy(s)
	            say('?')
	        
	        k += 1
	        say('.')
	        if k % 25 == 0:
	            say('\n')
	            #say(str(k) + ', ')
	            #say(str(sb) + ', ')
	    say("\n\ne : "+str(eb))
	    say("\nx : "+str(sb)+"\n\n")



class MaxWalkSat:

	def __init__(self, model):
		#print(model)
		#inspect.getargspec(self.__init__)
		self.model = model
		self.solution = model.generate_one()

	
	# def getRandomValidPoint(point, randomPart):
	# 	""" randomly changes a random part of a given point"""
	# 	maxTries = 250
	# 	try_count = 0;
	# 	while True and maxTries > try_count:
	# 		newPoint = copy.deepcopy(point)
	# 		for i in randomPart:
	# 			newPoint[i] = random.choice(xbounds[i])
	# 		if is_valid(*newPoint):
	# 			return newPoint
	# 		try_count +=1
	# 	return point
	
	def run(self):
		self.maxWalkSat()

	def maxWalkSat(self, maxTries=20, maxRounds=20, probability=0.5):
		global_best = 0;
		global_point = [];
		#print("hello world")
		for i in xrange(maxTries) :
			#print("outer")
			current_point = self.solution
			self.model.evaluate(current_point)
			current_solution = self.model.energy(current_point)
			best_point = current_point		
			best_solution = current_solution
			value = str(i)+". "
			for j in xrange(maxRounds):
				#print("	inner")
				# check if the solution is better than required threshold
				if current_solution <= self.model.threshold :
					return (current_solution, current_point) 
				else :
					#else find a random part of the current soltuion
					# n = len(self.model.point.decision)
					# random_part = random.sample(range(n), random.randint(1, n))
					# one_random_decision = random.choice(random_part)
					if random.random() < probability :
						pointNew = self.model.randomNeighbor()
						self.model.evaluate(pointNew)
						tempSolution = self.model.energy(pointNew)
						if tempSolution < current_solution :
							current_solution = tempSolution
							current_point = pointNew
							if tempSolution < best_solution:
								best_solution = tempSolution
								best_point = pointNew
								value += "!"
							else:
								value += '+'
						else:
							value += '.'
					else :
						flag = True
						pointNew = self.model.neighbor(current_point)
						#print(pointNew)
						self.model.evaluate(pointNew)
						tempSolution = self.model.energy(pointNew)
						if tempSolution < current_solution :
							current_solution = tempSolution
							current_point = pointNew;
							if tempSolution < best_solution:
								best_solution = tempSolution
								best_point = pointNew
								value += "!"
								flag = False;
							else:
								value += '+'
						else:
							value += '.'

			if global_best > best_solution:
				global_best = best_solution
				global_point = best_point
			print(value + " : " + str(best_solution))
		return (global_best, global_point)
