# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:38:28 2018

@author: User
"""
def count_vertices(graph):
    count = 0
    for k in graph.items():
        count += 1
    print('There are %s vertices in the graph' % count)
    edge_list = []
    for k,v in graph.items():
        for i in range(len(v)):
            edge_list += [[v[i],k]]
    print('There are %s edges in this graph' % len(edge_list) )
    print('The edges are', edge_list)

def find_cycle(graph):
    visited = set()
    def visit(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, ()):
            print('for', vertex,'with neighbors', neighbor)
            if neighbor in visited or visit(neighbor):
                return True
        visited.remove(vertex)
        return False

    for k in graph.keys():
        print('going to visit,', k)
        if (visit(k)) == False:
            print('No cycle found')
        else:
            print('Cycle found', True)
            break




G1 = { 1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]}
G2 = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

#count_vertices(G1)
#count_vertices(G2)
find_cycle(G1)
find_cycle(G2)
find_cycle({1:[2,5], 2:[3], 5:[4], 3:[], 4:[]})

# pseudo code for a cycle (kind of, not the best)
#    start at any node
#    follow the children
#    and the children of children
#    if any of the children at any stage have children = starting node:
#        then there is a cycle