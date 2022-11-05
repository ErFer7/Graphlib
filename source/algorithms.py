# -*- coding: utf-8 -*-

'''
Algoritmos.
'''

from math import inf
from source.graph import Graph


def breadth_first_search(graph: Graph, s_index: int) -> tuple[dict, dict]:
    '''
    Procura em largura.
    Índice incial: 1.
    '''

    visited = [False] * graph.vertex_count()
    distances = [inf] * graph.vertex_count()
    ancestors = [None] * graph.vertex_count()

    visited[s_index - 1] = True
    distances[s_index - 1] = 0

    queue = []
    queue.append(s_index)

    while len(queue) != 0:

        u_index = queue.pop(0)

        for v_index in graph.neighbors(u_index):

            v_index -= 1

            if not visited[v_index]:
                visited[v_index] = True
                distances[v_index] = distances[u_index - 1] + 1
                ancestors[v_index] = u_index
                queue.append(v_index + 1)

    return (distances, ancestors)


def depth_first_search(graph: Graph, s_index: int) -> tuple[list, list, list]:
    '''
    Procura em profundidade.
    Índice incial: 1.
    '''

    visited = [False] * graph.vertex_count()
    time = [inf] * graph.vertex_count()
    ancestors = [None] * graph.vertex_count()

    visited[s_index - 1] = True
    time[s_index - 1] = 0
    total_time = 0

    stack = []
    stack.append(s_index)

    while len(stack) != 0:

        total_time += 1
        u_vertex = stack.pop()
        time[u_vertex - 1] = total_time

        for v_index in graph.neighbors(u_vertex):

            v_index -= 1

            if not visited[v_index]:
                visited[v_index] = True
                ancestors[v_index] = u_vertex
                stack.append(v_index + 1)

    return (visited, time, ancestors)


def hierholzer(graph: Graph) -> tuple[bool, list]:
    '''
    Algoritmo de Hierholzer para a busca de ciclos Eulerianos.

    [Atualmente não funciona].
    '''

    available_vertices = {i: graph.neighbors(i) for i in range(graph.vertex_count())}

    for value in available_vertices.values():
        if len(value) % 2 != 0:
            return (False, [])

    begin = -1
    for key, value in available_vertices.items():
        if len(value) > 0:
            begin = key
            break
    if begin == -1:
        return (False, [])

    cycle = [begin]

    while True:
        for vertex in cycle:
            if len(available_vertices[vertex]) > 0:
                begin = vertex
                current = vertex
                break

        subcycle = [current]

        while True:
            next_ = available_vertices[current].pop()
            available_vertices[next_].remove(current)
            subcycle.append(next_)
            current = next_
            if current == begin:
                break

        index = cycle.index(begin)
        cycle[index:index + 1] = subcycle

        proceed = False
        for key, value in available_vertices.items():
            if len(value) > 0:
                proceed = True
                break

        if not proceed:
            break

    return (True, cycle)


def bellman_held_karp(graph: Graph) -> list:
    '''
    Algoritmo de Bellman-Held-Karp.
    '''

    raise NotImplementedError


def bellman_ford(graph: Graph, s_index: int) -> tuple[bool, dict, dict]:
    '''
    Algoritmo de Bellman-Ford.
    '''

    raise NotImplementedError


def dijkstra(graph: Graph, s_index: int) -> tuple[list, list]:
    '''
    Algoritmo de Dijkstra.
    Índice incial: 1.
    '''

    visited = [False] * graph.edge_count()
    distances = [inf] * graph.edge_count()
    ancestors = [None] * graph.edge_count()

    distances[s_index - 1] = 0.0

    while not all(visited):

        u_index = None

        min_distance = inf
        for i, distance in enumerate(distances):
            if distance < min_distance and not visited[i]:
                min_distance = distance
                u_index = i

        visited[u_index] = True

        for v_index in graph.neighbors(u_index + 1):

            v_index -= 1

            if not visited[v_index]:
                if distances[v_index] > distances[u_index] + graph.weight(u_index + 1, v_index + 1):
                    distances[v_index] = distances[u_index] + graph.weight(u_index + 1, v_index + 1)
                    ancestors[v_index] = u_index + 1

    return (distances, ancestors)


def floyd_warshall(graph: Graph):
    '''
    Algoritmo de Floyd-Warshall.
    '''

    D = []
    D.append(matrix_w(graph))
    size = graph.vertex_count()

    for k in range(1, size + 1):
        D.append(matrix_empty(size))

        for u in range(size):
            for v in range(size):
                D[k][u][v] = min(D[k - 1][u][v], D[k - 1][u][k - 1] + D[k - 1][k - 1][v])

    return D[-1]


def matrix_w(graph: Graph):
    '''
    Função auxiliar.
    '''

    D = graph.get_edges()

    for i in range(graph.vertex_count()):
        D[i][i] = 0

    return D

def matrix_empty(size: int):
    '''
    Função auxiliar.
    '''

    return [[None for i in range(size)] for i in range(size)]

def strongly_connected_components(graph: Graph):
    '''
    Algoritmo para a obtenção de componentes fortemente conexas.
    '''

    # visited, time, ancestors, f_time = scc_dfs(graph)
    # transposed_graph = Graph()

    raise NotImplementedError


def scc_dfs(graph: Graph) -> tuple[list, list, list, list]:
    '''
    Algoritmo DFS modificado.
    '''

    visited = [False] * graph.vertex_count()
    time = [inf] * graph.vertex_count()
    f_time = [inf] * graph.vertex_count()
    ancestors = [None] * graph.vertex_count()

    total_time = 0

    for v_index in range(graph.vertex_count()):

        if not visited[v_index]:
            scc_dfs_visit(graph, v_index, visited, time, ancestors, f_time, total_time)

    return (visited, time, ancestors, f_time)


def scc_dfs_visit(graph: Graph,
                  v_index: int,
                  visited: list,
                  time: list,
                  ancestors: list,
                  f_time: list,
                  total_time: int) -> None:
    '''
    Algoritmo recursivo de visita DFS.
    Índice incial: 0.
    '''

    visited[v_index] = True
    total_time += 1
    time[v_index] = total_time

    for u_index in graph.neighbors(v_index + 1):

        u_index -= 1

        if not visited[u_index]:
            ancestors[u_index] = v_index + 1
            scc_dfs_visit(graph, u_index, visited, time, ancestors, f_time, total_time)

    total_time += 1
    f_time = total_time
