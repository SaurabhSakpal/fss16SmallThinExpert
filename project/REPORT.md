# Software Product Line Optimization 
## 1. Overview

A software product line is a set of software-intensive systems that share a common, managed set of features satisfying the specific needs of a particular market segment or mission and that are developed from a common set of core assets in a prescribed way [1]. They are emerging as an important development paradigm because they help companies in modelling their solutions and offerings. It provides a structured way to quantify market, cost, productivity, quality, and other business drivers. A fundamental problem in software product line engineering is that a product line of industrial size can easily incorporate several thousand variable features. Such variability leads to heterogeneous goals and contradicting requirements. This motivated us to use the optimization techniques studied in CSC 591 Automated Software Engineering for finding sound and optimum configurations of very large variability models.
sadsad

## 2. Background

Many results in the automated analysis of software product lines were validated using feature models published in online feature model repositories such as SPLOT [2]. Some of these works are Sayyad et al. [3] [4], Pohl et al. [5], Lopez-Herrejon and Egyed [6], Johansen et al. [7], Mendonca et al. [8].  Most of the feature models in SPLOT were produced for academic purposes without representing actual systems. SPLOT models are small and less constrained with lower branching factors, but they also have higher ratios of feature groups and deep leaves [9]. This is how they differ from the actual software product lines in the industry. But nonetheless, they have been significant academically to analyze and compare optimization techniques. 
In this project we have done a 5-objective optimization of Software Product Line using different optimizers on three different models of varied size (mentioned in 3.1). There are five conflicting objectives further explained in section 3.1. Optimizers used and compared in this work include a naive Genetic Algorithm (GA) with random select operator, Nondominated Sorting Genetic Algorithm-II (NSGA-II) [10], Strength Pareto Evolutionary Algorithm SPEA2 [12], and a variation of NSGA2 using continuous domination (CDOM) instead of binary domination (BDOM). Three different performance measure Hypervolume, Spread and Inter Generational Distance (IGD) are used to analyze the performance of these optimizers on the three models. 

## 3. Implementation
The workflow of this project is illustrated in Fig 1. The model consist of an XML file obtained from SPLOT. The file is parsed to obtain a feature tree in Python. The parsed tree is traversed from top to bottom to generate a point.  A point is an instance of the population. Several points meeting the model constraints are generated to make up Generation 0 population that is an input to the optimizers. Optimizers run until the specified generations and give a set of points that are meta heuristically best satisfy the given objectives. This set of solution is pareto optimal and hence called the pareto frontier. These pareto frontiers are then analyzed on Hypervolume, Spread and IGD to rank the optimizers.

![alt text](https://raw.githubusercontent.com/SaurabhSakpal/fss16SmallThinExpert/master/project/data/ASE%20Architecture%20Diagram.png)
### 3.1 Models
A feature is an end-user-visible behavior of a software product that is of interest to some stakeholder. A feature model represents the information of all possible products of a software product line in terms of features and relationships among them. A feature model is represented as a hierarchically arranged set of features composed by: (1) Relationships between a parent feature and its child features (or subfeatures). (2) Cross-tree constraints that are typically inclusion or exclusion statements. All constraints are represented as CNF clauses. An example of a SPLOT model XML is given below:


![alt_text](https://github.com/SaurabhSakpal/fss16SmallThinExpert/blob/master/project/data/SplotParserXMLCode.png)


The summary of the three models used is given below:

| Model        | Number of Features           | Number of Cross Tree Constraints  |
| ------------- |:-------------:| :-----:|
| Home Automation     | 48 | 5 |
| Computadores      | 45      |   9 |
| Database Tools | 70      |    2 |


#### 3.1.1 Decisions
For a feature model, decisions are the various features in the model. All decisions are boolean, indicating whether a feature is selected or not. 
#### 3.1.2 Objectives
This project attempts multi objective optimization. For each model we have five conflicting objectives, as summarized below. Some of the objectives have been taken from this prior work [4].


| Objective        | Maximize/ Minimize           | Description  |
| ------------- |:-------------:| :-----|
| Cost     | Minimize |Each feature is associated with a cost to company. Cost of a product is sum of cost of all features it has. |
| Feature Richness      | Maximize      |   Number of features in the model |
| Violations      | Minimize      |   Number of cross tree constraints violated by the product.* |
| Benefits   | Maximize      |    Each feature has a benefit value, indicating how profitable it is for the company. Sum of all feature benefits in the product is the objective. |
| Defects   | Minimize      |    Each feature has a defect value, indicating how often this feature shows a defect. Sum of all feature defects in the product is the objective. |

*we generate products with 0 violations at the start, mutations introduced in our optimizers introduce minors violations in the later generations. 


### 3.2 Parser
The SPLOT models are in form of an XML as shown below. We wrote a parser to convert XML models into a tree. Extracting out the explicitly stated cross tree constraints and also the implicit tree structure constraint. 
Example of a feature model:
</p align="center">
![alt text](https://github.com/SaurabhSakpal/fss16SmallThinExpert/blob/master/project/data/image2.jpg)
</p>
### 3.3 SAT Solver
Though we have minimum constraint violations as one of our objectives. On Dr. Menzie’s suggestion we realized, we can SAT solve our generation 0 for all Optimizers (all optimizers we have are GA variations). This will give us 100% valid solutions right in the beginning. But still as the population evolves, mutations are introduced and we get some violations in cross tree constraints (tree structure constraints are not violated as our mutate operator takes care of that). Hence variance for this objective is very low (almost nil). All objectives are given equal weight. This means a single violation will greatly penalize the point fitness. This is desirable as we aim to achieve solutions with zero violations (not just minimum).

### 3.4 Optimisers
Genetic Algorithms have been one of the most common evolutionary algorithms in use for optimization. We have used following variants of Genetic Algorithms for the comparison. Each of them differ in just there select operator which decides what all points (equal to population size, k) will survive till the next generation. 

**Naive Genetic Algorithms:** Random points k are picked and taken over to the next generation. 

**NSGA2:** A primary ranking method (like BDOM) based on number of points that dominate a point is used to generate frontiers then a secondary sorting method is used for non-dominating sorting. This is mostly done with a motive of crowd pruning to preserve the diversity. Details can be studied in this work by Deb et al [10].

**SPEA2:** Unlike NSGA2, all individuals are scored by the number of other people they dominate. Two data structures population and archive are maintained. Population is a space for current mutants while archive is a space for good ideas. Population is built partially from archive. Details can be studied in this work by zitzler et al [11].

**NSGA2Cdom:** In a multiple objective problem binary domination is not the best way to go. As seen in work by Sayyad et al [3], continuous domination performs better for multi objective optimizations. This optimizer is a variant of NSGA2 with domination function replaced by CDOM. Now we can compare on how much a point is better or worse than the other.  

**Mutate :** To mutate each node is decided to be changed or not by flipping a coin biased as the mutation probability. If we decide not to mutate the node remains same, but if decide to mutate the whole subtree is generated again (highlighted in blue) following the tree structure constraints (not necessarily cross tree constraint).

**Cross-over :** For each node in a group a fair coin is tossed to select if the node would be taken from mom or dad. The whole subtree from that node is copied exactly into the child. 


We have used DEAP library [12] for our implementation of these algorithms. We had to provide our own our own cross-over and mutate operators and also a select operator for NSGA2Cdom. A point is represented as a feature tree with boolean values for each node. The cross-over and mutate operator works as shown below. 


## 4. Source Code
## 5. Results
## 6. Inference
## 7. Conclusion
## 8. References
[1] http://www.sei.cmu.edu/productlines/

[2] http://dl.acm.org/citation.cfm?id=1640002

[3] http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6693104

[4] http://menzies.us/pdf/13ibea.pdf

[5] http://dl.acm.org/citation.cfm?id=2190186

[6] http://www.ssbse.org/2011/fastabstracts/lopex-herrejon.pdf

[7] http://martinfjohansen.com/papers/Johansen2011c.pdf

[8] http://dl.acm.org/citation.cfm?id=1449918

[9] http://gsd.uwaterloo.ca/sites/default/files/vm-2012-berger.pdf

[10] http://www.iitk.ac.in/kangal/Deb_NSGA-II.pdf

[11] http://e-collection.library.ethz.ch/eserv/eth:24689/eth-24689-01.pdf

[12] https://github.com/DEAP/deap







