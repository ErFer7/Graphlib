# -*- coding: utf-8 -*-

'''
Testes de unidade.
'''

from os.path import join
from math import inf
from source.graph import Graph


def test_create_graph():
    '''
    ...
    '''

    passed = False

    try:
        Graph(join("graphs", "test.net"))
        passed = True
    except Exception:
        pass
    assert passed


def test_vertex_count():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))
    assert graph.vertex_count() == 4


def test_edge_count():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))
    assert graph.edge_count() == 4


def test_degree():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))

    assert graph.degree(1) == 2
    assert graph.degree(2) == 2
    assert graph.degree(3) == 3
    assert graph.degree(4) == 1


def test_label():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))

    assert graph.label(1) == 'a'
    assert graph.label(2) == 'b'
    assert graph.label(3) == 'c'
    assert graph.label(4) == 'd'


def test_neighbors():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))

    neighbors_1 = graph.neighbors(1)
    neighbors_2 = graph.neighbors(2)
    neighbors_3 = graph.neighbors(3)
    neighbors_4 = graph.neighbors(4)

    assert neighbors_1 == [2, 3]
    assert neighbors_2 == [1, 3]
    assert neighbors_3 == [1, 2, 4]
    assert neighbors_4 == [3]


def test_has_edge():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))

    assert not graph.has_edge(1, 1)
    assert graph.has_edge(1, 2)
    assert graph.has_edge(1, 3)
    assert not graph.has_edge(1, 4)

    assert graph.has_edge(2, 1)
    assert not graph.has_edge(2, 2)
    assert graph.has_edge(2, 3)
    assert not graph.has_edge(2, 4)

    assert graph.has_edge(3, 1)
    assert graph.has_edge(3, 2)
    assert not graph.has_edge(3, 3)
    assert graph.has_edge(3, 4)

    assert not graph.has_edge(4, 1)
    assert not graph.has_edge(4, 2)
    assert graph.has_edge(4, 3)
    assert not graph.has_edge(4, 4)


def test_weight():
    '''
    ...
    '''

    graph = Graph(join("graphs", "test.net"))

    assert graph.weight(1, 1) == inf
    assert graph.weight(1, 2) == 1.0
    assert graph.weight(1, 3) == 1.0
    assert graph.weight(1, 4) == inf

    assert graph.weight(2, 1) == 1.0
    assert graph.weight(2, 2) == inf
    assert graph.weight(2, 3) == 1.0
    assert graph.weight(2, 4) == inf

    assert graph.weight(3, 1) == 1.0
    assert graph.weight(3, 2) == 1.0
    assert graph.weight(3, 3) == inf
    assert graph.weight(3, 4) == 1.0

    assert graph.weight(4, 1) == inf
    assert graph.weight(4, 2) == inf
    assert graph.weight(4, 3) == 1.0
    assert graph.weight(4, 4) == inf
