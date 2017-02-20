### CM Challanage

A simple orchestrator that takes a directed graph of dependencies, a list of reqested jobs, then calculates order to preform jobs and determines which jobs need to be re-run on each pass or can be read from cache.

example graph:

![Initial Graph](/figure1.png)

Resulting job queue after processing input:

![Job Queue](/figure2.png)

Simulation output:

'''
Simulate work for request ['F', 'E', 'G']
Initial Pass
A  was run
D  was run
G  was run
C  was run
E  was run
F  was run
Nth Pass
A  was run
D  was run
G  was loaded from cache
C  was loaded from cache
E  was run
F  was run

'''