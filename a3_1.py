# -*- coding: utf-8 -*-

'''
Exercício 1 [Edmonds-Karp] da atividade 3.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import edmonds_karp


file = input("Grafo a ser usado: ")
s_index = int(input("Vértice fonte: "))
t_index = int(input("Vértice destino: "))
graph = Graph(join("graphs", file))

max_flow = edmonds_karp(graph, s_index, t_index)

print(f"O fluxo máximo é: {max_flow}")
