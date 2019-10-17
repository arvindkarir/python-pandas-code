# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:52:32 2018

@author: User
"""

graph = { 1 : [2, 4], 2 : [3,4], 3 : [5], 4 : [], 5 : [2,6], 6 : []}

G1 = {1:[2,5], 2:[3], 5:[4], 3:[], 4:[]}
G2 = {1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]} # some problem in code below, this is not working for 1-2-1


def findCycle(graph):
    nodes = list(graph.keys())
    visitedNodes = []
#    print('nodes are"', nodes)
    while nodes:
        current = nodes.pop()
#        print('current node is:', current)
        children = graph[current]
#        print('its children are:', children)
        for child in children:
#            #path = {current: child}
#            print('the path is', path)
#            print('the child is', child)
            if child in visitedNodes or current in visitedNodes:
                return True
            else:
                visitedNodes.append(child)
#                print('updated visited', visitedNodes)
    return False


print(findCycle(graph))
print(findCycle(G1))
print(findCycle(G2))