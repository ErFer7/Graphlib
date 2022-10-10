# -*- coding: utf-8 -*-

'''
Exercício 5 [Algoritmo de Floyd-Warshall] da atividade 1.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import floyd_warshall


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))
D = floyd_warshall(graph)
for i in range(1,len(D)+1):
    print("%d:" % (i) +",".join(map(str,D[i-1])))
