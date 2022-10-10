# -*- coding: utf-8 -*-

'''
Algoritmos.
'''

from math import inf
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

        u_index = queue.pop(0)

        for v_index in graph.neighbors(u_index):

            if not visited[v_index - 1]:
                visited[v_index - 1] = True
                distances[v_index] = distances[u_index] + 1
                ancestors[v_index] = u_index
                queue.append(v_index)

    return (distances, ancestors)


def depth_first_search(graph: Graph, s_index: int) -> tuple[dict, dict]:
    '''
    Procura em profundidade.
    [NÃO TESTADO]
    '''

    visited = [False] * graph.edge_count()
    time = {}
    ancestors = {s_index: None}

    visited[s_index - 1] = True
    time[s_index] = 0
    total_time = 0

    stack = []
    stack.append(s_index)

    while len(stack) != 0:

        total_time += 1
        u_vertex = stack.pop()
        time[u_vertex] = total_time

        for v_index in graph.neighbors(u_vertex):

            if not visited[v_index - 1]:
                visited[v_index - 1] = True
                ancestors[v_index] = u_vertex
                stack.append(v_index)

    return (visited, time, ancestors)


def hierholzer(graph: Graph) -> tuple[bool, list]:
    '''
    Algoritmo de Hierholzer para a busca de ciclos Eulerianos.
    '''


def bellman_held_karp(graph: Graph) -> list:
    '''
    Algoritmo de Bellman-Held-Karp.
    '''


def bellman_ford(graph: Graph, s_index: int) -> tuple[bool, dict, dict]:
    '''
    Algoritmo de Bellman-Ford.
    '''


def dijkstra(graph: Graph, s_index: int) -> tuple[list, dict]:
    '''
    Algoritmo de Dijkstra.
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


def floyd_warshall(graph: Graph) -> tuple:
    '''
    Algoritmo de Floyd-Warshall.
    '''
