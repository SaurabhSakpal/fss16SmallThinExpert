from __future__ import division,print_function
import sys,random,os
sys.dont_write_bytecode=True

class Employee:
	"""A class that represents and employee"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return 'Employee name is %s, Employee age is %i'%(self.name, self.age)

	def __lt__(self, other):
		return self.age < other.age

if __name__=="__main__":

	emp1 = Employee('Harry', 23)
	emp2 = Employee('Hermoine',21)
	emp3 = Employee('Ron', 21)

	emp_list = [emp1, emp2, emp3]
	
	for e in emp_list.sort():
		print e


		