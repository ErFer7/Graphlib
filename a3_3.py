# -*- coding: utf-8 -*-

'''
Exercício 3 [Coloração de Vértices] da atividade 3.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import backtracking_coloring


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

minimum_coloring, colors = backtracking_coloring(graph)

print(f"Quantidade mínima de cores: {minimum_coloring}")
print("Vértices e suas cores (representadas por um número):")

for i, color in enumerate(colors):
    print(f"{i + 1}: {color}")
