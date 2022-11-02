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

    graph = Graph(join("graphs", "test.net"))

    distances_a, ancestors_a = breadth_first_search(graph, 1)
    distances_b, ancestors_b = breadth_first_search(graph, 2)
    distances_c, ancestors_c = breadth_first_search(graph, 3)
    distances_d, ancestors_d = breadth_first_search(graph, 4)

    test_distances_a = {1: 0, 2: 1, 3: 1, 4: 2}
    test_distances_b = {1: 1, 2: 0, 3: 1, 4: 2}
    test_distances_c = {1: 1, 2: 1, 3: 0, 4: 1}
    test_distances_d = {1: 2, 2: 2, 3: 1, 4: 0}

    test_ancestors_a = {1: None, 2: 1, 3: 1, 4: 3}
    test_ancestors_b = {1: 2, 2: None, 3: 2, 4: 3}
    test_ancestors_c = {1: 3, 2: 3, 3: None, 4: 3}
    test_ancestors_d = {1: 3, 2: 3, 3: 4, 4: None}

    for i in range(1, 5):
        assert distances_a.get(i) == test_distances_a[i]
        assert ancestors_a.get(i) == test_ancestors_a[i]

        assert distances_b.get(i) == test_distances_b[i]
        assert ancestors_b.get(i) == test_ancestors_b[i]

        assert distances_c.get(i) == test_distances_c[i]
        assert ancestors_c.get(i) == test_ancestors_c[i]

        assert distances_d.get(i) == test_distances_d[i]
        assert ancestors_d.get(i) == test_ancestors_d[i]
