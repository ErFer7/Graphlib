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

for k, distance in distances.items():

    if distance not in tree:
        tree[distance] = [k]
    else:
        tree[distance].append(k)

for k, i in tree.items():

    print(f"{k}: " + ", ".join(map(str, i)))
