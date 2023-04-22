"""
rip main
"""

import sys
import rip.cli


def main() -> None:
    """
    Kicks everything off for the cli tool
    """
    args = rip.cli.arg_parser(sys.argv[1:])
    try:
        args.func(args)
    except AttributeError:
        rip.cli.arg_parser(["-h"])
