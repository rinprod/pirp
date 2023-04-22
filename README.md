# RIP

RIP Installs Packages, or, R Installer of Packages

Command line R package installer inspired by Python's "pip" tool.

This is currently an EXPERIMENTAL project, so you should probably avoid using it in production unless you're happy to deal with some bugs.

## Usage

`rip` isn't a direct reimplementation of pip but for R, but it does draw heavily from the key features of that tool.

This enables both R users as well as admins of R systems to perform useful package installation tasks.
For building new systems or working on specific projects, this can be a huge time saver.

```bash
rip --help
```

```output
usage: rip [-h] [-v] [-c CRAN] [-R RPATH] [-l LIBRARY]
           {install,list,search,status,freeze} ...

R Install Packages - Command line package installation for R

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CRAN, --cran CRAN  CRAN mirror to use [default: `get]
  -R RPATH, --rpath RPATH
                        path to your R installation [default: $PATH]
  -l LIBRARY, --library LIBRARY
                        path to the R library to use [default: `.libPaths()`]

Commands:
  {install,list,search,status,freeze}
    install             installs packages
    list                lists installed packages
    search              search CRAN for a package and print its version
    status              prints useful debugging information about your
                        environment
    freeze              prints output suitable to freeze the currently
                        installed packages

For more information please see the docs
```

## License

`rip` is made available under the MIT license.

See the `LICENSE` file for more.
