##Title
 
How to Effectively Use Topic Models for Software Engineering Tasks? An Approach Based on Genetic Algorithms

##Keywords


**ii1 LDA** : Latent Dirichlet Allocation (LDA) is a Topic Model used for information retrieval. In LDA, each document is viewed as a mixture of several topics and used to figure out the semantics of the document based on word occurrences.

**ii2 Topic Models** : Statistical model that is used to find hidden semantic structures in text documents. Topic models are intuitive in nature, and based on the occurrences of each word in the document. Topic models try to find the topic of the document. Probabilistic latent semantic indexing  is the most common topic model in use currently.

**ii3 Genetic Algorithms** : Genetic Algorithms (GA) is a metaheuristic approach based on the process of natural selection and belongs to the class of evolutionary algorithms. GA consists of fours parts namely: generation, natural selection, mutation and crossover.

##iii1. Motivation:

Topic Models are information retrieval methods that have recently been used to perform analysis of essential software engineering tasks. Unfortunately, Topic models, in all these approaches, have been used on software artifacts in a similar manner as they were used on natural language documents because the underlying assumption was that source code and natural language documents are similar. However, the results have been debatable and are not always as expected.

Source Code is repetitive and can be predicted, unlike natural language documents. Topic models designed for natural language model requires to find optimal configuration. But finding such configuration is very hard. Also, ad-hoc heuristic based methods result in non-optimal solutions. So it is necessary to take advantage of predictability and repetitive nature of source code and using genetic algorithms can definitely help in doing so.

##iii2. Future Work:

In this paper, the authors proposed an approach based on Genetic Algorithms called as LDA-GA. This approach determines the near-optimal configuration for LDA in the context of three important software engineering tasks, namely traceability link recovery, feature location, and software artifact labelling.

In future work the author plans to use LDA-GA on other software engineering tasks that use text analysis. Also the authors plan to colloborate the results reported in this paper on other data sets.

##iii3. Related Work:

Recent applications of LDA to SE tasks operate on models of software artifacts instead of operating directly on those artifacts. Approaches that generate these models require as input a textual corpus that represents the software artifacts being analysed. These corpus are made from scraping out the comments and other metadata from the artifact documents.

Several papers recently have used LDA on SE tasks and used ad-hoc heuristics to configure LDA. The performance of this approach has been suboptimal for all the SE tasks like feature location, bug localisation, impact analysis, source code.

Finding an LDA configuration that provides the best performance is a difficult task. Some papers recently provided a method to find optimal LDA configuration; however, these approaches focus only on identifying the number of topics that would result in the best performance of a task. But the main issue with all the methods is that they ignore all the other parameters that are required to apply LDA in practice.


##iii.4. Tutorial Material:

To understand this paper one should know what is LDA. Here is a good tutorial for noobs: http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/

##Iv. Improvements:

The paper doesn't perform extensive testing of model over different data sets. This is very important because what results are obtained for one data set might not be true for other data sets.

Also, the paper doesn't cover all the software engineering artifacts. There is a chance that this LDA-GA model might not be suitable for all the software engineering artifacts. 


##V. Connection to other papers:

Paper “Feature location in source code: A taxonomy and survey,” by B. Dit, M. Revelle, M. Gethers, and D. Poshyvanyk, proposes a method to use LDA for feature location in source code, while the current paper uses LDA-GA for the feature location. It's seen that LDA-GA is more efficient than the LDA method for feature selection in the source code.

LDA which is the crx of the paper was first proposed in the paper “Latent Dirichlet Allocation” by  D. M. Blei, A. Y. Ng, and M. I. Jordan. LDA being modular in nature has become the most used topic modelling technniqe and it can extended further as required.   
