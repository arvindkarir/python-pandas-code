# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:21:32 2018

@author: User
"""

def bfs(graph, v):
    all = []
    Q = []
    Q.append(v)
    while Q != []:
        v = Q.pop(0)
        all.append(v)
        for n in graph[v]:
            if n not in Q and n not in all:
                Q.append(n)
    return all


def countVE(G):
    print("Vertices count:", (len(G.keys()) ))
    countE = 0
    for keys, vals in G.items():
        if vals != []:
            countE += len(vals)
    print('Edges count', countE, 'for Graph %s' % retrieve_name(G))

import inspect
def retrieve_name(var):
        """ Gets the name of var. Does it from the out most frame inner-wards. :param var: variable to get name from.
        return: string """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]




G1 = { 1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]}
G2 = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

(countVE(G1))
(countVE(G2))
