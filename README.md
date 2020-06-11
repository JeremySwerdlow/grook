# Grook

Grook is an esolang inspired by [Ook!](https://esolangs.org/wiki/Ook!). Like its inspiration, Grook
is intended to be writeable by someone other than humans; in this case, it is meant for use by a
certain loveable [Marvel Character](https://www.marvel.com/characters/groot).

The repository contains several files related to the generation and running of Grook code. Please
see the short descriptions of each below.

Grook is in no way associated with or funded by Marvel or any other company. This is purely for fun!

## [`convert_to_grook.py`](convert_to_grook.py)

The `convert_to_grook.py` file serves the purpose of generating Grook code. It is a simple
translator for code from [Brainf*ck](https://en.wikipedia.org/wiki/Brainfuck) to Grook. It can be
called as follows:

```text
usage: convert_to_grook.py [-h] [--output OUTPUT] input

positional arguments:
  input                 the input file to convert

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        the output file to write to
```

## [`grook.py`](grook.py)

The `grook.py` file serves as an interpreter for Grook code. It was adapted from Elliot Chance's
guide *Write Your Own Brainf*ck Interpreter*, which can be found
[here](https://levelup.gitconnected.com/write-your-own-brainfuck-interpreter-98e828c72854).

It can be called as follows:

```text
usage: grook.py [-h] [--save-generated] input

positional arguments:
  input                 the input Grook file to run

optional arguments:
  -h, --help            show this help message and exit
  --save-generated, -s  save the generated lex and yacc files
```

## Contributing & Issues

This is an ongoing project; it does not have a full set of Turing operations, as the input delimeter
is currently ignored. There are other areas for improvement. Please feel free to open any Issues or
Pull Requests against the repository. Thanks in advance!
