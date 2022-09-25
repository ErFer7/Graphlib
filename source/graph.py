# -*- coding: utf-8 -*-

'''
Módulo para o processamento de grafos.
'''

from source.vertex import Vertex
from source.edge import Edge


class Graph():

    '''
    Grafo.
    '''

    # Atributos privados
    __vertices: list
    __edges: list

    def __init__(self, file_name: str = None) -> None:

        self.__vertices = []
        self.__edges = []

        if file_name is not None:

            lines = ''

            with open(file_name, 'r', encoding="utf-8") as file:
                lines = file.readlines()

            adding_vertices = True

            for line in lines[1:]:

                if adding_vertices:

                    if not line.startswith("*edges"):
                        self.add_vertex(Vertex(line.split()[1]))
                    else:
                        adding_vertices = False
                else:

                    v_index = int(line.split()[0])
                    u_index = int(line.split()[1])
                    weight = float(line.split()[2])
                    self.connect_vertices(v_index, u_index, weight)

    # Métodos utilitários
    def add_vertex(self, vertex: Vertex) -> None:
        '''
        Adiciona um vértice.
        '''

        self.__vertices.append(vertex)

    def connect_vertices(self, v_index: int, u_index: int, weight: float) -> None:
        '''
        Adiciona um vértice.
        '''

        self.__edges.append(Edge(weight))
        self.__edges[-1].connect(self.__vertices[v_index - 1], self.__vertices[u_index - 1])

    # Métodos obrigatórios
    def vertex_count(self) -> int:
        '''
        Retorna a quantidade de vértices.
        '''

        return len(self.__vertices)

    def edge_count(self) -> int:
        '''
        Retorna a quantidade de arestas.
        '''

        return len(self.__edges)

    def degree(self, v_index: int) -> int:
        '''
        Retorna o grau do vértice v.
        '''

        return self.__vertices[v_index - 1].get_degree()

    def label(self, v_index: int) -> str:
        '''
        Retorna o rótulo do vértice v.
        '''

        return self.__vertices[v_index - 1].get_label()

    def neighbors(self, v_index: int) -> list:
        '''
        Retorna os vizinhos do vértice v.
        '''

        return self.__vertices[v_index - 1].neighbors()

    def has_edge(self, v_index: int, u_index: int) -> bool:
        '''
        Se {u, v} ∈ E, retorna verdadeiro; se não existir, retorna falso.
        '''

    def weight(self, v_index: int, u_index: int) -> float:
        '''
        Se {u, v} ∈ E, retorna o peso da aresta {u, v}; se não existir, retorna um valor infinito positivo.
        '''
