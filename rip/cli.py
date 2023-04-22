"""
rip
"""

import argparse
from typing import Optional, Sequence
from rip.version import __version__
from rip.cliactions import do_install, do_list, do_search, do_status, do_freeze


def arg_parser(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """
    Parses cli arguments for the command cli tool
    """
    parser = argparse.ArgumentParser(
        prog="rip",
        description="R Install Packages - Command line package installation for R",
        epilog="For more information please see the docs",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-c",
        "--cran",
        help="CRAN mirror to use [default: `get]",
    )
    parser.add_argument(
        "-R",
        "--rpath",
        help="path to your R installation [default: $PATH]",
    )
    parser.add_argument(
        "-l",
        "--library",
        help="path to the R library to use [default: `.libPaths()`]",
    )
    subparser = parser.add_subparsers(title="Commands", dest="subcmd")
    cmd_install = subparser.add_parser("install", help="installs packages")
    cmd_install.set_defaults(func=do_install)
    cmd_install_group = cmd_install.add_mutually_exclusive_group()
    cmd_install_group.add_argument(
        "-p",
        "--package",
        help="package name to install (multiple packages can be specified)",
        nargs="*",
    )
    cmd_install_group.add_argument(
        "-r",
        "--requirements",
        help="installs packages from a requirements file",
    )
    cmd_list = subparser.add_parser("list", help="lists installed packages")
    cmd_list.set_defaults(func=do_list)
    cmd_search = subparser.add_parser(
        "search", help="search CRAN for a package and print its version"
    )
    cmd_search.set_defaults(func=do_search)
    cmd_search.add_argument("string", help="string to search for")
    cmd_status = subparser.add_parser(
        "status", help="prints useful debugging information about your environment"
    )
    cmd_status.set_defaults(func=do_status)
    cmd_freeze = subparser.add_parser(
        "freeze",
        help="prints output suitable to freeze the currently installed packages",
    )
    cmd_freeze.set_defaults(func=do_freeze)
    return parser.parse_args(args)
