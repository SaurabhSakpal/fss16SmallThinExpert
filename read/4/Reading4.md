##Title
 
A GUI Crawling-based technique for Android Mobile Application Testing

##Keywords

Activity: A Java component of Android application, instantiated at run time. It is responsible for presenting visual user interface for each task user can undertake. 

Activity States: An Activity instance in its lifetime passes through 3 main stages running, paused, stopped. At run time only one activity instance could be in run state, an instance can make dynamic call to other instances. Doing so the calling activity enters a paused state. When it becomes completely obscured by another activity instance, an activity is said to have entered the stop state.

Event : An event is a data input. Two types of events can be fired, user events (click, mouse etc. ) and events due to external input sources (GPS, sensors, etc.).

Event Driven Software (EDS): Software whose behavior is driven by several types of events (or inputs). Android applications are considered EDS.

##iii1 Motivation: 
The motivation for this work comes from the growing sales of Android devices and an increasing demand for suitable techniques and tools to support their testing. Since Android applications behavior is considered event driven, many existing EDS techniques can be adopted to carry out cost effective testing process. Based on crawling based techniques of Ajax applications, authors built a GUI crawler which produces a tree model. Each node of the tree represent user interfaces and edges correspond to event based transitions.

##iii2 Related Work: 
Authors cite various works that address various issues of functional and non-functional requirements testing like performance, reliability or security testing of mobile applications.

S. She, S. Sivapalan, I. Warren. Hermes: A Tool for testing Mobile Device Applications. 
This work introduces a tool for testing J2ME mobile application, which provides framework for writing test cases in XML and a distributed run time for executing tests automatically on the device rather than on an emulator.

 A. Marchetto, P. Tonella and F. Ricca. State-Based Testing of Ajax Web Applications. 
This paper presents a black box testing technique for GUI Adaptive Random Testing. Considering two types of events namely user events like data input and clicks and environmental events produced by GPS, blue tooth chips, network etc. Test cases consist of event sequences composed by pool of randomly selected events. 

##iii3 Study Instruments
To test the new approach and algorithm, a new tool called A2T2 (Android Automated Testing Tool) was developed. It consists of three parts. An instrumentation component, which discover uncaught exceptions in the application code to discover crashes. A GUI crawler which collects information (description of interfaces, triggered events) on obtained GUI tree. The crawler also reports crashes and event sequence producing them. The test case generator executable test cases supporting crash and regression testing. These test cases are able to replay event sequence  to verify presence of crashes and assertions pertaing to equivalence of interfaces.


##iii4 Future Work
Authors have just focused on user events. There could be other events which solicit a mobile application, they could be events produced by sensors, chips, network or just another application running on the same device. Future strategy can aim to include these types of events as well.
In order to detect the runtime crashes, the source code of the application needs to be instrumented through the A2T2 tool. It would be better if future enhancements can aim to run on application build.


##IV. Scope for improvement

The paper introduces a tool called A2T2 to supports this new technique. The tool consists of Java Code Instrumentation, the GUI crawler and the Test Case Generator. No empirical results have been provided to judge the effectiveness of the tool. A reason for this could be the absence of other Android GUI testing tools at the time this work was done. But it would have been better to highlight the benchmarks which the tool achieves. Author do mention this explicitly as one of the future scopes.

##V. Connection to other papers:

A. Marchetto, P. Tonella and F. Ricca. State-Based Testing of Ajax Web Applications. 
 A. Mesbah, A. van Deursen. Invariant-based automatic testing of AJAX user interfaces.
A. M. Memon and Qing Xie. Designing and comparing automated test oracles for GUI-based software applications.
These work introduce different criterion to tell if interfaces are equivalent or not.
The last work introduces interface comparison using test oracles having different degree of details or granularity. Influenced with these approaches authors checks if the interface obtained during the test run coincides with the previous test execution and their Activities, Event Handlers and Widget properties and Values are all the same. 

Studying the Fault-Detection Effectiveness of GUI Test Cases for Rapidly Evolving by A. M. Memon et al., authors define crash testing as a testing activity which aims at revealing exception faults due to uncaught exceptions. In the described approach, the source code of the application is instrumented through the A2T2 tool to find such uncaught exceptions. After this preliminary examination, during GUI exploration by the crawler first crash testing could be performed. 
