# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:00:38 2017
http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
Python program to print DFS traversal for complete graph
@author: User
"""

from collections import defaultdict
# https://docs.python.org/2/library/collections.html

class someGraph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def nodeVisit(self, v, visited):
        # Mark current node as visited, print it
        visited[v] = True
        print(v)

        # Recur for all vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.nodeVisit(i, visited)

    # DFS traversal, uses recursive nodeVisit
    def visitNode(self):
        V = len(self.graph)
        visited =[False]*(V)

        # Call the recursive function to print
        # DFS traversal from all vertice one by one
        for i in range(V):
            if visited[i] == False:
                self.nodeVisit(i, visited)

g = someGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Depth First Traversal")
g.visitNode()
