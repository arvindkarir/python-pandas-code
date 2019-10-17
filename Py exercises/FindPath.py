# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:03:26 2017
https://www.python.org/doc/essays/graphs/

The problem with this implementation is that it always goes A->B-> and so on while there could be A->C connection directly
This is DEFINITELY not find the shortest path
@author: User
"""

graph = {'A': [ 'B','C'],
             'B': ['C', 'D'],
             'C': [ 'D', 'F', 'E'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C', 'E']}

def find_path(graph, start, end, path=[]): #definition, begins with path as empty
        path = path + [start] # appends start to path
        if start == end:
            return path
        if not start in graph: #checks for repeat
            return None
        for node in graph[start]: #for each of the nodes in start (eg if B is start, it will check both C and D)
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

print(find_path(graph, 'A', 'F'))