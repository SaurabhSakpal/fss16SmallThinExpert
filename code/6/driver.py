from optimizers import *

#models = [Schaffer,Osyczaka2,Kursawe]
models = [Osyczaka2]
#optimizers = [MaxWalkSat, SimulatedAnnealing]
optimizers = [MaxWalkSat]

for model in models:
	print '************ Executing '+str(model)+'*************'
	for optimizer in optimizers:
		modelobj = model()
		#print modelobj 
		optobj = optimizer(modelobj)
		optobj.run()
		#modelobj.test()
