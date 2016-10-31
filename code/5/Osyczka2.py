import random, copy

bound_x1_x2_x6 = xrange(0,11)
bound_x3_x5 = xrange(1,6)
bound_x4 = xrange(0,7)

xbounds = [bound_x1_x2_x6, bound_x1_x2_x6, bound_x3_x5, bound_x4, bound_x3_x5, bound_x1_x2_x6]


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



def f1(x1, x2, x3, x4, x5, x6):
	""" This method returns value of function 1 for given point """
	return -(25 * (x1 - 2)**2 + (x2 - 2)**2 + ((x3 - 1)**2)*((x4 - 4)**2) + (x5 - 1)**2);



def f2(x1, x2, x3, x4, x5, x6):
	""" This method returns value of function 2 for given point """
	return x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2;



def score(x1, x2, x3, x4, x5, x6):
	""" The score is used to check if the point is better or not """
	return f1(x1, x2, x3, x4, x5, x6) + f2(x1, x2, x3, x4, x5, x6);


def generate_one():
	"""" Generate one valid point randomly """
	while True:
		solution = []
		for bound in xbounds:
			solution.append(random.sample(bound, 1)[0])
		if is_valid(*solution):
			return solution

def getRandomValidPoint(point, randomPart):
	""" randomly changes a random part of a given point"""
	maxTries = 250
	try_count = 0;
	while True and maxTries > try_count:
		newPoint = copy.deepcopy(point)
		for i in randomPart:
			newPoint[i] = random.choice(xbounds[i])
		if is_valid(*newPoint):
			return newPoint
		try_count +=1
	return point



def maxWalkSat(maxTries=20, maxRounds=20, threshold=-1000, probability=0.5):
	global_best = 0;
	global_point = [];
	for i in xrange(maxTries) :
		current_point = generate_one()
		current_solution = score(*current_point)
		best_point = current_point		
		best_solution = current_solution
		value = str(i)+". "
		for j in xrange(maxRounds):
			# check if the solution is better than required threshold
			if current_solution <= threshold :
				return (current_solution, current_point) 
			else :
				#else find a random part of the current soltuion
				random_part = random.sample(range(6), random.randint(1,6))
				one_random_decision = random.choice(random_part)
				if random.random() < probability :
					pointNew = getRandomValidPoint(current_point, random_part)
					tempSolution = score(*pointNew)
					if tempSolution < current_solution :
						current_solution = tempSolution
						current_point = pointNew
						if tempSolution < best_solution:
							best_solution = tempSolution
							best_point = pointNew
							value += "!"
					else:
						value += "?"
				else :
					flag = True
					for neighbour_value in xbounds[one_random_decision]:
						pointNew = copy.deepcopy(current_point)
						pointNew[one_random_decision] = neighbour_value;
						if is_valid(*pointNew):
							tempSolution = score(*pointNew)
							if tempSolution < current_solution :
								current_solution = tempSolution
								current_point = pointNew;
								if tempSolution < best_solution:
									best_solution = tempSolution
									best_point = pointNew
									value += "!"
									flag = False;
								break;
					if flag:
						value+="."
		if global_best > best_solution:
			global_best = best_solution
			global_point = best_point
		print value + " : " + str(best_solution)
	return (global_best, global_point)

a = maxWalkSat()
print a[0]
print a[1]

