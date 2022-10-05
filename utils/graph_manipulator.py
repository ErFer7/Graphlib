# -*- coding: utf-8 -*-

'''
Manipulador de Grafos.
'''

from os.path import join
from secrets import choice
from string import ascii_lowercase


class GraphManipulator():

    '''
    Representa o manipulador de grafos.
    '''

    _interface: None

    def __init__(self, interface) -> None:

        self._interface = interface

    def call_command(self, name: str, parameters: list, options: dict) -> None:
        '''
        Comando chamado.
        '''

        match name:

            case "help":
                pass
            case "exit":
                self._interface.stop()
            case "generate":
                try:
                    self.generate_graph(parameters[0], parameters[1], parameters[2])
                except Exception:
                    self._interface.raise_error("Graph Manipulator", "Error")
            case _:
                self._interface.raise_error("Graph Manipulator", "Command not found")

    def generate_graph(self, vertices: int, edges: int, file_name: str) -> None:
        '''
        Gera um grafo
        '''

        lines = [f"*vertices {vertices}\n"]

        for i in range(1, int(vertices) + 1):
            lines.append(f"{i} {ascii_lowercase[(i - 1) % len(ascii_lowercase)] + str(i)}\n")

        lines.append(f"*edges {edges}\n")

        for _ in range(int(edges)):
            lines.append(f"{choice(range(1, int(vertices) + 1))} {choice(range(1, int(vertices) + 1))} {1.0}\n")

        with open(join("graphs", file_name + ".txt"), 'w+', encoding="utf-8") as file:
            file.writelines(lines)
