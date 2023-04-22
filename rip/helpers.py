"""
rip
"""

import subprocess
import sys
from typing import Optional


def which_r(
    path: Optional[str] = None,
    status: Optional[int] = None,
    exit_on_error: Optional[bool] = True,
) -> str:
    """
    checks for an installation of R at the provided path, or, if no path is
    supplied, on the system $PATH

    params:
    path   - path to the R installation
    status - exit code

    returns: True/False
    """
    error_state = False
    r_binary: str
    if path is None:
        r_binary = "R"
    else:
        r_binary = f"{path}/bin/R"

    try:
        subprocess.run([r_binary, "--help"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: R not found")
        print("Please make sure R is installed and on the $PATH or override with `-R`")
        error_state = True
    except FileNotFoundError:
        print("Error: R not found")
        print("Please make sure R is installed and on the $PATH or override with `-R`")
        error_state = True

    if error_state and status is not None:
        if exit_on_error:
            sys.exit(status)

    if error_state:
        return ""

    return r_binary


def set_lib(library: Optional[str]) -> str:
    """
    Set the appropriate library path

    Returns: String containg the library path to use
    """
    if library is None:
        lib = ".libPaths()"
    else:
        lib = f"'{library}'"
    return lib


def set_cran(cran: Optional[str]) -> str:
    """
    Set the appropriate CRAN repo

    Returns: String containg the CRAN repo to use
    """
    if cran is None:
        repo = "getOption('repos')"
    else:
        repo = f"'{cran}'"
    return repo
