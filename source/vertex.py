# -*- coding: utf-8 -*-

'''
Módulo para vértices.
'''

from math import inf


class Vertex():

    '''
    Vértice.
    '''

    # Atributos privados
    _label: str
    _degree: int
    _in_degree: int
    _out_degree: int
    _neighbors: list
    _in_neighbors: list
    _out_neighbors: list
    _directed: bool

    def __init__(self, label: str) -> None:

        self._label = label
        self._degree = 0
        self._in_degree = 0
        self._out_degree = 0
        self._neighbors = []
        self._in_neighbors = []
        self._out_neighbors = []
        self._directed = False

    def __repr__(self) -> str:
        '''
        Retorna o rótulo quando chamado diretamente por outra função.
        '''

        return self._label

    @property
    def degree(self) -> int:
        '''
        Retorna o grau atual.
        '''

        if self._directed:
            return self._in_degree + self._out_degree

        return self._degree

    @property
    def in_degree(self) -> int:
        '''
        Retorna o grau com base nas arestas que levam até este vértice.
        '''

        return self._in_degree

    @property
    def out_degree(self) -> int:
        '''
        Retorna o grau com base nas arestas que saem deste vértice.
        '''

        return self._out_degree

    @property
    def neighbors(self) -> list:
        '''
        Retorna uma lista com os vértices da vizinhança.
        '''

        if self._directed:
            return self._in_neighbors + self._out_neighbors

        return self._neighbors

    @property
    def in_neighbors(self) -> list:
        '''
        Retorna os vizinhos que apontam para este vértice.
        '''

        return self._in_neighbors

    @property
    def out_neighbors(self) -> list:
        '''
        Retorna os vizinhos que este vértice aponta.
        '''

        return self._out_neighbors

    def set_connection(self, edge_matrix: list[list], v_index: int, directed: bool) -> None:
        '''
        Conecta o vértice a outro.
        '''

        self._directed = directed
        self._degree = 0
        self._in_degree = 0
        self._out_degree = 0
        self._neighbors.clear()
        self._in_neighbors.clear()
        self._out_neighbors.clear()

        if self._directed:

            for u_index, weight in enumerate(edge_matrix[v_index]):

                if weight != inf:
                    self._out_degree += 1
                    self._out_neighbors.append(u_index + 1)

            for u_index, row in enumerate(edge_matrix):

                if row[v_index] != inf:
                    self._in_degree += 1
                    self._in_neighbors.append(u_index + 1)
        else:

            for u_index, weight in enumerate(edge_matrix[v_index]):

                if weight != inf:
                    self._degree += 1
                    self._neighbors.append(u_index + 1)
