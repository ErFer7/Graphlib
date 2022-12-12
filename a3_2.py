# -*- coding: utf-8 -*-

'''
Exercício 2 [Hopcroft-Karp] da atividade 3.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import hopcroft_karp


# file = input("Grafo a ser usado: ")
file = "pequeno.net"
graph = Graph(join("graphs", file))

print(graph)

test = hopcroft_karp(graph, [1, 2, 3])

print(test)
