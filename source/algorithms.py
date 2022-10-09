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
