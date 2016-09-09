##Title
 
Characterizing Failures in Mobile OSes: A Case Study with Android and Symbian

##Keywords

**ii1 Android** : The OS under consideration on which the experiment was performed. 

**ii2 Reliability** : By measuring the number and gravity of bugs, the reliability of the system is measured with the evolution of software.

**ii3 Bug fixes** : Analyzing the amount of work and effort required to be put in to fix the bugs.

##iii1. Motivation:

With the increase in many rich features being packed in new smartphones, there is an increasing number of system software defects being reported. Hence, it is a challenge to analyze the bugs and failures reported and identify the root cause along with solutions to problems. 

The major motivation for this is that according to the study 78% of the bugs needed just minor code changes. Every new feature introduced comes with a cost of new software, memory, battery etc as complexity impacts the reliability of the system.

Also, because Android and Symbian being open source, it is easier to analyze their dependability. Such analyses have been rare for mobile Operating Systems and quite common in desktop OSes.

##iii2. Future Work:

This paper presents future work on the lines of analyze the propagation of errors among various layers, primarily between application layer and middleware. 

Secondly, in future endeavors, the authors wish to explore more empirical relation between  complexity, customizability and reliability.

##iii3. Related Work:

Most of previous work in software reliability analysis is used to characterize various properties of failures. A very common approach is analyzing bug reports for common OSes. 

Chou et al. presented finding the OS errors by compiler modules to count bug density. In another instance, researchers attached event loggers to a set of 20+ symbian phones to record failure events. Authors were able to study relations between panics and user visible failures.

In another experiment, researchers created a catalog for risk based testing of wireless applications based on observed and predicted failures. 

##Iii.4. Study Instruments:

 Data collection is a major part of the paper. The bugs that are to be chosen need to be filtered. So, only the bugs marked as defects were chosen for scrutinization. The keywords that represent significant user inconvenience were used like - crash, shutdown, freeze, broken, failure, error, exception, and security. 

##Iv. Improvements:

System software bugs: There isn’t much talk about how bugs at one of stack effect the other levels which is a major factor because in case of mobile operating systems, the layers are tightly coupled and require more in depth study.
Ambiguity: There were occasions in the paper which left the real idea quite ambiguous. One example was how to take suggestions from users regarding the defects. 

##V. Connection to other papers:

This paper has a strong connection with others which focus on bug detection and bug fixing in android or other mobile operating systems. For e.g., Cuixiong Hu, Iulian Neamtiu. 2011. Automating GUI Testing for Android Applications. In proceedings of the 6th International Workshop on Automation of Software Test


These kind of papers aim to automate the process (to an extent) of bug anomaly detection and fixing. Although, major code changes still need to be carried out manually.