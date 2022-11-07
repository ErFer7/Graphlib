# -*- coding: utf-8 -*-

'''
Exercício 3 [Kruskal ou Prim] da atividade 2.
'''
from os.path import join
from source.graph import Graph
from source.algorithms import kruskal


file = input("Grafo a ser usado: ")
graph = Graph(join("graphs", file))

tree = kruskal(graph)

print(sum(map(lambda e:e[2],tree)))
print(*map(lambda e:str(e[0])+'-'+str(e[1]),tree),sep=', ')
