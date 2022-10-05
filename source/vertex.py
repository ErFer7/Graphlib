# -*- coding: utf-8 -*-

'''
Módulo para vértices.
'''


class Vertex():

    '''
    Vértice.
    '''

    # Atributos privados
    _label: str
    _degree: int
    _neighbors: list

    def __init__(self, label: str) -> None:

        self._label = label
        self._degree = 0
        self._neighbors = []

    # Métodos utilitários
    def get_label(self) -> str:
        '''
        Retorna o rótulo.
        '''

        return self._label

    def get_degree(self) -> int:
        '''
        Retorna o grau atual.
        '''

        return self._degree

    def connect(self, vertex) -> None:
        '''
        Conecta o vértice a outro.
        '''

        self._neighbors.append(vertex)
        self._degree += 1

    def neighbors(self) -> list:
        '''
        Retorna uma lista com os vértices da vizinhança.
        '''

        return self._neighbors
