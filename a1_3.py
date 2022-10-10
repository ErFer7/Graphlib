# -*- coding: utf-8 -*-

'''
Exercício 3 [Ciclo Euleriano] da atividade 1.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import hierholzer


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

valid, cycle = hierholzer(graph)

if valid:
    print("1\n" + ",".join(map(lambda x: str(x + 1), cycle)))
else:
    print(0)
