# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:22:31 2017

@author: User
"""
from collections import defaultdict

class someGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addPath(self, u, v):
        self.graph[u].append(v)

    def showPath(self, u):
        return (self.graph[u])

    def chkPath(self, src, dest):
        for key, value in self.graph.items():
            if src in key:
                if dest in value:
                    return ('link')
                else:
                    return ('not linked')


g = someGraph()
g.addPath('A', 'B')
g.addPath('A', 'C')
g.addPath('A', 'D')
g.addPath('A', 'E')
g.addPath('A', 'F')
g.addPath('A', 'G')
g.addPath('B', 'D')
g.addPath('B', 'F')
g.addPath('B', 'G')
g.addPath('C', 'D')
g.addPath('C', 'G')
g.addPath('D', 'E')
g.addPath('D', 'G')
g.addPath('E', 'F')
g.addPath('E', 'G')
g.addPath('F', 'G')

print(g.showPath('B'))
print(g.chkPath('D', 'G'))
print(g.chkPath('B', 'C'))
