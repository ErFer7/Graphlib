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


def topological_sort(graph: Graph) -> list:
    '''
    Ordenação topológica.
    '''

    sorted_vertices = []
    visited = [False] * graph.vertex_count()

    for v_index in range(1, graph.vertex_count() + 1):
        if not visited[v_index - 1]:
            topological_sort_dfs(graph, v_index, visited, sorted_vertices)

    return sorted_vertices


def topological_sort_dfs(graph: Graph, v_index: int, visited: list, sorted_vertices: list) -> None:
    '''
    Função auxiliar.
    '''

    visited[v_index - 1] = True

    for u_index in graph.out_neighbors(v_index):
        if not visited[u_index - 1]:
            topological_sort_dfs(graph, u_index, visited, sorted_vertices)

    sorted_vertices.insert(0, v_index)


def kruskal(graph: Graph):
    '''
    Algoritmo de Kruskal para achar arvore geradora minima
    '''
    A = []
    vmod = graph.vertex_count()
    S = [[v] for v in range(vmod)]
    E = graph.valid_edges()
    E.sort(key=lambda e:e[2])
    for edge in E:
        if S[edge[0]-1] != S[edge[1]-1]:
            if edge not in A:
                A.append(edge)
            x = list(set().union(S[edge[0]-1],S[edge[1]-1]))
            for y in x:
                S[y] = x
    return A


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


def ford_fulkerson(graph: Graph) -> Graph:
    '''
    Algoritmo de Ford-Fulkerson
    '''

    raise NotImplementedError


def edmonds_karp(graph: Graph, s_index: int, t_index: int) -> Graph:
    '''
    Algoritmo de Edmonds-Karp
    '''

    residual_graph = graph.residual()
    flow_matrix = [[0.0 for _ in range(graph.vertex_count())] for _ in range(graph.vertex_count())]

    path = edmonds_karp_bfs(residual_graph, flow_matrix, s_index, t_index)

    while True:
        path = edmonds_karp_bfs(residual_graph, flow_matrix, s_index, t_index)

        if path is None:
            break

        flow = min(graph.weight(v_index, u_index) - flow_matrix[v_index - 1][u_index - 1] \
                   for v_index, u_index in path)

        for v_index, u_index in path:
            flow_matrix[v_index - 1][u_index - 1] += flow
            flow_matrix[u_index - 1][v_index - 1] -= flow

    return sum(flow_matrix[s_index - 1][i] for i in range(graph.vertex_count()))


def edmonds_karp_bfs(graph: Graph, flow_matrix: list[list[float]], s_index, t_index) -> list:

    '''
    BFS para Edmonds-Karp
    '''

    queue = []
    paths = {}

    queue.append(s_index)
    paths[s_index] = []

    while len(queue) > 0:

        u_index = queue.pop(0)

        for v_index in graph.in_neighbors(u_index):

            if v_index not in paths and graph.weight(u_index, v_index) - flow_matrix[u_index - 1][v_index - 1] > 0:
                paths[v_index] = paths[u_index] + [(u_index, v_index)]

                if v_index == t_index:
                    return paths[v_index]
                queue.append(v_index)

    return None


hopcroft_distances = []

def hopcroft_karp(graph: Graph, x_vertices: list):
    '''
    Algoritmo de Hopcroft-Karp.
    '''
    global hopcroft_distances
    hopcroft_distances = [inf] * graph.vertex_count()

    mate = [None] * graph.vertex_count()
    mate_size = 0

    while hopcroft_karp_bfs(graph, x_vertices, mate):
        for x_index in x_vertices:
            if mate[x_index] is None:
                if hopcroft_karp_dfs(graph, x_vertices, mate, x_index):
                    mate_size += 1

    return (get_final_mate_size(mate), mate)

def get_final_mate_size(mate):
    final_size = 0
    for i in mate:
        if i != 0 and i != None:
            final_size += 1
    return final_size

def hopcroft_karp_bfs(graph: Graph, x_vertices: list, mate: list):
    '''
    BFS para o Hopcroft-Karp.
    '''
    queue = []

    for x_index, x in enumerate(x_vertices):
        if mate[x_index] is None:
            hopcroft_distances[x_index - 1] = 0
            queue.append(x_index)
        else:
            hopcroft_distances[x_index - 1] = inf

    hopcroft_distances[0] = inf

    while len(queue) > 0:
        x_index = queue.pop(0)
        x_index = 0 if x_index is None else x_index

        if hopcroft_distances[x_index - 1] < hopcroft_distances[0]:
            for y_index, y in enumerate(graph.neighbors(x_index)):
                dist_index = 0 if mate[y_index - 1] is None else mate[y_index - 1]
                if hopcroft_distances[dist_index] == inf:
                    hopcroft_distances[dist_index] = hopcroft_distances[x_index - 1] + 1
                    queue.append(mate[y_index - 1])
    return hopcroft_distances[0] != inf


def hopcroft_karp_dfs(graph: Graph, x_vertices: list, mate: list, x_index: int):
    '''
    DFS para o Hopcroft-Karp.
    '''

    if x_index is not None:
        for y_index, y in enumerate(graph.neighbors(x_index)):
            dist_index = 0 if mate[y_index - 1] is None else mate[y_index - 1]
            if hopcroft_distances[dist_index] == hopcroft_distances[x_index - 1] + 1:
                if hopcroft_karp_dfs(graph, x_vertices, mate, mate[y_index - 1]):
                    mate[y_index - 1] = x_index
                    mate[x_index - 1] = y_index

                    return True

        hopcroft_distances[x_index - 1] = inf
        return False

    return True


def backtracking_coloring(graph: Graph):
    '''
    Algoritmo de coloração mínima.
    '''

    palette = [0]
    colored = [False] * graph.vertex_count()
    colors = [None] * graph.vertex_count()
    tried_colors = [[] for _ in range(graph.vertex_count())]
    history = []

    first_bfs_pass = True

    while not all(colored):

        queue = []
        if first_bfs_pass:
            queue.append(1)
            first_bfs_pass = False
        else:
            queue.append(colored.index(False) + 1)

        vertex_colored = color_vertex(graph, queue[0], palette, tried_colors, colors, history, colored)

        while len(queue) > 0:
            u_index = queue.pop(0)

            for v_index in graph.neighbors(u_index):

                if colored[v_index - 1]:
                    continue

                vertex_colored = color_vertex(graph, v_index, palette, tried_colors, colors, history, colored)

                if vertex_colored:
                    queue.append(v_index)
                else:
                    while True:
                        queue.clear()
                        last = history.pop()

                        if len(history) == 0:
                            palette.append(palette[-1] + 1)
                            tried_colors[last - 1].clear()

                        vertex_colored = color_vertex(graph, last, palette, tried_colors, colors, history, colored)

                        if vertex_colored:
                            queue.append(last)
                            break

                        tried_colors[last - 1].clear()
                        colors[last - 1] = None
                    break

    return (len(palette), colors)

def color_vertex(graph: Graph,
                 v_index: int,
                 palette: list,
                 tried_colors: list[list],
                 colors: list,
                 history: list,
                 colored: list) -> True:
    '''
    Função auxiliar de coloração.
    '''

    neighborhood_colors = []
    for w_index in graph.neighbors(v_index):
        neighborhood_colors.append(colors[w_index - 1])

    colored[v_index - 1] = False
    for color in palette:
        if color not in neighborhood_colors and color not in tried_colors[v_index - 1]:
            colored[v_index - 1] = True
            colors[v_index - 1] = color
            history.append(v_index)
            tried_colors[v_index - 1].append(color)
            break

    return colored[v_index - 1]
