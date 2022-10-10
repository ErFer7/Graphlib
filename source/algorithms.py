# -*- coding: utf-8 -*-

'''
Algoritmos.
'''

from source.graph import Graph


def breadth_first_search(graph: Graph, s_index: int) -> tuple[dict, dict]:
    '''
    Procura em largura.
    '''

    visited = [False] * graph.edge_count()
    distances = {}
    ancestors = {s_index: None}
    visited[s_index - 1] = True
    distances[s_index] = 0
    queue = []
    queue.append(s_index)

    while len(queue) != 0:

        u_vertex = queue.pop(0)

        for v_index in graph.neighbors(u_vertex):

            if not visited[v_index - 1]:
                visited[v_index - 1] = True
                distances[v_index] = distances[u_vertex] + 1
                ancestors[v_index] = u_vertex
                queue.append(v_index)

    return (distances, ancestors)


def min_path_Floyd_Warshall(graph:Graph):
    D = []
    D.append(matrix_W(graph))
    size = graph.vertex_count()
    for k in range(1,size+1):
        D.append(matrix_empty(size))
        for u in range(size):
            for v in range(size):
                D[k][u][v] = min(D[k-1][u][v],D[k-1][u][k-1]+D[k-1][k-1][v])
    return D[-1]


def matrix_W(graph:Graph):
    D = graph.get_edges()
    for i in range(graph.vertex_count()):
        D[i][i] = 0
    return D

def matrix_empty(size:int):
    return [[None for i in range(size)] for i in range(size)]
    