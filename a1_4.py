# -*- coding: utf-8 -*-

'''
Exercício 4 [Algoritmo de Bellman-Ford ou de Dijkstra] da atividade 1.
'''

from os.path import join
from source.algorithms import dijkstra
from source.graph import Graph


file = input("Grafo a ser usado: ")
s = int(input("Índice do vértice (a partir de 1): "))
graph = Graph(join("graphs", file))

distances, ancestors = dijkstra(graph, s)

for v in range(graph.edge_count()):

    path = []
    ancestor = v

    while True:

        path.insert(0, ancestor + 1)
        ancestor = ancestors[ancestor]

        if ancestor is None:
            break

        ancestor -= 1

    print(f"{v + 1}: " + ",".join(map(str, path)) + f"; d={int(distances[v])}")
