import random, math
from model import *
#This code attempts to solve 2-SAT problem using MaxWalkSat

operator = {0:'|', 1: '&'}
max_tries = 1000
max_changes = 10

def printSolution(solution):
	'''
	Given truh values of all the variables. Print the solution
	'''
	for i,var in enumerate(solution):
		print 'x'+str(i)+' :'+str(solution[var])

def printExpression(expression, signs):
	'''
	prints all clauses joined by and operator. 
	A clause (2,3,0) will be printed as x2 | x3
	'''
	exp = []
	for i,e in enumerate(expression):
		s1 = '!' if signs[i][0]==1 else ''
		s2 =  '!' if signs[i][1]==1 else ''
		exp.append('('+s1+'x'+str(e[0])+' '+operator[e[2]]+' '+s2+'x'+str(e[1])+')')
	
	print ' & '.join(exp)

def generateExpression(num_clauses,num_vars):
	'''
	Returns 2 lists expression and signs. This list is called expression.
	Each item in expression is a clause (a tuple of size 3).
	clause is of the form (variable1,variable1, operator )
	Each item in signs is a tuple (s1,s2). s1, s2 being signs of variable1 and 2 in the clause
	'''
	expression = []
	signs = []
	for i in range(num_clauses):
		v = random.sample(range(num_vars),2)
		expression.append((v[0],v[1],random.randint(0,1)))
		s1 = random.randint(0,1)
		s2 = random.randint(0,1)
		signs.append((s1,s2))
	return expression, signs

def evaluateClause(clause,solution, sign):
	'''
	Returns the truth value of the clause
	'''
	s1,s2 = sign
	v1 = solution[clause[0]]
	v2 = solution[clause[1]]
	if s1:
		v1 = not v1
	if s2:
		v2 = not v2

	if clause[2]==1:
		# operator is AND
		return v1 and v2
	else:
		# operator is OR
		return v1 or v2

def findCost(solution,signs):
	'''
	Returns cost of a solution.
	Cost is defined as number of clauses evaluting to False
	'''
	clause_val = [evaluateClause(c,solution,signs[i]) for i,c in enumerate(expression)]
	return sum([0 if v else 1 for v in clause_val])

def maxWalkSat(expression, signs, num_vars, insanity=0.3):
	solution = [False]*num_vars
	#60% clauses should be satisfied for a solution to be optimal
	thresh = 0.4
	cost = findCost(solution,signs)

	for trial in range(max_tries):
		for change in range(max_changes):

			#Find truth value of all the clauses and find cost
			cost = findCost(solution,signs)
			if float(cost)/num_clauses < thresh:
				return solution
			
			#Make a list of all false clauses and pick a random clause from it
			clause_val = [evaluateClause(c,solution,signs[i]) for i,c in enumerate(expression)]
			false_clauses = [i for i, isTrue in enumerate(clause_val) if not isTrue]
			a_clause = expression[random.choice(false_clauses)]

			if random.random() < insanity:
				#jump around if your sanity is even less than insanity
				var = a_clause[random.randint(0,1)]
				solution[var] = not solution[var]
			else:
				#throw marbles and check if you are sane
				var1,var2,op = a_clause

				#try flipping both variables and re-evaluate cost for each flip
				var1 = not var1
				cost1 = findCost(solution,signs)
				var1 = not var1
				
				var2 = not var2
				cost2 = findCost(solution,signs)
				var2 = not var2

				#Flip variable whih gives you min cost after flipping
				if cost1 < cost2:
					solution[var1] = not solution[var1]
				else:
					solution[var2] = not solution[var2]
	return solution



if __name__ == '__main__':
	num_vars = 6
	num_clauses = 200
	expression, signs = generateExpression(num_clauses,num_vars)
	printExpression(expression, signs)
	solution = maxWalkSat(expression,signs,num_vars)
	score = float(num_clauses-findCost(solution,signs))/num_clauses
	print 'A solution which satisfies '\
	+str(score*100)\
	+' per cent clauses out of ',str(num_clauses)
	printSolution(solution)
