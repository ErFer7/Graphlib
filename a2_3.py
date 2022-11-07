# -*- coding: utf-8 -*-

'''
Exercício 3 [Kruskal ou Prim] da atividade 2.
'''

from math import inf
from os.path import join
from source.graph import Graph
from source.algorithms import prim


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

spanning_tree = prim(graph)

print(spanning_tree.weight_sum())

edges = []

for i, row in enumerate(spanning_tree.edges):
    for j, weight in enumerate(row):
        if weight != inf and j > i:
            edges.append(f"{i + 1}-{j + 1}")

print(", ".join(edges))
