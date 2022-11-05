# -*- coding: utf-8 -*-

'''
Módulo para vértices.
'''

# TODO: Implementar o in e out das operações

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

    def __init__(self, label: str) -> None:

        self._label = label
        self._degree = 0
        self._in_degree = 0
        self._out_degree = 0
        self._neighbors = []
        self._in_neighbors = []
        self._out_neighbors = []

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

        return self._degree

    @property
    def neighbors(self) -> list:
        '''
        Retorna uma lista com os vértices da vizinhança.
        '''

        return self._neighbors

    def connect(self, v_index) -> None:
        '''
        Conecta o vértice a outro.
        '''

        self._neighbors.append(v_index)
        self._degree += 1
