'''Grook.py implements a Brainf*ck derivative

Built using Elliot Chance's article on writing your own Brainf*ck interpreter
https://levelup.gitconnected.com/write-your-own-brainfuck-interpreter-98e828c72854

Author: Jeremy Swerdlow (jeremyjswerdlow@gmail.com)
'''
import argparse
import os
import sys

import ply.lex as lex
import ply.yacc as yacc

# Sets up lexer
tokens = (
    'INCREMENT',
    'DECREMENT',
    'SHIFT_LEFT',
    'SHIFT_RIGHT',
    'OUTPUT',
    'INPUT',
    'OPEN_LOOP',
    'CLOSE_LOOP',
)

# Per https://www.dabeaz.com/ply/ply.html, whitespace must use \s instead of a space.
t_INCREMENT = r'I\sam\sGroot\.\sI\sam\sGroot\.'
t_DECREMENT = r'I\sam\sGroot!\sI\sam\sGroot!'
t_SHIFT_LEFT = r'I\sam\sGroot\.\sI\sam\sGroot\?'
t_SHIFT_RIGHT = r'I\sam\sGroot\?\sI\sam\sGroot\.'
t_OUTPUT = r'I\sam\sGroot!\sI\sam\sGroot\?'
t_INPUT = r'I\sam\sGroot\?\sI\sam\sGroot!'
t_OPEN_LOOP = r'I\sam\sGroot!\sI\sam\sGroot\.'
t_CLOSE_LOOP = r'I\sam\sGroot\.\sI\sam\sGroot!'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Sets up the parser
def p_commands(p):
    """
    commands : command
             | commands command
    """
    if len(p) == 2:
        p[0] = Commands()
        p[0].commands = [p[1]]
        return

    if not p[1]:
        p[1] = Commands()

    p[1].commands.append(p[2])
    p[0] = p[1]


def p_command(p):
    """
    command : INCREMENT
            | DECREMENT
            | SHIFT_LEFT
            | SHIFT_RIGHT
            | OUTPUT
            | INPUT
            | loop
    """
    if isinstance(p[1], str):
        p[0] = Command(p[1])
    else:
        p[0] = p[1]


def p_loop(p):
    """
    loop : OPEN_LOOP commands CLOSE_LOOP
    """
    p[0] = Loop(p[2])


def p_error(p):
    print("Syntax error in input!")


# All classes defined to run Grook code
class Grook:
    "Holds the Grook source code until it's run"
    def __init__(self, source):
        self.source = source

    def run(self):
        "runs the Grook source code, using a finite size of data"
        self.data = [0] * 100
        self.location = 0
        commands = self.parse(self.source)
        commands.run(self)

    def parse(self, source):
        "parses the source code using yacc"
        lex.lex()
        parser = yacc.yacc()
        return parser.parse(source)

    def __str__(self):
        return str(self.parse(self.source))


class Commands:
    "Defines a collection of the commands for Grook"
    def __init__(self):
        self.commands = []

    def run(self, program):
        "runs each command within the commands object"
        for command in self.commands:
            command.run(program)

    def __str__(self):
        return ' '.join([str(command) for command in self.commands])


class Command:
    "Defines a command for parsing a Grook file"
    def __init__(self, command):
        self.command = command

    def run(self, program):
        "runs the command for the program"
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == 'I am Groot. I am Groot.':
            program.data[program.location] += 1
        if self.command == 'I am Groot! I am Groot!':
            program.data[program.location] -= 1
        if self.command == 'I am Groot. I am Groot?':
            program.location -= 1
        if self.command == 'I am Groot? I am Groot.':
            program.location += 1
        if self.command == 'I am Groot! I am Groot?':
            sys.stdout.write(chr(program.data[program.location]))

    def __str__(self):
        return self.command


class Loop:
    "Defines a loop for the Grook program structure"
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        "runs all commands within the loop as a loop"
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return 'I am Groot! I am Groot.' + str(self.commands) + 'I am Groot. I am Groot!'


# Main execution body
if __name__ == "__main__":
    # Set up our command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the input Grook file to run")
    parser.add_argument(
        "--save-generated",
        "-s",
        help="save the generated lex and yacc files",
        action="store_true",
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Get the source code
    with open(args.input, "r") as fh:
        source = fh.read()

    # Run the source code
    program = Grook(source)
    program.run()

    # Clean up (if needed)
    if not args.save_generated:
        os.remove("parser.out")
        os.remove("parsetab.py")
