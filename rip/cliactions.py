"""
rip
"""

import subprocess
from typing import Any
import rip.helpers


def do_install(args: Any) -> None:
    """
    Performs the "install" action
    """
    lib = rip.helpers.set_lib(args.library)
    r_binary: str = rip.helpers.which_r(path=args.rpath, status=1)

    if args.requirements is None:
        pkgs = "', '".join(args.package)

        r_cmd = f"install.packages(c('{pkgs}'), lib={lib}, repos = '{args.cran}')"
        subprocess.run(
            [r_binary, "-s", "-e", r_cmd],
            check=False,
        )

    if args.package is None:
        with open(str(args.requirements), "r", encoding="utf8") as reqs_file:
            reqs = reqs_file.readlines()
        for req in reqs:
            req_split = req.split("==")
            r_cmd = f"remotes::install_version('{req_split[0]}', lib={lib}, repos='{args.cran}')"
            subprocess.run(
                [r_binary, "-s", "-e", r_cmd],
                check=False,
            )


def do_freeze(args: Any) -> None:
    """
    Performs the "freeze" action.
    Runs some R to inspect the installed packages and outputs them in the freeze format
    """
    lib = rip.helpers.set_lib(args.library)

    r_cmd = (
        f"invisible(apply(as.data.frame(installed.packages(lib.loc={lib}"
        ")[,c('Package', 'Version')]), 1, function(x){cat(x['Package']"
        ", '==', x['Version'], '\n', sep='')}))"
    )
    r_binary = rip.helpers.which_r(path=args.rpath, status=1)
    subprocess.run(
        [r_binary, "-s", "-e", r_cmd],
        check=False,
    )


def do_list(args: Any) -> None:
    """
    Performs the "list" actions.
    Runs some R to list the installed packages and their versions.
    """
    lib = rip.helpers.set_lib(args.library)

    r_cmd = (
        f"print(as.data.frame(installed.packages(lib.loc='{lib}'"
        ")[,c('Package', 'Version')]), row.names=F)"
    )
    r_binary = rip.helpers.which_r(path=args.rpath, status=1)
    subprocess.run(
        [r_binary, "-s", "-e", r_cmd],
        check=False,
    )


def do_search(args: Any) -> None:
    """
    Performs the "search" action.
    """
    r_binary = rip.helpers.which_r(path=args.rpath, status=1)
    r_search = (
        f"cat(available.packages(repos='{args.cran}')['{args.string}','Version'], '\n')"
    )
    try:
        result = subprocess.run(
            [
                r_binary,
                "-s",
                "-e",
                r_search,
            ],
            capture_output=True,
            encoding="utf8",
            check=True,
        )
        print(f"{args.string}: {result.stdout}", end="")
    except subprocess.CalledProcessError:
        print(f"No package called: {args.string}")


def do_status(args: Any) -> None:
    """
    Performs the status actions
    """
    print(args)
