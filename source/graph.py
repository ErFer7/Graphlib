# -*- coding: utf-8 -*-

'''
Graphlib

Módulo para o processamento de grafos.
'''

from math import inf
from source.vertex import Vertex


class Graph():

    '''
    Grafo.
    '''

    # Atributos privados
    _vertices: list[Vertex]
    _edges: list[list]
    _directed: bool

    def __init__(self, file_name: str = None) -> None:

        self._vertices = []
        self._edges = []
        self._directed = False

        if file_name is None:
            return

        lines = ''

        with open(file_name, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        adding_vertices = True

        for line in lines[1:]:

            if adding_vertices:

                if not (line.startswith("*edges") or line.startswith("*arcs")):
                    self.add_vertex(Vertex(line.split()[1]))
                else:
                    adding_vertices = False
                    self._directed = line.startswith("*arcs")

                    for i in range(self.vertex_count()):
                        self._edges.append([])
                        for _ in range(self.vertex_count()):
                            self._edges[i].append(inf)
            else:

                v_index = int(line.split()[0])
                u_index = int(line.split()[1])
                weight = float(line.split()[2])

                self.connect_vertices(v_index, u_index, weight)

    def __repr__(self) -> str:

        ret_str = ''

        for vertex in self._vertices:
            ret_str += "        " + str(vertex)

        ret_str += '\n'

        for i, line in enumerate(self._edges):

            ret_str += str(self._vertices[i]) + ' '

            for edge in line:
                ret_str += f"{edge: 8.2f} "

            ret_str += '\n'

        return ret_str

    # Métodos utilitários
    def add_vertex(self, vertex: Vertex) -> None:
        '''
        Adiciona um vértice.
        '''

        self._vertices.append(vertex)

    def get_vertex(self, v_index) -> Vertex:
        '''
        Retorna um vértice.
        '''

        return self._vertices[v_index - 1]

    def connect_vertices(self, v_index: int, u_index: int, weight: float) -> None:
        '''
        Adiciona um vértice.
        '''

        self._edges[v_index - 1][u_index - 1] = weight
        self._vertices[v_index - 1].connect(u_index)

        if not self._directed:
            self._edges[u_index - 1][v_index - 1] = weight
            self._vertices[u_index - 1].connect(v_index)

    def get_edges(self) -> list:
        '''
        Retorna lista de arestas
        '''
        return self._edges

    # Métodos obrigatórios
    def vertex_count(self) -> int:
        '''
        Retorna a quantidade de vértices.
        '''

        return len(self._vertices)

    def edge_count(self) -> int:
        '''
        Retorna a quantidade de arestas.
        '''

        return len(self._edges)

    def degree(self, v_index: int) -> int:
        '''
        Retorna o grau do vértice v.
        (Ainda não suporta grafos dirigidos).
        '''

        return self._vertices[v_index - 1].get_degree()

    def label(self, v_index: int) -> str:
        '''
        Retorna o rótulo do vértice v.
        '''

        return str(self._vertices[v_index - 1])

    def neighbors(self, v_index: int) -> list:
        '''
        Retorna os vizinhos do vértice v.
        (Ainda não suporta grafos dirigidos).
        '''

        return self._vertices[v_index - 1].neighbors()

    def has_edge(self, v_index: int, u_index: int) -> bool:
        '''
        Se {u, v} ∈ E, retorna verdadeiro; se não existir, retorna falso.
        '''

        return self._edges[v_index - 1][u_index - 1] != inf or self._edges[u_index - 1][v_index - 1] != inf

    def weight(self, v_index: int, u_index: int) -> float:
        '''
        Se {u, v} ∈ E, retorna o peso da aresta {u, v}; se não existir, retorna um valor infinito positivo.
        '''

        ret_val = self._edges[v_index - 1][u_index - 1]

        if ret_val == inf:
            return self._edges[u_index - 1][v_index - 1]

        return ret_val
