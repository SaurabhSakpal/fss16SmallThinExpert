##Title
 
Empirical Studies on the NLP Techniques for Source Code Data Preprocessing


##Keywords

ii1. Program Comprehension: Comprehending the existing already established source code, the system in order to tweak, maintain or extend features. It is majorly composed of two parts: Structured data (the actual code part) and unstructured (e.g., requirement documents,  bug reports, erchives etc.). 

ii2. Source Code Preprocessing: Preprocessing is done to the code so that sense can be made out of the unstructured data. Some common examples are stemming, splitting, tokenization etc.

ii3. NLP Techniques: These are the techniques that are used for source code preprocessing. NLP techniques act as the means to provide input for IR techiques to be applied.

##iii1. Motivation: In a professional environment, program compreshension is a challenging task especially because the source code is a small percentage of the total. Some part of structured data also contains unstructured data like comments, identifiers etc which are used to make sense between the various entities. A common technique using the structured data is to create system dependency graph, object oriented class and member dependency class. Now, unstructured data is more difficult to be made sense of. This requires some preprocessing (NLP) and then processing can be done (IR). One such model is LDA.

Preprocessing using NLP is particularly important for this task because a code by  itself comprises a lot of components that can distract the IR operations. The primary aim is to obtain the programming sense and the developer's intent using the identifiers and comments, string literals etc. 

##iii2. Future Work: This was a good experiment to obtain empirical results among various NLP opertions, it is hard to generalize. Hence, the authors wish to test on more large scale programs. Further, a qualitative analysis of effect of each pre processing operations in the NLP phase for IR to perform even better. Explore even more number and variety of operations like pruning and it's effects in tandem with the existing ones. Increasing the number of topics of LDA.

##iii3. Related Work: There has been significant development on the forefront of constructing structured dependency for a program base in order to understand the code. System dependency graph, object oriented class are primary examples of it. 

##iii.4. Tutorial Material: To understand this paper one should know what is LDA. Here is a good tutorial for noobs: http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/

##Iv. Improvements: The paper compares the pre processing results between stemming, splitting and both together but there could be many other operations that could effect. The codebase used for the purpose of this paper is quite small and the results might not be valid for a larger codebase.

Also, depending only on one method (LDA) to develop a generalized empirical formula can be erroneous because it also depends on the data set.

##V. Connection to other papers: This paper is closely related to other papers in NLP, SE and IR fields.
G. Bavota, M. Gethers, R. Oliveto, D. Poshyvanyk, and
A. D. Lucia. Improving software modularization via
automated analysis of latent topics and dependencies.

The two papers share a similar motivation which is to build more sense and identify latent dependency between code and intent. 
 
 D. Poshyvanyk, Y.-G. Gu ́eh ́eneuc, A. Marcus,
G. Antoniol, and V. Rajlich. Feature location using
probabilistic ranking of methods based on execution
scenarios and information retrieval

These two papers use probabilistic methods for the process of information retrieval. 
