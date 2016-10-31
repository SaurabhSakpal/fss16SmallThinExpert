from Optimizers import *

models = [Schaffer,Osyczaka2,Kursawe]
Optimizers = [maxWalkSat, simulatedAnnealing]

for model in models:
	for optimizer in Optimizers:
		optimizer(model())