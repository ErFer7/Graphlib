# -*- coding: utf-8 -*-

'''
Módulo para vértices.
'''


class Vertex():

    '''
    Vértice.
    '''

    # Atributos privados
    __label: str
    __degree: int
    __edges: list

    def __init__(self, label: str) -> None:

        self.__label = label
        self.__edges = []
        self.__degree = 0

    # Métodos utilitários
    def get_label(self) -> str:
        '''
        Retorna o rótulo.
        '''

        return self.__label

    def get_degree(self) -> int:
        '''
        Retorna o grau atual.
        '''

        return self.__degree

    def get_edge(self, e_index: int):
        '''
        Retorna uma aresta.
        '''

        return self.__edges[e_index]

    def connect(self, edge) -> None:
        '''
        Conecta o vértice a uma aresta.
        '''

        self.__edges.append(edge)
        self.__degree += 1

    def neighbors(self) -> list:
        '''
        Retorna uma lista com os vértices da vizinhança.
        '''

        neighbors_list = []

        for edge in self.__edges:
            neighbors_list.append(edge.get_next(self.__label))
