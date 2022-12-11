# -*- coding: utf-8 -*-

'''
Exercício 1 [Edmonds-Karp] da atividade 3.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import edmonds_karp


# file = input("Grafo a ser usado: ")
file = "test_dir.net"
graph = Graph(join("graphs", file))

print(graph)

test = edmonds_karp(graph, 1, 4)

print(test)
