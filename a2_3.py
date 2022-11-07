# -*- coding: utf-8 -*-

'''
Exercício 3 [Kruskal ou Prim] da atividade 2.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import prim


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

spanning_tree = prim(graph)

print(spanning_tree.weight_sum())

for row in spanning_tree.edges:
    pass
