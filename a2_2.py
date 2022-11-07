# -*- coding: utf-8 -*-

'''
Exercício 2 [Ordenação Topológica] da atividade 2.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import topological_ordering


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

print(topological_ordering(graph))