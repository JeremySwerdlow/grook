"""Maps brainf*ck to grook commands, and outputs the resulting grook code

Author: Jeremy Swerdlow (jeremyjswerdlow@gmail.com)
"""
import argparse
import os
import sys


mapping = {
    ".": "I am Groot! I am Groot?",
    "+": "I am Groot. I am Groot.",
    "-": "I am Groot! I am Groot!",
    "<": "I am Groot. I am Groot?",
    ">": "I am Groot? I am Groot.",
    ",": "I am Groot? I am Groot!",
    "[": "I am Groot! I am Groot.",
    "]": "I am Groot. I am Groot!",
}


def convert_to_grook(source: str) -> str:
    """converts brainf*ck code to grook

    positional arguments:
    source -- the brainf*ck source code
    """
    source = " ".join(list(source))  # add spaces between the commands
    for brfk, grook in mapping.items():
        source = source.replace(brfk, grook)  # replace with counterpart

    return source


# main execution body
if __name__ == "__main__":
    # Set up our command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the input file to convert")
    parser.add_argument("--output", "-o", help="the output file to write to")

    # Parse the command line arguments
    args = parser.parse_args()

    # Generate the grook code
    with open(args.input, "r") as fh:
        source = fh.read()
    grook = convert_to_grook(source)

    # Output the grook code as specified
    if args.output is not None:  # an output file was specified
        if os.path.exists(args.output):  # don't overwrite a preexisting file
            print(f"Output file '{args.output}' exists. Not overwriting.")
            sys.exit(1)
        with open(args.output, "w") as fh:
            fh.write(grook)
    else:  # no output file was specified
        print(grook)
