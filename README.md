### CM Challanage

A simple example of orchestrator algorithm that takes a list of requested jobs, builds a dependency graph and calculates order to preform jobs.  One twist is that the algorithm also determines which jobs need to be re-run on each pass or can be read from cache (no recurring jobs in dependencies).

example job request and intital graph:

![Initial Graph](/figure1.png)

Resulting job queue after processing input:

![Job Queue](/figure2.png)

Simulation output:

```

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

```