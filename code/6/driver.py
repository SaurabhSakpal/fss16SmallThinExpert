from Optimizers import *

#models = [Schaffer,Osyczaka2,Kursawe]
models = [Osyczaka2]
#Optimizers = [MaxWalkSat, SimulatedAnnealing]
Optimizers = [SimulatedAnnealing]

for model in models:
	for optimizer in Optimizers:
		modelobj = model()
		#print modelobj 
		optobj = optimizer(modelobj)
		optobj.run()
		#modelobj.test()
