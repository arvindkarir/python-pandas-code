# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:15:46 2018

@author: User
"""

def findCycle(graph, start):
    colors = { node : 'white' for node in graph }
    colors[start] = 'gray'
    stack = [(None, start)] # store edge, but at this point we have not visited anyone
    while stack: # is not empty
        (prev, node) = stack.pop()  # get stored edge
        for neighbor in graph[node]: # for all the connections from node going forward
            if neighbor == prev: # going back where we are coming from
                pass # don't go back along the same edge
            elif colors[neighbor] == 'gray': # backedge exists
                return True
            else: # can't be anything else than WHITE...
                colors[neighbor] = 'gray'
                stack.append((node, neighbor)) # push edge on stack
    return False

#
#    while edgeStack != []:
#        prev, node = edgeStack.pop() # get the stored edge
#        for neighbor in G[node]:
#            if neighbor == prev:
#                pass
#            elif colors[neighbor] == 'white':
#                colors[neighbor] == 'gray'
#                tovisit.append(neighbor)
#            else:
#                colors[neighbor] = 'black'
#                tovisit.pop()
#        return False



def getEdges(anode, G):
    # this for nodes
    for keys, values in G.items():
        if anode in G.keys():
            return G[anode]
    #this for edges
#    alledges = []
#    for keys, values in G.items():
#        if anode in G.keys():
#            for neighbor in (G[anode]):
#                edges = anode, neighbor
#                alledges.append(edges)
#        else:
#            pass
#        return( alledges)


G1 = { 1 : [2, 5], 2 : [1, 3], 3 : [], 4 : [], 5 : [4]}
G2 = { 1 : [2, 4], 2 : [3, 4], 3 : [5], 4 : [], 5 : [2], 6 : []}

print(findCycle(G1,1))
print(findCycle(G2,1))
