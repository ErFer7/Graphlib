# -*- coding: utf-8 -*-

'''
Interface do console.
'''

import re

from utils.graph_manipulator import GraphManipulator


class Interface():

    '''
    Representa a interface.
    '''

    _title: str
    _horizontal_bar: str
    _graph_manipulator: GraphManipulator
    _running: bool

    def __init__(self, version) -> None:

        self._title = f"Command-line graph manipulator\n{version}"
        self._horizontal_bar = '─' * 50
        self._graph_manipulator = GraphManipulator(self)
        self._running = False

        print(self._title)
        print(self._horizontal_bar)

    def run(self) -> None:
        '''
        Executa.
        '''

        self._running = True

        while self._running:

            command = input("[Graphlib] > ")
            self.parse(command)

    def parse(self, command: str):
        '''
        ...
        '''

        pattern = re.compile(r"(\"[^\"]+\"|[^\s\"]+)")
        command_list = pattern.split(command)[1:-1]

        while ' ' in command_list:
            command_list.remove(' ')

        if len(command_list) == 0:

            self.raise_error("Interface", "No input provided")
            return

        name = command_list[0]
        parameters = []
        options = {}
        parameter_target = "main"

        for string in command_list[1:]:

            if string.startswith("--"):

                if len(string) > 2:

                    options[string[2:]] = []
                    parameter_target = string[2:]
                else:

                    self.raise_error("Interface", "Syntax error")
                    return
            elif string.startswith('-'):

                if len(string) > 1:

                    options[string[1:]] = []
                    parameter_target = string[1:]
                else:

                    self.raise_error("Interface", "Syntax error")
                    return
            else:

                if parameter_target == "main":
                    parameters.append(string)
                else:
                    options[parameter_target].append(string)

        self._graph_manipulator.call_command(name, parameters, options)

    def print_output(self, text: str):
        '''
        Exibe no console.
        '''

        print(f"[Graphlib] < {text}")

    def raise_error(self, manager_name, description: str):
        '''
        Exibe um erro.
        '''

        self.print_output(f"({manager_name}): {description}")

    def stop(self):
        '''
        Termina a execução.
        '''

        self.print_output("Exiting...")
        self._running = False
