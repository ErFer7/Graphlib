# -*- coding: utf-8 -*-

'''
Exercício 1 [Componentes Fortemente Conexas] da atividade 2.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import kosaraju


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

sccs = kosaraju(graph)

for scc in sccs:
    print(','.join(map(str, scc)))
