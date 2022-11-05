# -*- coding: utf-8 -*-

'''
Exercício 2 [Buscas] da atividade 1.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import breadth_first_search

file = input("Grafo a ser usado: ")
s = int(input("Índice do vértice (a partir de 1): "))
graph = Graph(join("graphs", file))

distances, ancestors = breadth_first_search(graph, s)

tree = {}

for i, distance in enumerate(distances):

    if distance not in tree:
        tree[distance] = [i + 1]
    else:
        tree[distance].append(i + 1)

sorted_tree = sorted(tree.items(), key=lambda x: x[0])

for k, i in sorted_tree:
    print(f"{k}: " + ", ".join(map(str, i)))
