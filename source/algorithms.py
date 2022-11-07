# -*- coding: utf-8 -*-

'''
Algoritmos.
'''

from math import inf
from random import randint
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

    D = graph.edges

    for i in range(graph.vertex_count()):
        D[i][i] = 0

    return D


def matrix_empty(size: int):
    '''
    Função auxiliar.
    '''

    return [[None for i in range(size)] for i in range(size)]


def kosaraju(graph: Graph):
    '''
    Algoritmo para a obtenção de componentes fortemente conexas.
    '''

    stack = []
    sccs = []
    visited = [False] * graph.vertex_count()
    transposed_visited = [False] * graph.vertex_count()

    transposed_graph = graph.transposed()

    for v_index in range(1, graph.vertex_count() + 1):
        kosaraju_dfs_stack(graph, v_index, visited, stack)

    for v_index in stack:

        scc = []
        kosaraju_dfs_scc(transposed_graph, v_index, transposed_visited, scc)

        if len(scc) > 0:
            sccs.append(scc)

    return sccs


def kosaraju_dfs_stack(graph: Graph, v_index: int, visited: list, stack: list):
    '''
    DFS para o algoritmo de Kosaraju, este algoritmo constrói o stack de visitas.
    '''

    if not visited[v_index - 1]:

        visited[v_index - 1] = True

        for u_index in graph.out_neighbors(v_index):
            kosaraju_dfs_stack(graph, u_index, visited, stack)

        stack.append(v_index)


def kosaraju_dfs_scc(graph: Graph, v_index: int, visited: list, scc: list):
    '''
    DFS para o algoritmo de Kosaraju, este algoritmo constrói uma lista com uma scc (strongly connected component).
    '''

    if not visited[v_index - 1]:

        visited[v_index - 1] = True
        scc.append(v_index)

        for u_index in graph.out_neighbors(v_index):
            kosaraju_dfs_scc(graph, u_index, visited, scc)


def kruskal(graph: Graph) -> Graph:
    '''
    Algoritmo de Kruskal.
    '''

    raise NotImplementedError


def prim(graph: Graph) -> Graph:
    '''
    Algoritmo de Prim levemente modificado.
    '''

    r_index = randint(1, graph.vertex_count())
    spanning_tree = graph.disconnected()
    visited = [False] * graph.vertex_count()

    visited[r_index - 1] = True
    edges = {}

    for u_index in graph.neighbors(r_index):
        edges[(r_index, u_index)] = graph.weight(r_index, u_index)

    while not all(visited):

        minimum_path = min(edges.values())
        v_index, u_index = list(edges.keys())[list(edges.values()).index(minimum_path)]

        if not visited[u_index - 1]:

            visited[u_index - 1] = True
            spanning_tree.add_edge(v_index, u_index, minimum_path)

            for n_index in graph.neighbors(u_index):
                if (n_index, u_index) not in edges:
                    edges[(u_index, n_index)] = graph.weight(u_index, n_index)

        del edges[(v_index, u_index)]

    return spanning_tree
