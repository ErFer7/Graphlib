# -*- coding: utf-8 -*-

'''
Exercício 2 [Ordenação Topológica] da atividade 2.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import topological_sort


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

topological_sort_list = topological_sort(graph)

print(' → '.join(map(graph.label, topological_sort_list)) + '.')
