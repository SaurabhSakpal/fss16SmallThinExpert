##Title
 
Query Expansion via Wordnet for Effective Code Search


##Keywords

ii1. Wordnet: WordNet is a lexical database for the English language. It groups English words into sets of synonyms called synsets, provides short definitions and usage examples, and records a number of relations among these synonym sets or their members. WordNet can thus be seen as a combination of dictionary and thesaurus. 

ii2. Query Expansion: This is a method where Parts-Of-Speech (POS) tagging is performed on original query and for each word a synonym is found using WordNet. Thus if the original query had 5 keywords the expanded query will have around 30 keywords to match in the codebase.

ii3. Identifier Expansion: This is a method where we create identifiers for each method in the codebase. Identifiers are an important source of domain information and can often serve as a starting point in many program comprehension tasks. For instance, “CrystalPlayer” is split into “crystal player” and “Decimal2Hex” is split into “decimal hex”.

##iii1. Motivation:
A software change is a fundamental component of software maintenance. Software changes occur due to the continuous changing requirements of the stakeholders. Given a change request, developers need to understand the change request and figure out which parts of the current code base are related to the change request and need to be modified. To help developers perform this task, a number of text retrieval (TR)-based code search approaches have been proposed. These approaches take change request as input and return a ranked list of program elements that match the query. A common issue with all TR-based code search approaches is that the results of the retrieval depend greatly on the quality of the change query. Also, The words used in a query written by a maintainer can be different from the lexicon used by the developers. Thus, the maintainer will waste a lot of time rewriting a query, which affects the effectiveness of a code search tool to aid software maintenance tasks.

Reformulation will be more effective if multiple queries are created from the original query of the maintainer using synonyms of the words from the original query. This paper suggest a similar approach based on use of synonyms using wordnet. 

##iii2. Future Work
The current paper proposes synonym based query expansion method to search code repository and currently focuses on using this method on JavaScript/ECMAScript based coding projects. In future, the authors suggest using the proposed method for other programming languages based projects and implement additional search methods to evaluate effectiveness and generality of the proposed method.

##iii3. Related Work:
Query expansion has long been established as a way to improve the results returned by a Text Retrieval engine. There has been significant development on the forefront of using query expansion to help code search. Hill et al. proposed a query expansion tool named Conquer, which automatically extracts natural language phrases from source code identifiers and categorises the phrases and search results in a hierarchy. Conquer combines Verb-Direct Object pairs and contextual search technique. It introduces a novel natural language based approach to organise and present search results and suggest alternative query words.

##iii4. Baseline Results:
On average, the approach proposed in the paper improves the precision and recall of direct search by 40% and 24%, respectively. The results indicate that the alternative queries recommended by the proposed approach could reflect the true intention of the developers and the approach greatly helped the participants rewrite a good query close to the ideal query.
Also, the authors compared their approach with the recently proposed approach called as Conquer. On average, across all the tasks, the proposed approach outperforms Conquer’s precision and recall by 5% and 8%, respectively. Hence, we can conclude that the proposed approach performs better than Conquer search technique.

##Iv. Improvements:
The proposed method is only evaluated on JavaScript source code. A method is only good if it is generic and provides results with similar accuracy over all possible programming languages.

Also, not every method can be broken down into identifiers. There are certain words which are very specific to the domain of the project and also certain words are lingo used inside the project and finding synonyms for such words is impossible.   

##V. Connection to other papers:
This paper is motivated from following papers which propose reformuation of query to increase precision and accuracy.
 
 L. L. Pollock, K. Vijay-Shanker, E. Hill, G. Sridhara, and D. Shepherd, "Natural language-based software analyses and tools for software maintenance"

E. Hill, M. Roldan-Vega, J. A. Fails, and G. Mallet, “Nl-based query refinement and contextualised code search results: A user study”

The follwoing two papers have proposed use of query expansion to improve text retrieval engine. They use same verb-direct object pair method to improve the preccision which even the current paper uses.
 
J. Rocchio, “Relevance feedback in information retrieval”

D. Shepherd, Z. P. Fry, E. Hill, L. L. Pollock, and K. Vijay-Shanker, “Using natural language program analysis to locate and understand action oriented concerns” 
 
