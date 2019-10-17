# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:31:19 2018

@author: User
"""
import collections
#G1 = { 1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]}

G2 = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

def revGraph(graph):
    rev = {}
    adict = {}
    {k:str(v) for k,v in rev.items()}
    nodeslist = []
    newlist = []
    for key, value in graph.items():
        if not value:
            newlist.append(([], key))
        else:
            for v in value:
                newlist.append((key, v))
#    print(newlist)
    for path in newlist:
        nodeslist += [[path[0], path[1]]]
    print('list is', nodeslist)

    firstnodes = []
    secondnodes = []
    for nodes in nodeslist:
        firstnodes.append(str(nodes[0]) )
        secondnodes.append(str(nodes[1]))

    edges = (list(zip(firstnodes, secondnodes)))
    print(edges)

# [('1', '2'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '5'), ('[]', '4'), ('5', '2'), ('[]', '6')]
##################
#for name in file:
#    if name in list:
#        if dict.has_key(param):
#            dict[param].append(name)
#        else:
#            dict[param] = [name]
#    ########################
#
#    for edge in edges:
#        adict[edge[0]] = edge[1]
#        for key, value in adict.items():

    print (adict)

#        for key, value in list(edge):
#            d[key].append(value)
#    print(d)
#
#    for edge in edges:
#        if edge[0] not in rev:
#            rev[(edge[0])] = (edge[1])
#        rev[edge[0]] + edge[1]
#
#
#
#
##    for node in firstnodes:
##        for nodes in nodeslist:
##            if node == '[]':
##                rev[str(nodeslist[1])] = []
##                nodeslist.pop()
##            else:
##                if nodes in firstnodes:
##                    rev[str(nodes[0])].append(nodes[1])
##                else:
##                    rev[str(nodes[0])] = (nodes[1])
#
#    print(rev)
#
#    print(nodeslist)
#    for node in nodeslist:
#        if not node[0] in nodeslist:
#            [str(node[0])] = (node[1])
#        else:
#            [str(node[0])].append(node[1])



#
#
#        if not node[0]:
#            pass
#        else:
#            if not node[0] in rev:
#                rev[str(node[0])] = (node[1])
#            else:
#                rev[str(node[0])].append(node[1])
#    print(rev)


#    for key, value in newgraph.items():
#        for v in value:
#            if v in rev.keys():
#                rev[v] += (key)
#            else:
#                rev[v] = (key)
#
#    return rev

#name_dic[name_input] = []

#print(revGraph(G1))
print(revGraph(G2))