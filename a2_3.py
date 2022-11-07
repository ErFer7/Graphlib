# -*- coding: utf-8 -*-

'''
Exercício 3 [Kruskal ou Prim] da atividade 2.
'''
<<<<<<< HEAD
=======

from math import inf
>>>>>>> bee9628b2f8e054ca9a2365549b2c1ed9b18698b
from os.path import join
from source.graph import Graph
# from source.algorithms import kruskal
from source.algorithms import prim


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

# tree = kruskal(graph)

# print(sum(map(lambda e:e[2],tree)))
# print(*map(lambda e:str(e[0])+'-'+str(e[1]),tree),sep=', ')

spanning_tree = prim(graph)

print(spanning_tree.weight_sum())

edges = []

for i, row in enumerate(spanning_tree.edges):
    for j, weight in enumerate(row):
        if weight != inf and j > i:
            edges.append(f"{i + 1}-{j + 1}")

print(", ".join(edges))
