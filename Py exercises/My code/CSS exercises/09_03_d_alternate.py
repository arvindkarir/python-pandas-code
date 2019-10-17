# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:38:28 2018

@author: User
"""
def reverse_g(graph):
    edge_list = []
    for k,v in graph.items():
        if not k in edge_list: # nodes with values = []
            edge_list.append(k)
        else:
            for each in v:
                if each in edge_list:
                    pass
                else:
                    edge_list.append(each)
    print(edge_list)

    reverse_graph = {k: [] for k in edge_list}
    for k, v in graph.items():
        for i in v:
            if i in edge_list:
                reverse_graph[i].append(k)
    print(list(reverse_graph.items()))



G1 = { 1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]}
G2 = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

reverse_g(G1)
reverse_g(G2)
#reverse_g({1:[2,5], 2:[3], 5:[4], 3:[], 4:[]})
