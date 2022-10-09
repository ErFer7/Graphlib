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

    def __repr__(self) -> str:
        '''
        Retorna o rótulo quando chamado diretamente por outra func
        '''
        return self._label

    def get_degree(self) -> int:
        '''
        Retorna o grau atual.
        '''

        return self._degree

    def connect(self, v_index) -> None:
        '''
        Conecta o vértice a outro.
        '''

        self._neighbors.append(v_index)
        self._degree += 1

    def neighbors(self) -> list:
        '''
        Retorna uma lista com os vértices da vizinhança.
        '''

        return self._neighbors
