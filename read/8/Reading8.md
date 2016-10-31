##Title
 
Query Expansion based on crowd knowledge for code search 


##Keywords

ii1. Term Mismatch Problem: Also known as vocabulary problem in code search. Since queries given by users and code snippets most of the times do not contain the same words, effective retrieval is difficult.

ii2. Query Expansion: This is a method where Parts-Of-Speech (POS) tagging is performed on original query and for each word a synonym is found using WordNet. Thus if the original query had 5 keywords the expanded query will have around 30 keywords to match in the codebase.

ii3. Crowd Knowledge: In this paper refers to the Questio
n and Answer pairs extracted from stack Overflow. Software specific words are extracted from such corpus and used for Query Expansion. Q&A pairs contain useful knowledge about software development and hence refereed to as Crowd Knowledge

##iii1. Motivation:
With increasing number of repository sizes, code search is one of the major problems in software development. The complexity arises because typical language processing becomes irrelevant as many words have different meaning in code and natural language. Also in code search it is difficult to type in a exact matching query. Query extension is a technique of expanding the user query by inserting 'synonyms' of the query words. This can be  done globally through something like WordNet or the process can be automated by using the original query's search results. The latter process is refereed to as Pseudo Relevance Feedback (PRF). In this work authors have gathered PRF on original search result by retrieving information from Stack Overflow Q&A pairs. Stack Overflow being a major querying forum for software developers, provides a good corpus of related terms.  


##iii2. Future Work
Authors mention that future work can be done in two areas. First is analyzing queries based on the features like a metric to assess performance of the query and automatically suggesting reformulation strategy. Second area for future work is improving performance of query expansion by heuristic term frequency transformation model to capture the local saliency of a candidate term in the feedback documents. 

##iii3. Related Work:
In past various query expansion code search approaches have been attempted. The source to find 'synonyms' to the query words have included users' feedback, co-occurring query words, a WordNet or  a code-related Thesaurus. Some works also include methods to create word similarity resource by leveraging context of the word in source code, finding similar word pairs by parsing through code comments and method signatures or creating  WordNet from stack overflow Q&A pairs. But all these attempts do not make use of context of the query by not viewing query as a whole. 

##iii4. Baseline Results:
Three experiments were performed.
--RQ1: Check if QECK can improve performace of other code search algorithms
For evaluation authors apply their query expansion approach (QECK) to three different code search algorithms. First algorithm is BM25 based on information retrieval approach on Lucene. Second is Portfolio based on Vector Space Model (VSM), PageRank and Spreading Activation Network (SAN), the third is VF based on VSM and frequent item mining. There is significant difference in the mean value of precision once QECK is applied.

--RQ2: How the parameters affect the performance of QECK
Two parameters are number of PRF documents and number of expansion words. The optimal values of the parameters is found by fixing one and varying other. It is observed that the 3 algorithms perform best when number of PRF documents is 5 and number of expansion words are 9.

--RQ3: Whehter QECK + Rocchio's model is better than the sate-of-the-art Meili et al's WordNet
It is observed that Precision shows an improvement of 22% for QECK with Rocchio.
  
##Iv. Scope for Improvement:
In experiment RQ2, the two parameters number of PRF documents and number of expansion words are assumed independent of each other, no reasoning is presented to support this assumption And optimal values are found by varying them one at a time

##V. Connection to other papers:
The concept of Pseudo Relevance Feedback (PRF) is taken from the following work
S. Wang, D. Lo, and L. Jiang, “Active code search: Incorporating user feedback to improve code search relevance”

Stack Overflow Q&A pairs have been previously used for constructing software specific WordNet
 Y. Tian, D. Lo, and J. Lawall, “Automated construction of a software-specific word similarity database”
Y. Tian, D. Lo, and J. Lawall, “SEWordSim: Software-specific word similarity database”