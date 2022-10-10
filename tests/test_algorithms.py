# -*- coding: utf-8 -*-

'''
Testes de unidade.
'''

from os.path import join
from source.graph import Graph
from source.algorithms import breadth_first_search


def test_bfs():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test_graph.net"))

    distances_a, ancestors_a = breadth_first_search(graph, 1)
    distances_b, ancestors_b = breadth_first_search(graph, 2)
    distances_c, ancestors_c = breadth_first_search(graph, 3)
    distances_d, ancestors_d = breadth_first_search(graph, 4)

    assert distances_a == {1: 0, 2: 1, 3: 1, 4: 2} and ancestors_a == {1: None, 2: 1, 3: 1, 4: 3}
    assert distances_b == {1: 1, 2: 0, 3: 1, 4: 2} and ancestors_b == {1: 2, 2: None, 3: 2, 4: 3}
    assert distances_c == {1: 1, 2: 1, 3: 0, 4: 1} and ancestors_c == {1: 3, 2: 3, 3: None, 4: 3}
    assert distances_d == {1: 2, 2: 2, 3: 1, 4: 0} and ancestors_d == {1: 3, 2: 3, 3: 4, 4: None}
