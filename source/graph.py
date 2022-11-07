# -*- coding: utf-8 -*-

'''
Graphlib

Módulo para o processamento de grafos.
'''

from math import inf
from source.vertex import Vertex


class Graph():

    '''
    Grafo.
    '''

    # Atributos privados
    _vertices: list[Vertex]
    _edges: list[list[float]]
    _directed: bool

    def __init__(self, file_name: str = None) -> None:

        self._vertices = []
        self._edges = []
        self._directed = False

        if file_name is None:
            return

        lines = ''

        with open(file_name, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        adding_vertices = True

        for line in lines[1:]:

            if adding_vertices:

                if not (line.startswith("*edges") or line.startswith("*arcs")):
                    self.add_vertex(Vertex(line.split()[1]))
                else:
                    adding_vertices = False
                    self._directed = line.startswith("*arcs")

                    for i in range(self.vertex_count()):
                        self._edges.append([])
                        for _ in range(self.vertex_count()):
                            self._edges[i].append(inf)
            else:

                v_index = int(line.split()[0])
                u_index = int(line.split()[1])
                weight = float(line.split()[2])

                self.add_edge(v_index, u_index, weight)

        self.update_vertices()

    def __repr__(self) -> str:

        ret_str = ''

        for vertex in self._vertices:
            ret_str += "        " + str(vertex)

        ret_str += '\n'

        for i, line in enumerate(self._edges):

            ret_str += str(self._vertices[i]) + ' '

            for edge in line:
                ret_str += f"{edge: 8.2f} "

            ret_str += '\n'

        return ret_str

    # Getters e Setters
    @property
    def edges(self) -> list[list[float]]:
        '''
        Retorna uma matriz de arestas.
        '''

        return self._edges

    # Métodos utilitários
    def set_attributes(self, vertices: list[Vertex], edges: list[list[float]], directed: bool) -> None:
        '''
        Define os atributos. Este método é usado na cópia de grafos.
        '''

        self._vertices = vertices
        self._edges = edges
        self._directed = directed

    def add_vertex(self, vertex: Vertex) -> None:
        '''
        Adiciona um vértice.
        '''

        self._vertices.append(vertex)

    def get_vertex(self, v_index) -> Vertex:
        '''
        Retorna um vértice.
        '''

        return self._vertices[v_index - 1]

    def add_edge(self, v_index: int, u_index: int, weight: float) -> None:
        '''
        Conecta as arestas.
        '''

        self._edges[v_index - 1][u_index - 1] = weight

        if not self._directed:
            self._edges[u_index - 1][v_index - 1] = weight

    def set_edge_weight(self, v_index: int, u_index: int, weight: float) -> None:
        '''
        Define o peso de uma aresta.
        '''

        self._edges[v_index][u_index] = weight

    def update_vertices(self) -> None:
        '''
        Atualiza as conexões dos vértices.
        '''

        for i, vertex in enumerate(self._vertices):
            vertex.set_connection(self._edges, i, self._directed)

    def transposed(self):
        '''
        Retorna o grafo transposto.
        '''

        graph = Graph()
        inf_matrix = [[inf for _ in range(self.vertex_count())] for _ in range(self.vertex_count())]

        graph.set_attributes(self._vertices.copy(),inf_matrix, self._directed)

        for i, row in enumerate(graph.edges):
            for j, _ in enumerate(row):
                graph.set_edge_weight(i, j, self._edges[j][i])

        graph.update_vertices()

        return graph

    # Métodos obrigatórios
    def vertex_count(self) -> int:
        '''
        Retorna a quantidade de vértices.
        '''

        return len(self._vertices)

    def edge_count(self) -> int:
        '''
        Retorna a quantidade de arestas.
        '''

        return len(self._edges)

    def degree(self, v_index: int) -> int:
        '''
        Retorna o grau do vértice v.
        '''

        return self._vertices[v_index - 1].degree

    def in_degree(self, v_index: int) -> int:
        '''
        Retorna o grau +.
        '''

        return self._vertices[v_index - 1].in_degree

    def out_degree(self, v_index: int) -> int:
        '''
        Retorna o grau -.
        '''

        return self._vertices[v_index - 1].out_degree

    def label(self, v_index: int) -> str:
        '''
        Retorna o rótulo do vértice v.
        '''

        return str(self._vertices[v_index - 1])

    def neighbors(self, v_index: int) -> list:
        '''
        Retorna os vizinhos do vértice v.
        '''

        return self._vertices[v_index - 1].neighbors

    def in_neighbors(self, v_index: int) -> list:
        '''
        Retorna os vizinhos do vértice v +.
        '''

        return self._vertices[v_index - 1].in_neighbors

    def out_neighbors(self, v_index: int) -> list:
        '''
        Retorna os vizinhos do vértice v -.
        '''

        return self._vertices[v_index - 1].out_neighbors

    def has_edge(self, v_index: int, u_index: int) -> bool:
        '''
        Se {u, v} ∈ E, retorna verdadeiro; se não existir, retorna falso.
        '''

        return self._edges[v_index - 1][u_index - 1] != inf or self._edges[u_index - 1][v_index - 1] != inf

    def weight(self, v_index: int, u_index: int) -> float:
        '''
        Se {u, v} ∈ E, retorna o peso da aresta {u, v}; se não existir, retorna um valor infinito positivo.
        '''

        ret_val = self._edges[v_index - 1][u_index - 1]

        if ret_val == inf:
            return self._edges[u_index - 1][v_index - 1]

        return ret_val
    
    def valid_edges(self) -> list:
        '''
        retorna lista de (u,v,w) para toda aresta/arco com w != inf
        '''
        valid = []
        for u in range(self.vertex_count()):
            for v in range(self.vertex_count()):
                if self._edges[u][v] != inf:
                    valid.append((u+1,v+1,self._edges[u][v]))
        return valid
