# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:15:11 2017

"""
from collections import deque

class task:
    
    def __init__(self, id, recurring):
        self.id = id
        self.dependencies = []
        self.children = []
        self.recurring = recurring
        

def build_job_queue(tasks):
    
    dependency_graph = {}
    in_q = deque(tasks)
    out_q = deque()
    
    while in_q:
        task = in_q.popleft()
        dependency_graph[task] = len(task.dependencies)
        
        for dependency in task.dependencies:
            dependency.children.append(task)
            if dependency not in dependency_graph:
                dependency_graph[dependency] = len(dependency.dependencies)
                in_q.append(dependency)
    
    while len(out_q) < len(dependency_graph):
        for task in dependency_graph:
            if dependency_graph[task] == 0:
                out_q.append(task)
                for child_task in task.children:
                    if task.recurring:
                            child_task.recurring = True
                    dependency_graph[child_task] -= 1
                dependency_graph[task] = -1
    return out_q

def orchestrator(tasks):
    
    cache = {}
    
    job_q = build_job_queue(tasks)

    print('Simulate work for request', [task.id for task in tasks])
    for i in range(2):
        print('Initial Pass') if i == 0 else print('Nth Pass')
        for job in job_q:
            if not job.recurring and job in cache:
                print (job.id, ' was loaded from cache')
            else:
                # RUN JOB
                cache[job] = True
                print (job.id, ' was run')
   

#Build Graph
A = task('A', True)
B = task('B', False)
C = task('C', False)
D = task('D', False)
E = task('E', False)
F = task('F', False)
G = task('G', False)

F.dependencies = [C,A]
E.dependencies = [D,C]
D.dependencies = [A]
C.dependencies = [G]


orchestrator([F, E, G])
    