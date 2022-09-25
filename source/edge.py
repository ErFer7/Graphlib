# -*- coding: utf-8 -*-

'''
Módulo para arestas.
'''


class Edge():

    '''
    Aresta.
    '''

    # Atributos privados
    __weight: float
    __vertex_v: None
    __vertex_u: None

    def __init__(self, weight: float) -> None:
        self.weight = weight

    # Métodos utilitários
    def connect(self, vertex_v, vertex_u) -> None:
        '''
        Conecta os vértices
        '''

        self.__vertex_v = vertex_v
        self.__vertex_v = vertex_u

    def get_next(self, caller_label):
        '''
        Retorna o vértice sucessor.
        '''

        if caller_label == self.__vertex_v.get_label():
            return self.__vertex_u
        else:
            return self.__vertex_v

    def get_weight(self) -> float:
        '''
        Retorna o peso.
        '''

        return self.__weight
