# -*- coding: utf-8 -*-

'''
Exercício 2 [Buscas] da atividade 1.
'''

from os.path import join
from source.graph import Graph

def buscaEmLargura(graph:Graph,s:int):
    s = graph.get_vertex(s)
    C = {}
    D = {}
    A = {}
    C[s] = True
    D[s] = 0
    Q = []
    Q.append(s)
    while len(Q) != 0:
        u = Q.pop(0)
        for v in u.neighbors():
            if v not in C:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.append(v)
    return (D,A)


graph = Graph(join("graphs", "graph_1.txt"))
s = int(input())
nivel = buscaEmLargura(graph, s)[0]
arvore = {}
for i in nivel:
    if nivel[i] in arvore:
        arvore[nivel[i]].append[i]
    else:
        arvore[nivel[i]] = [i]

for i in arvore:
    print("%d: " % (i),end="")
    print(*arvore[i],sep=",")