##Title
 
Cuixiong Hu,  Iulian Neamtiu. 2011. Automating GUI Testing for Android Applications. In proceedings of the 6th International Workshop on Automation of Software Test 

##Keywords

**ii1 Testing Automation** : A testing scenario where derivation of test cases for both crash and regression testing can be automated.

**ii2 API Errors** : Errors caused by incompatibilities between the API version assumed by the application and the API version provided by the system

**ii3 Activity Errors** : Errors caused due to incorrect implementations of activity protocols.

**ii4 Unhandled Exception** : Exceptions that user code does not catch and causes the application to crash.

**ii5 Concurrency Errors** : Errors that occur due to the interaction of multiple processes or threads. 

##iii1 Motivation: 
The motivation for this work comes from the growing sales of Android devices and an increasing demand for suitable techniques and tools to support their testing. Also authors believe that Android application testing is challenging, though developed using Java, they differ from standard Java client-server model.

##iii2 Related Work: 
Characterizing failures in mobile oses: A case study with android and symbian by A. Kumar Maji, K. Hao, S. Sultana, and S. Bagchi. 2010
This paper studied bugs in Android and Symbian operating systems. The major focus of this paper has been grouping the bugs on the basis of operating system layer they are found on. Also, the paper doesn't do semantic categorizations of the bugs. Semantic categorization means  classifying the bugs into types like concurrency bug, I/O bug, API bug etc. This paper also studies the bug fixes to find how many lines of code was required to fix the bug and how it could have been avoided.

Model-based testing through a GUI: Formal Approaches to Software Testing by A. Kervinen, M. Maunumaa, T. Paakkonen and M. Katara. 2006
The paper present a formal model and architecture for testing concurrently running applications. This model is more rigorous and powerful. The model was put to test against mobile applications running on the Symbian platform and it found 6 bugs in those applications.

Guitar – a gui testing framework on sourceforge.com. 2010
GUITAR is a GUI testing framework for Java and Microsoft Windows applications. It is unclear if the framework can be used for Android applications because architecture of Android applications is way different from that of the MS Windows and Java application.

Generating event sequence-based test cases using gui runtime state feedback by X. Yuan and A. M. Memon. 2010
This paper suggests a framework to generate event-sequence based test cases for GUI applications. The framework takes a model-based approach for testing GUI-based applications. It can generate test cases automatically using a structural event generation graph. The framework  targets Java desktop applications, which are different from the Android mobile environment.

##iii3 Baseline results
Android Ripper was compared against Monkey, a random testing approach. Both the techniques were tested on an open-source Android application called “Wordpress for Android”. Release r394 of the Android application was used for testing. This release source code consists of 6 java packages, a total of 71 files containing 334 classes and 1,489 methods and total of 10017 executable lines of code. Monkey took 4.46 hours to find 3 crashes corresponding to bug B2 and reached 25.27 % line of code coverage. On the other hand Android Ripper took less than 5 hours to find 8 crashes related to 4 bugs and reached 38 % line of code coverage.   


##iii4 Future Work
This paper suggests two types of improvements. Firstly, not all errors are handled by the current framework. The future framework will try and handle all possible errors that are seen the android applications which will help in identifying much more defects. Some of the current unhandled exceptions are I/O exceptions, concurrency exceptions, API exceptions.

Secondly, the future work will try and extend the current framework to include model-based verification onto java static analysis tools. This will help in identifying pattern and state machine violations at the compile time.

##Scope for improvement

iv1 The framework described in the paper chooses an event  at random. from the available ones. Once the event is successfully completed, the activity of the Android application changes. The paper, however, fails to explain once the event is chosen randomly, what happens to the other events. Do we keep them in a pipeline or do we flush them? 

iv2 The framework entirely depends on log parsing to figure out bugs and exception. To figure out all possible exceptions we need to write several regex rules to match the exception seen in the log to one of the valid exceptions. This method to identify the bugs is inefficient. There is a high chance of missing out on a bug if we missed a regex rule to match a particular exception.  

iv3 Although 10 applications were selected by the authors in the paper for bug study and testing the framework. But none of the applications required sign-in. Sign-in is very important because it can cause session based bugs.

##Connection to other papers

Racerx: effective, static detection of race conditions and deadlocks by D. Engler and K. Ashcraft
The authors have planned to use this paper for extending the framework to find the concurrency bug in android applications. Concurrency bugs are one of the most seen bugs in the today's multithreaded world.

Characterizing failures in mobile oses: A case study with android and symbian by A. Kumar Maji, K. Hao, S. Sultana, and S. Bagchi. 2010
This paper is one of the motivations for the Android Automated GUI testing framework. This paper shows that the density of the bugs seen in the GUI of the mobile applications is way higher than the density of the bugs seen in the Desktop Applications. 



