# codingAssignment
Assignment Description

Objective A:
———————————
The objective of the exercise is to write a package that is able to extract the time to last byte distribution per object size class.

An example of the outcome desired is provided in the png file.

The input log file is provided in a csv format. 
The time to last byte = request time + transfer time + turnaround time

The object size classes are:

<100kB
>100kB<1MB
>1M<10MB
>10MB<100MB
>100MB<1GB

The use of Numpy, Pandas or any other helper framework is forbidden, write the algorithms from scratch please..

If you are applying for an entry level programming position Please write the program in: 

Python or Java


If you are applying for a senior level programming position Please write the program in: 

Python AND Java

If you want to impress us (Optional) also write it in:

C++

If you are applying for a senior position, discuss performance/resource usage comparison between different implementations (and languages).

Tip: Keep it simple but do not compromise on readability of your code.
———

Objective B:
———————————

Create a restful web service using the program written in Objective A that allows:
-Uploading a log file of the same profile in this exercise
-Verifying that the file is correctly formatted.
-Displaying the Outcome.
-Handling errors (example:file is too big, unable to open, etc..)
-Provide a serialized version of the results in json (do not forget schema validation!!)

Entry Level + Senior Level Position:

-Use the language/technology of your Choice, Provide a URL to your service/API.
-Provide documentation of your API.


Senior Level Position Only:

-Provide a UML design of your use cases, data model, execution model and sequence diagrams.
-Provide readme of how to install and dependencies.

Objective C (senior level Only, Optional stretch goal if you want to impress us)
——————————— 

-Create a persistence layer able to store logs and results and provide a web interface / serialized json interface to view / manage the results.  

-Modify the core packages to make the calculation of the results multithreaded.

-Provide monitoring of threads / logging of errors / issues.

-Provide the ability to configure the object size classes in Objective A (via the Restful API)



How you will be evaluated:

- Timeliness of the delivery
- Quality of the code
- Clarity of the code
- Speed of execution of the code
- Delivery Method
- Unit Testing
- Design and Documentation ability


You have:

24 hours to deliver Objective A
72 hours to deliver Objective B
96 hours to deliver Objective C (Senior Only if you want to impress us)


from the time this exercise would have been communicated to you by HR.

Have Fun! Good Luck!
