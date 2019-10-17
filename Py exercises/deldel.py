# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:34:04 2018

@author: User
"""
## Possible to use the node counting method to find out if the graph has cycle or not

from collections import defaultdict

def dfs(graph): # not using any start node - go thru all nodes
    visited = []
    stack = list(graph.keys()) # all keys in stack
    while stack:
        current = stack.pop()
        visited.append(current)
        neighbors = graph[current]
#        print(neighbors)
        for n in neighbors:
            if n not in visited:
                stack.append(n)

#            print('new stack is',stack)
#    print('visited', visited)
    nodecount = defaultdict(int)
    for node in visited:
        nodecount[node] += 1
    for k, v in nodecount.items():
        if v > 1:
            return True




graph = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

G2 = {1:[2,5], 2:[3], 5:[4], 3:[], 4:[]}

print(dfs(graph))
print(dfs(G2))